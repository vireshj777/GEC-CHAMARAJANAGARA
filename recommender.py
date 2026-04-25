def generate_recommendations(important, junk, harmful):
    suggestions = []

    # Files not used for long time
    old_files = [f for f in junk if f.get("days_unused", 0) > 90]
    if old_files:
        suggestions.append(f"🧹 Delete {len(old_files)} files not used for 90+ days")

    # Important files
    if important:
        suggestions.append(f"💾 Backup {len(important)} important files")

    # Harmful files
    if harmful:
        suggestions.append(f"⚠️ {len(harmful)} suspicious files detected")

    if not suggestions:
        suggestions.append("✅ System looks clean and optimized")

    return suggestions