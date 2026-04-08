# from requests import get

# websites = {
#     "google.com",
#     "airbnb.com",
#     "https://twitter.com",
#     "facebook.com",
#     "https://tiktok.com",
# }

# results = {}

# for website in websites:
#     if not website.startswith("https://"):
#         website = f"https://{website}"
#     response = get(website)
#     if response.status_code == 200:
#         results[website] = "OK"
#     else:
#         results[website] = "FAILED"

# print(results)

import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/remote-full-time-jobs"

all_jobs = []

# def scrape_page(url):
response = requests.get(url)

# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section", class_ = "jobs").find_all("li")[:-1]

for job in jobs:
    title = job.find("span", class_ = "new-listing__header__title__text").text
    company = job.find("p", class_ = "new-listing__company-name").text
  

    temp = job.find_all("p", class_ = "new-listing__categories__category")

    region = temp[-1].text

    position = [tag for tag in temp
                if tag.get("class") == ["new-listing__categories__category"]][0].text

    url = job.find("a", class_ = "listing-link--unlocked")["href"]
    job_data = {
        "title": title,
        "company": company,
        "position": position,
        "region": region,
        "url": f"http://weworkremotely.com{url}",
    }
    all_jobs.append(job_data)

# response = requests.get(url)

# soup = BeautifulSoup(response.content, "html.parser")

# jobs = soup.find("section", class_="jobs").find_all("li")[:-1]

print(all_jobs)
