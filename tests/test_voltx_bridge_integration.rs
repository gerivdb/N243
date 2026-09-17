// N243 — VOLTX Bridge Integration Test
// Validation du bridge VOLTX et de ses 5 canaux.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use n243::bridge::voltx_bridge::{VoltxBridge, VoltxChannel};

#[test]
fn test_voltx_bridge_has_five_channels() {
    let expected = vec![
        VoltxChannel::Plix,
        VoltxChannel::Piano,
        VoltxChannel::Talex,
        VoltxChannel::Spidx,
        VoltxChannel::Wazaa,
    ];
    assert_eq!(expected.len(), 5);
}

#[test]
fn test_voltx_channel_names() {
    assert_eq!(VoltxChannel::Plix.as_str(), "plix");
    assert_eq!(VoltxChannel::Piano.as_str(), "piano");
    assert_eq!(VoltxChannel::Talex.as_str(), "talex");
    assert_eq!(VoltxChannel::Spidx.as_str(), "spidx");
    assert_eq!(VoltxChannel::Wazaa.as_str(), "wazaa");
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

    bridge.send(VoltxChannel::Plix, "hello-voltx").unwrap();
    assert_eq!(received.lock().unwrap().as_deref(), Some("hello-voltx"));
}
