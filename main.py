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

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

all_jobs = []

def scrape_page(url):
    response = requests.get(url)

    # print(response.content)

    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find("section", class_="jobs").find_all("li")[:-1]

    for job in jobs:
        title = job.find("h3", class_="new-listing__header__title").text
        company, position, region = job.find_all("span", class_="company")
        url = job.find("div", class_="tooltip").next_sibling["href"]
        job_data = {
            "title": title,
            "company": company,
            "position":position,
            "region": region,
            "url": f"http://weworkremotedly.com{url}",
        }
        all_jobs.append(job_data)



# print(jobs)
