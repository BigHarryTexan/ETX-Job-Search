def generate_report(new_items):
    if not new_items:
        return "# Weekly Job Report\n\nNo new IT-related postings this cycle."

    lines = ["# Weekly Job Report\n", "## New IT-Related Postings\n"]
    for item in new_items:
        lines.append(f"- **{item['source']}** — {item['title']}\n  {item['url']}\n")
    return "\n".join(lines)

def save_report(text):
    with open("weekly_report.md", "w") as f:
        f.write(text)

