// N243 — WAZAA Bridge Integration Test
// Validation du bridge WAZAA et de ses topics.
// IntentHash: 0xN243_WAZAA_BRIDGE_20260915

use n243::bridge::wazaa_bridge::{WazaaBridge, WazaaMessage};

#[test]
fn test_wazaa_bridge_connect_disconnect() {
    let mut bridge = WazaaBridge::new();
    assert!(!bridge.is_connected());
    assert!(bridge.connect().is_ok());
    assert!(bridge.is_connected());
    bridge.disconnect();
    assert!(!bridge.is_connected());
}

#[test]
fn test_wazaa_bridge_publish_requires_connect() {
    let bridge = WazaaBridge::new();
    assert!(bridge.publish("n243.gates", "payload").is_err());
}

#[test]
fn test_wazaa_bridge_subscribe_and_publish() {
    let mut bridge = WazaaBridge::new();
    bridge.connect().unwrap();

    let received = std::sync::Arc::new(std::sync::Mutex::new(None));
    let r = received.clone();
    bridge.subscribe("n243.gates", move |payload| {
        *r.lock().unwrap() = Some(payload);
    }).unwrap();

    bridge.publish("n243.gates", "hello-wazaa").unwrap();
    assert_eq!(received.lock().unwrap().as_deref(), Some("hello-wazaa"));
}

#[test]
fn test_wazaa_message_new() {
    let msg = WazaaMessage::new("n243.runners", "payload", "N243");
    assert_eq!(msg.topic, "n243.runners");
    assert_eq!(msg.payload, "payload");
    assert_eq!(msg.source, "N243");
    assert!(!msg.timestamp.is_empty());
}
