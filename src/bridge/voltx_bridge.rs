// N243 — VOLTX Bridge
// IntentHash: 0xN243_VOLTX_BRIDGE_20260915

use serde::{Deserialize, Serialize};
use std::collections::HashMap;

/// Canaux VOLTX intégrés à N243
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub enum VoltxChannel {
    Plix,    // Vision → Audio
    Piano,   // Audio → Narration
    Talex,   // Narration → Graphe
    Spidx,   // Graphe → Diffusion
    Wazaa,   // Diffusion → Vision
}

impl VoltxChannel {
    pub fn as_str(&self) -> &'static str {
        match self {
            VoltxChannel::Plix => "plix",
            VoltxChannel::Piano => "piano",
            VoltxChannel::Talex => "talex",
            VoltxChannel::Spidx => "spidx",
            VoltxChannel::Wazaa => "wazaa",
        }
    }

    pub fn from_str(s: &str) -> Option<Self> {
        match s {
            "plix" => Some(VoltxChannel::Plix),
            "piano" => Some(VoltxChannel::Piano),
            "talex" => Some(VoltxChannel::Talex),
            "spidx" => Some(VoltxChannel::Spidx),
            "wazaa" => Some(VoltxChannel::Wazaa),
            _ => None,
        }
    }
}

/// Bridge VOLTX pour N243
/// Permet l'enregistrement de canaux et l'envoi/réception de messages
pub struct VoltxBridge {
    subscribers: HashMap<String, Vec<Box<dyn Fn(String) + Send + Sync>>>,
    connected: bool,
}

impl VoltxBridge {
    pub fn new() -> Self {
        Self {
            subscribers: HashMap::new(),
            connected: false,
        }
    }

    /// Connecte le bridge
    pub fn connect(&mut self) -> Result<(), String> {
        self.connected = true;
        Ok(())
    }

    /// Enregistre un canal VOLTX
    pub fn register_channel<F>(&mut self, channel: VoltxChannel, handler: F) -> Result<(), String>
    where
        F: Fn(String) + Send + Sync + 'static,
    {
        if !self.connected {
            return Err("Bridge not connected".to_string());
        }
        self.subscribers
            .entry(channel.as_str().to_string())
            .or_default()
            .push(Box::new(handler));
        Ok(())
    }

    /// Envoie un message sur un canal VOLTX
    pub fn send(&self, channel: VoltxChannel, payload: &str) -> Result<(), String> {
        if !self.connected {
            return Err("Bridge not connected".to_string());
        }
        let handlers = match self.subscribers.get(channel.as_str()) {
            Some(h) => h,
            None => return Ok(()),
        };
        for handler in handlers {
            handler(payload.to_string());
        }
        Ok(())
    }

    /// Déconnecte le bridge
    pub fn disconnect(&mut self) {
        self.connected = false;
        self.subscribers.clear();
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct VoltxMessage {
    pub channel: String,
    pub payload: String,
    pub timestamp: String,
    pub source: String,
}

impl VoltxMessage {
    pub fn new(channel: VoltxChannel, payload: impl Into<String>, source: impl Into<String>) -> Self {
        Self {
            channel: channel.as_str().to_string(),
            payload: payload.into(),
            timestamp: chrono::Utc::now().to_rfc3339(),
            source: source.into(),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_voltx_channel_as_str() {
        assert_eq!(VoltxChannel::Plix.as_str(), "plix");
        assert_eq!(VoltxChannel::Piano.as_str(), "piano");
        assert_eq!(VoltxChannel::Talex.as_str(), "talex");
        assert_eq!(VoltxChannel::Spidx.as_str(), "spidx");
        assert_eq!(VoltxChannel::Wazaa.as_str(), "wazaa");
    }

    #[test]
    fn test_voltx_channel_from_str() {
        assert_eq!(VoltxChannel::from_str("plix"), Some(VoltxChannel::Plix));
        assert_eq!(VoltxChannel::from_str("unknown"), None);
    }

    #[test]
    fn test_voltx_bridge_connect() {
        let mut bridge = VoltxBridge::new();
        assert!(bridge.connect().is_ok());
        assert!(bridge.connected);
    }

    #[test]
    fn test_voltx_bridge_register_and_send() {
        let mut bridge = VoltxBridge::new();
        bridge.connect().unwrap();

        let received = std::sync::Arc::new(std::sync::Mutex::new(None));
        let r = received.clone();
        bridge.register_channel(VoltxChannel::Plix, move |payload| {
            *r.lock().unwrap() = Some(payload);
        }).unwrap();

        bridge.send(VoltxChannel::Plix, "hello").unwrap();
        assert_eq!(received.lock().unwrap().as_deref(), Some("hello"));
    }

    #[test]
    fn test_voltx_message_new() {
        let msg = VoltxMessage::new(VoltxChannel::Talex, "payload", "source");
        assert_eq!(msg.channel, "talex");
        assert_eq!(msg.payload, "payload");
        assert_eq!(msg.source, "source");
    }
}
