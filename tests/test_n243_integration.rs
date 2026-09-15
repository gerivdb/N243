// N243 — Integration Tests
// IntentHash: 0xN243_INTEGRATION_TESTS_20260915

use n243::bridge::voltx_bridge::{VoltxBridge, VoltxChannel};
use n243::bridge::wazaa_bridge::{WazaaBridge, WazaaMessage};

#[test]
fn test_wazaa_bridge_integration() {
    let mut bridge = WazaaBridge::new();
    assert!(bridge.connect().is_ok());
    assert!(bridge.is_connected());

    // Test publish
    assert!(bridge.publish("test.topic", "payload").is_ok());

    // Test subscribe
    let received = std::sync::Arc::new(std::sync::Mutex::new(None));
    let r = received.clone();
    bridge.subscribe("test.topic", move |msg| {
        *r.lock().unwrap() = Some(msg);
    }).unwrap();

    bridge.publish("test.topic", "hello").unwrap();
    assert_eq!(received.lock().unwrap().as_deref(), Some("hello"));

    bridge.disconnect();
}

#[test]
fn test_voltx_bridge_integration() {
    let mut bridge = VoltxBridge::new();
    assert!(bridge.connect().is_ok());

    // Test register_channel + send sur chaque canal
    let channels = [
        VoltxChannel::Plix,
        VoltxChannel::Piano,
        VoltxChannel::Talex,
        VoltxChannel::Spidx,
        VoltxChannel::Wazaa,
    ];

    for channel in channels {
        let received = std::sync::Arc::new(std::sync::Mutex::new(None));
        let r = received.clone();
        bridge.register_channel(channel, move |msg| {
            *r.lock().unwrap() = Some(msg);
        }).unwrap();

        let payload = format!("test_{}", channel.as_str());
        bridge.send(channel, &payload).unwrap();
        assert_eq!(received.lock().unwrap().as_deref(), Some(payload.as_str()));
    }

    bridge.disconnect();
}

#[test]
fn test_voltx_channel_enum() {
    // Test as_str
    assert_eq!(VoltxChannel::Plix.as_str(), "plix");
    assert_eq!(VoltxChannel::Piano.as_str(), "piano");
    assert_eq!(VoltxChannel::Talex.as_str(), "talex");
    assert_eq!(VoltxChannel::Spidx.as_str(), "spidx");
    assert_eq!(VoltxChannel::Wazaa.as_str(), "wazaa");

    // Test from_str
    assert_eq!(VoltxChannel::from_str("plix"), Some(VoltxChannel::Plix));
    assert_eq!(VoltxChannel::from_str("unknown"), None);
}

#[test]
fn test_wazaa_message_integration() {
    let msg = WazaaMessage::new("test.topic", "payload", "test_source");
    assert_eq!(msg.topic, "test.topic");
    assert_eq!(msg.payload, "payload");
    assert_eq!(msg.source, "test_source");
    assert!(!msg.timestamp.is_empty());
}

#[test]
fn test_voltx_message_integration() {
    let msg = n243::bridge::voltx_bridge::VoltxMessage::new(
        VoltxChannel::Talex,
        "payload",
        "test_source",
    );
    assert_eq!(msg.channel, "talex");
    assert_eq!(msg.payload, "payload");
    assert_eq!(msg.source, "test_source");
    assert!(!msg.timestamp.is_empty());
}
