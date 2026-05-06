import json
from src.scraper import run_scraper

def generate_html_report(data, output_file="weekly_report.html"):
    # Start HTML
    html = []
    html.append("<h2>Weekly ETX Job Watch Report</h2>")

    if not data:
        html.append("<p>No IT-related postings found this week.</p>")
        final_html = "\n".join(html)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(final_html)
        return final_html

    html.append("<p>Here are the possible IT-related postings found this week:</p>")
    html.append("<ul>")

    for item in data:
        title = item["title"]
        source = item["source"]
        url = item["url"]

        html.append(
            f'<li><strong>{source}</strong> — '
            f'<a href="{url}">{title}</a></li>'
        )

    html.append("</ul>")
    html.append("<p>This report was generated automatically by your ETX Job Watch pipeline.</p>")

    final_html = "\n".join(html)

    # Write to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    return final_html


if __name__ == "__main__":
    results = run_scraper()
    html_body = generate_html_report(results)
    print("Report generated: weekly_report.html")
