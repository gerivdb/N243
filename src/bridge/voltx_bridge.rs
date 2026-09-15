// N243 — VOLTX Bridge
// IntentHash: 0xN243_VOLTX_BRIDGE_20260915
//
// Bridge entre le bus unifié VOLTX (Python, 5 canaux EGMI v0.7)
// et les runners N243 (Rust).
//
// Architecture:
//   VOLTX (Python)                  N243 (Rust)
//   ├── PLIX (Vision)             ↔ ├── LLUX agent
//   ├── PIANO (Audio)             ↔ ├── TIMX agent
//   ├── TALEX (Narration)         ↔ ├── ROOTX agent
//   ├── SPIDX (Graphe)            ↔ ├── TLM-CORE agent
//   └── WAZAA (Bus)               ↔ └── WAZAA bridge
//
// Conforme ADR-VOLTX-N243-INTEGRATION-20260915 et
// INTENT-VOLTX-N243-INTEGRATION-20260915.

use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use thiserror::Error;

// ------------------------------------------------------------------
// Canaux VOLTX (EGMI v0.7)
// ------------------------------------------------------------------

/// Canaux du bus unifié VOLTX.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum VoltxChannel {
    /// Vision — traitement d'images, detection d'objets
    Plix,
    /// Audio — sonification, transcription
    Piano,
    /// Narration — génération de récits TALEX
    Talex,
    /// Graphe — SPIDX, indexation sémantique
    Spidx,
    /// Bus central — WAZAA events
    Wazaa,
}

impl VoltxChannel {
    /// Retourne le nom du canal pour le bus WAZAA.
    pub fn topic(&self) -> &'static str {
        match self {
            VoltxChannel::Plix => "voltx/plix",
            VoltxChannel::Piano => "voltx/piano",
            VoltxChannel::Talex => "voltx/talex",
            VoltxChannel::Spidx => "voltx/spidx",
            VoltxChannel::Wazaa => "voltx/wazaa",
        }
    }

    /// Retourne le runner N243 associé.
    pub fn runner(&self) -> &'static str {
        match self {
            VoltxChannel::Plix => "LLUX",
            VoltxChannel::Piano => "TIMX",
            VoltxChannel::Talex => "ROOTX",
            VoltxChannel::Spidx => "TLM-CORE",
            VoltxChannel::Wazaa => "ORCHESTRATOR",
        }
    }

    /// Retourne tous les canaux.
    pub fn all() -> &'static [VoltxChannel] {
        &[
            VoltxChannel::Plix,
            VoltxChannel::Piano,
            VoltxChannel::Talex,
            VoltxChannel::Spidx,
            VoltxChannel::Wazaa,
        ]
    }
}

impl std::fmt::Display for VoltxChannel {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            VoltxChannel::Plix => write!(f, "PLIX"),
            VoltxChannel::Piano => write!(f, "PIANO"),
            VoltxChannel::Talex => write!(f, "TALEX"),
            VoltxChannel::Spidx => write!(f, "SPIDX"),
            VoltxChannel::Wazaa => write!(f, "WAZAA"),
        }
    }
}

// ------------------------------------------------------------------
// Messages VOLTX
// ------------------------------------------------------------------

/// Message échangé sur le bus VOLTX.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct VoltxMessage {
    pub id: uuid::Uuid,
    pub channel: VoltxChannel,
    pub payload: serde_json::Value,
    pub source: String,
    pub timestamp: chrono::DateTime<chrono::Utc>,
    pub intent_hash: String,
}

impl VoltxMessage {
    /// Crée un nouveau message VOLTX.
    pub fn new(
        channel: VoltxChannel,
        payload: serde_json::Value,
        source: impl Into<String>,
        intent_hash: impl Into<String>,
    ) -> Self {
        Self {
            id: uuid::Uuid::new_v4(),
            channel,
            payload,
            source: source.into(),
            timestamp: chrono::Utc::now(),
            intent_hash: intent_hash.into(),
        }
    }
}

// ------------------------------------------------------------------
// Erreurs
// ------------------------------------------------------------------

/// Erreurs du bridge VOLTX.
#[derive(Error, Debug)]
pub enum VoltxBridgeError {
    #[error("Bridge not connected")]
    NotConnected,
    #[error("Channel not supported: {0}")]
    UnsupportedChannel(String),
    #[error("Serialization error: {0}")]
    SerializationError(#[from] serde_json::Error),
    #[error("IO error: {0}")]
    IoError(#[from] std::io::Error),
}

pub type VoltxBridgeResult<T> = Result<T, VoltxBridgeError>;

// ------------------------------------------------------------------
// VOLTX Bridge
// ------------------------------------------------------------------

/// Bridge VOLTX ↔ N243.
///
/// Gère la communication entre les 5 canaux VOLTX et les runners N243
/// via le bus WAZAA.
#[derive(Debug, Clone, Default)]
pub struct VoltxBridge {
    /// Connexion au bus WAZAA (déléguée à WazaaBridge)
    connected: bool,
    /// Canaux actifs
    active_channels: HashMap<VoltxChannel, bool>,
    /// Messages en attente de publication
    pending: Vec<VoltxMessage>,
}

impl VoltxBridge {
    /// Crée un nouveau bridge VOLTX.
    pub fn new() -> Self {
        let mut active_channels = HashMap::new();
        for channel in VoltxChannel::all() {
            active_channels.insert(*channel, false);
        }
        Self {
            connected: false,
            active_channels,
            pending: Vec::new(),
        }
    }

    /// Connecte le bridge au bus WAZAA et active tous les canaux.
    pub fn connect(&mut self) -> VoltxBridgeResult<()> {
        // TODO: établir la connexion réelle avec le bus WAZAA
        // (TCP localhost:8787 ou HTTP localhost:8080)
        self.connected = true;
        for channel in VoltxChannel::all() {
            self.active_channels.insert(*channel, true);
        }
        Ok(())
    }

    /// Déconnecte le bridge.
    pub fn disconnect(&mut self) {
        self.connected = false;
        for channel in VoltxChannel::all() {
            self.active_channels.insert(*channel, false);
        }
        self.pending.clear();
    }

    /// Vérifie si le bridge est connecté.
    pub fn is_connected(&self) -> bool {
        self.connected
    }

    /// Vérifie si un canal est actif.
    pub fn is_channel_active(&self, channel: VoltxChannel) -> bool {
        self.active_channels.get(&channel).copied().unwrap_or(false)
    }

    /// Publie un message sur un canal VOLTX.
    pub fn publish(
        &mut self,
        channel: VoltxChannel,
        payload: serde_json::Value,
        source: impl Into<String>,
        intent_hash: impl Into<String>,
    ) -> VoltxBridgeResult<uuid::Uuid> {
        if !self.connected {
            return Err(VoltxBridgeError::NotConnected);
        }
        if !self.is_channel_active(channel) {
            return Err(VoltxBridgeError::UnsupportedChannel(channel.to_string()));
        }

        let msg = VoltxMessage::new(channel, payload, source, intent_hash);
        let msg_id = msg.id;

        // TODO: publication réelle sur le bus WAZAA
        // Pour l'instant, on stocke dans pending pour debug
        self.pending.push(msg);

        Ok(msg_id)
    }

    /// Souscrit à un canal VOLTX avec un handler.
    ///
    /// Le handler est appelé pour chaque message reçu sur le canal.
    pub fn subscribe<F>(&mut self, _channel: VoltxChannel, _handler: F) -> VoltxBridgeResult<()>
    where
        F: Fn(VoltxMessage) + Send + Sync + 'static,
    {
        if !self.connected {
            return Err(VoltxBridgeError::NotConnected);
        }
        // TODO: souscription réelle au bus WAZAA
        Ok(())
    }

    /// Publie un événement de contrôle N243 sur VOLTX.
    pub fn publish_control_event(
        &mut self,
        runner: &str,
        event: &str,
        data: serde_json::Value,
    ) -> VoltxBridgeResult<uuid::Uuid> {
        let payload = serde_json::json!({
            "runner": runner,
            "event": event,
            "data": data,
        });
        self.publish(
            VoltxChannel::Wazaa,
            payload,
            "N243",
            format!("0xN243_CONTROL_{}", chrono::Utc::now().format("%Y%m%dT%H%M%SZ")),
        )
    }

    /// Retourne le nombre de messages en attente.
    pub fn pending_count(&self) -> usize {
        self.pending.len()
    }

    /// Vide la file des messages en attente et retourne les IDs.
    pub fn flush_pending(&mut self) -> Vec<uuid::Uuid> {
        let ids: Vec<uuid::Uuid> = self.pending.iter().map(|m| m.id).collect();
        self.pending.clear();
        ids
    }
}

// ------------------------------------------------------------------
// Tests
// ------------------------------------------------------------------

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_channel_topics() {
        assert_eq!(VoltxChannel::Plix.topic(), "voltx/plix");
        assert_eq!(VoltxChannel::Piano.topic(), "voltx/piano");
        assert_eq!(VoltxChannel::Talex.topic(), "voltx/talex");
        assert_eq!(VoltxChannel::Spidx.topic(), "voltx/spidx");
        assert_eq!(VoltxChannel::Wazaa.topic(), "voltx/wazaa");
    }

    #[test]
    fn test_channel_runners() {
        assert_eq!(VoltxChannel::Plix.runner(), "LLUX");
        assert_eq!(VoltxChannel::Piano.runner(), "TIMX");
        assert_eq!(VoltxChannel::Talex.runner(), "ROOTX");
        assert_eq!(VoltxChannel::Spidx.runner(), "TLM-CORE");
        assert_eq!(VoltxChannel::Wazaa.runner(), "ORCHESTRATOR");
    }

    #[test]
    fn test_bridge_connect_disconnect() {
        let mut bridge = VoltxBridge::new();
        assert!(!bridge.is_connected());
        assert!(!bridge.is_channel_active(VoltxChannel::Plix));

        bridge.connect().unwrap();
        assert!(bridge.is_connected());
        assert!(bridge.is_channel_active(VoltxChannel::Plix));

        bridge.disconnect();
        assert!(!bridge.is_connected());
        assert!(!bridge.is_channel_active(VoltxChannel::Plix));
    }

    #[test]
    fn test_publish_requires_connection() {
        let mut bridge = VoltxBridge::new();
        let result = bridge.publish(
            VoltxChannel::Plix,
            serde_json::json!({"test": true}),
            "TEST",
            "0xTEST",
        );
        assert!(result.is_err());
    }

    #[test]
    fn test_publish_when_connected() {
        let mut bridge = VoltxBridge::new();
        bridge.connect().unwrap();

        let msg_id = bridge
            .publish(
                VoltxChannel::Plix,
                serde_json::json!({"test": true}),
                "TEST",
                "0xTEST",
            )
            .unwrap();
        assert_eq!(bridge.pending_count(), 1);

        let ids = bridge.flush_pending();
        assert_eq!(ids.len(), 1);
        assert_eq!(ids[0], msg_id);
        assert_eq!(bridge.pending_count(), 0);
    }
}
