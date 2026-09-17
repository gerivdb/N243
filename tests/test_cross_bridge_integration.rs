// N243 — Cross-Bridge Integration Test (WAZAA + VOLTX)
// Validation de l'intégration opérationnelle des bridges.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use n243::bridge::{wazaa_bridge::WazaaBridge, voltx_bridge::{VoltxBridge, VoltxChannel}};

#[test]
fn test_wazaa_and_voltx_bridges_are_independent() {
    let mut wazaa = WazaaBridge::new();
    let mut voltx = VoltxBridge::new();

    assert!(wazaa.connect().is_ok());
    assert!(voltx.connect().is_ok());
    assert!(wazaa.is_connected());
    assert!(voltx.is_connected());
}

#[test]
fn test_wazaa_publish_and_voltx_send_share_nothing() {
    let mut wazaa = WazaaBridge::new();
    let mut voltx = VoltxBridge::new();
    wazaa.connect().unwrap();
    voltx.connect().unwrap();

    let wazaa_received = std::sync::Arc::new(std::sync::Mutex::new(None));
    let voltx_received = std::sync::Arc::new(std::sync::Mutex::new(None));

    let w1 = wazaa_received.clone();
    wazaa.subscribe("ops.status", move |payload| {
        *w1.lock().unwrap() = Some(payload);
    }).unwrap();

    let v1 = voltx_received.clone();
    voltx.register_channel(VoltxChannel::Piano, move |payload| {
        *v1.lock().unwrap() = Some(payload);
    }).unwrap();

    wazaa.publish("ops.status", "wazaa-ok").unwrap();
    voltx.send(VoltxChannel::Piano, "voltx-ok").unwrap();

    assert_eq!(wazaa_received.lock().unwrap().as_deref(), Some("wazaa-ok"));
    assert_eq!(voltx_received.lock().unwrap().as_deref(), Some("voltx-ok"));
}
