import requests
from bs4 import BeautifulSoup

TARGET_SOURCES = {
    "Angelina County": "https://www.angelinacounty.net/jobs",
    "Nacogdoches County": "https://www.co.nacogdoches.tx.us/jobs",
    "Cherokee County": "https://www.co.cherokee.tx.us/jobs",
    "Jasper County": "https://www.co.jasper.tx.us/page/jasper.Jobs",
    "Newton County": "https://www.co.newton.tx.us/page/newton.Jobs",
    "Hardin County": "https://www.co.hardin.tx.us/page/hardin.Jobs",
    "Tyler County": "https://www.co.tyler.tx.us/page/tyler.Jobs",
    "Sabine County": "https://www.co.sabine.tx.us/page/sabine.Jobs",
    "San Augustine County": "https://www.co.san-augustine.tx.us/page/sanaugustine.Jobs",
}

WORKIN_TEXAS_CITIES = [
    "Lufkin", "Nacogdoches", "Jacksonville", "Woodville", "Jasper",
    "Newton", "Livingston", "Marshall", "Paris", "Texarkana"
]

IT_KEYWORDS = ["IT", "Information Technology", "Network", "Systems", "Helpdesk", "Technology", "Infrastructure"]

def fetch_page(url):
    try:
        r = requests.get(url, timeout=10)
        return r.text
    except:
        return None

def scrape_county_jobs():
    results = []
    for county, url in TARGET_SOURCES.items():
        html = fetch_page(url)
        if not html:
            continue
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(" ", strip=True)
        for kw in IT_KEYWORDS:
            if kw.lower() in text.lower():
                results.append({
                    "source": county,
                    "title": f"Possible IT posting containing '{kw}'",
                    "url": url
                })
    return results

def scrape_workintexas():
    results = []
    for city in WORKIN_TEXAS_CITIES:
        url = f"https://www.workintexas.com/vosnet/Default.aspx?city={city}"
        html = fetch_page(url)
        if not html:
            continue
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(" ", strip=True)
        for kw in IT_KEYWORDS:
            if kw.lower() in text.lower():
                results.append({
                    "source": f"WorkInTexas ({city})",
                    "title": f"IT-related posting containing '{kw}'",
                    "url": url
                })
    return results

def run_scraper():
    data = []
    data.extend(scrape_county_jobs())
    data.extend(scrape_workintexas())
    return data

if __name__ == "__main__":
    import json
    print(json.dumps(run_scraper(), indent=2))

