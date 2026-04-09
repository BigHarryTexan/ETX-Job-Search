import json
from scraper import run_scraper

def generate_markdown_report(data, output_file="weekly_report.md"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Weekly ETX Job Watch Report\n\n")

        if not data:
            f.write("No IT-related postings found this week.\n")
            return

        for item in data:
            f.write(f"## {item['title']}\n")
            f.write(f"- **Source:** {item['source']}\n")
            f.write(f"- **URL:** {item['url']}\n\n")

if __name__ == "__main__":
    results = run_scraper()
    generate_markdown_report(results)
    print("Report generated: weekly_report.md")
