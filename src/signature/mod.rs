pub struct Signature {
    pub links: Vec<SignatureLink>,
}

pub struct SignatureLink {
    pub from: &'static str,
    pub to: &'static str,
    pub link_type: SignatureLinkType,
}

pub enum SignatureLinkType {
    SensorielleToSemantique,
    SyscallToGrammar,
    ProceduraleToCognitive,
    TernaireToEpisodique,
}

impl Signature {
    pub fn new() -> Self {
        Signature {
            links: Vec::new(),
        }
    }

    pub fn add_link(&mut self, from: &'static str, to: &'static str, link_type: SignatureLinkType) {
        self.links.push(SignatureLink {
            from,
            to,
            link_type,
        });
    }

    pub fn route(&self, task: &str) -> Option<&'static str> {
        for link in &self.links {
            if self.matches(task, link) {
                return Some(link.to);
            }
        }
        None
    }

    fn matches(&self, task: &str, link: &SignatureLink) -> bool {
        // Simplified matching logic for now
        match link.link_type {
            SignatureLinkType::SensorielleToSemantique => task.contains("sensorielle"),
            SignatureLinkType::SyscallToGrammar => task.contains("grammar"),
            SignatureLinkType::ProceduraleToCognitive => task.contains("cognitive"),
            SignatureLinkType::TernaireToEpisodique => task.contains("episodique"),
        }
    }
}
