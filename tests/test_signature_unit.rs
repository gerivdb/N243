// N243 — unit tests for `src/signature/mod.rs`
// Coverage: Signature creation, link registration, route matching.

use n243::signature::{Signature, SignatureLinkType};

#[test]
fn test_signature_new_has_empty_links() {
    let sig = Signature::new();
    assert!(sig.links.is_empty());
}

#[test]
fn test_signature_add_link_and_route_sensorielle() {
    let mut sig = Signature::new();
    sig.add_link(
        "sensorielle",
        "semantique",
        SignatureLinkType::SensorielleToSemantique,
    );

    let route = sig.route("sensorielle input");
    assert_eq!(route, Some("semantique"));
}

#[test]
fn test_signature_route_grammar() {
    let mut sig = Signature::new();
    sig.add_link("syscall", "grammar", SignatureLinkType::SyscallToGrammar);

    let route = sig.route("compile grammar phase");
    assert_eq!(route, Some("grammar"));
}

#[test]
fn test_signature_route_cognitive() {
    let mut sig = Signature::new();
    sig.add_link(
        "procedurale",
        "cognitive",
        SignatureLinkType::ProceduraleToCognitive,
    );

    let route = sig.route("cognitive reasoning");
    assert_eq!(route, Some("cognitive"));
}

#[test]
fn test_signature_route_no_match() {
    let sig = Signature::new();
    let route = sig.route("unknown task");
    assert!(route.is_none());
}
