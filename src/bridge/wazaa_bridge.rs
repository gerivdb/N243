// N243 — WAZAA Bridge
// IntentHash: 0xN243_WAZAA_BRIDGE_20260915

use serde::{Deserialize, Serialize};
use std::collections::HashMap;

/// WAZAA Bridge pour N243
/// Permet la publication et la souscription sur le bus WAZAA
pub struct WazaaBridge {
    subscribers: HashMap<String, Vec<Box<dyn Fn(String) + Send + Sync>>>,
    connected: bool,
}

impl WazaaBridge {
    pub fn new() -> Self {
        Self {
            subscribers: HashMap::new(),
            connected: false,
        }
    }

    /// Connecte le bridge au bus WAZAA
    pub fn connect(&mut self) -> Result<(), String> {
        // Placeholder: connexion au bus WAZAA
        self.connected = true;
        Ok(())
    }

    /// Publie un message sur un topic WAZAA
    pub fn publish(&self, _topic: &str, _payload: &str) -> Result<(), String> {
        if !self.connected {
            return Err("Bridge not connected".to_string());
        }
        // Placeholder: publication sur le bus
        Ok(())
    }

    /// Souscrit à un topic WAZAA
    pub fn subscribe<F>(&mut self, topic: &str, handler: F) -> Result<(), String>
    where
        F: Fn(String) + Send + Sync + 'static,
    {
        if !self.connected {
            return Err("Bridge not connected".to_string());
        }
        self.subscribers
            .entry(topic.to_string())
            .or_default()
            .push(Box::new(handler));
        Ok(())
    }

    /// Déconnecte le bridge
    pub fn disconnect(&mut self) {
        self.connected = false;
        self.subscribers.clear();
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct WazaaMessage {
    pub topic: String,
    pub payload: String,
    pub timestamp: String,
    pub source: String,
}

impl WazaaMessage {
    pub fn new(topic: impl Into<String>, payload: impl Into<String>, source: impl Into<String>) -> Self {
        Self {
            topic: topic.into(),
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
    fn test_wazaa_bridge_connect() {
        let mut bridge = WazaaBridge::new();
        assert!(bridge.connect().is_ok());
        assert!(bridge.connected);
    }

    #[test]
    fn test_wazaa_bridge_publish_not_connected() {
        let bridge = WazaaBridge::new();
        assert!(bridge.publish("test", "payload").is_err());
    }

    #[test]
    fn test_wazaa_bridge_subscribe() {
        let mut bridge = WazaaBridge::new();
        bridge.connect().unwrap();
        assert!(bridge.subscribe("test", |_| {}).is_ok());
    }

    #[test]
    fn test_wazaa_message_new() {
        let msg = WazaaMessage::new("topic", "payload", "source");
        assert_eq!(msg.topic, "topic");
        assert_eq!(msg.payload, "payload");
        assert_eq!(msg.source, "source");
    }
}
