// N243 — PRD Frontmatter Validation Test
// Valide les frontmatters YAML des documents PRD/MOC du repo.
// IntentHash: 0xN243_META_ORCHESTRATOR_20260801

use std::fs;
use std::path::Path;

fn read_frontmatter(path: &Path) -> Option<String> {
    let content = fs::read_to_string(path).ok()?;
    if !content.starts_with("---\n") {
        return None;
    }
    let end = content.find("\n---\n")?;
    Some(content[4..end].to_string())
}

#[test]
fn test_prd_files_have_valid_frontmatter() {
    let prd_dir = Path::new("PRD");
    assert!(prd_dir.exists(), "PRD directory should exist");

    let mut prd_files = Vec::new();
    if let Ok(entries) = fs::read_dir(prd_dir) {
        for entry in entries.flatten() {
            let path = entry.path();
            if path.extension().map(|e| e == "md").unwrap_or(false) {
                prd_files.push(path);
            }
        }
    }

    assert!(!prd_files.is_empty(), "PRD directory should contain markdown files");

    for path in &prd_files {
        let file_name = path.file_name().and_then(|n| n.to_str()).unwrap_or("");
        // Skip index files and non-PRD markdown files
        if file_name.starts_with("PRD-000") || !file_name.starts_with("PRD-") {
            continue;
        }
        let frontmatter = read_frontmatter(path);
        assert!(frontmatter.is_some(), "{} should have frontmatter", path.display());
        
        let fm = frontmatter.unwrap();
        assert!(fm.contains("type: PRD-MOC"), "{} should have type: PRD-MOC", path.display());
        assert!(fm.contains("version:"), "{} should have version", path.display());
        assert!(fm.contains("status:"), "{} should have status", path.display());
        assert!(fm.contains("intent_hash:"), "{} should have intent_hash", path.display());
    }
}
