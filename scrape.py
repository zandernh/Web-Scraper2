import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
job_elements = results.find_all('div', 'card-content')

python_jobs = results.find_all('h2', string=lambda text: "python" in text.lower())

python_jobs_element = [h2_element.parent.parent.parent for h2_element in python_jobs]

def scrape_func():

    print("Total Python Jobs:", len(python_jobs))

    for job_element in python_jobs_element:
        job_title = job_element.find('h2', 'title').text.strip()
        company = job_element.find('h3', 'company').text.strip()
        location = job_element.find('p', 'location').text.strip()

        print(
            f"""
            Title: {job_title}
            Company: {company}
            Location: {location}
            """
        )

    return 0

if __name__ == "__main__":
    scrape_func()