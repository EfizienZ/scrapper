import requests
from bs4 import BeautifulSoup
import re


requests.packages.urllib3.disable_warnings()
base_url = 'https://www.gestorias.es'


# Function to scrape data from a page
def scrape_page(route):
    # Loop to scrape all pages
    hrefs = []
    while True:
        current_url = base_url + route
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        a_tags = soup.find_all('a', class_='uk-button uk-button-primary uk-float-left uk-margin-bottom uk-hidden-small')
        for tag in a_tags:
            if 'href' in tag.attrs:
                hrefs.append(tag['href'])
        next_page_link = soup.find('a', title='next page')
        if next_page_link:
            route = next_page_link['href']
        else:
            # If there's no "Next Page" link, break the loop
            break
    return hrefs


# Function to scrape web pages for itemprop="sameAs" elements
def scrape_web_pages(hrefs):
    web_pages = []
    phones = []
    names = []
    for href in hrefs:
        response = requests.get(base_url + href)
        soup = BeautifulSoup(response.text, 'html.parser')
        same_as_element = soup.find(itemprop="sameAs")
        telephone = soup.find(itemprop="telephone")
        name = soup.find(itemprop="name")
        if same_as_element:
            web_pages.append('https://' + same_as_element.text)
        else:
            print("No web for " + href)
            web_pages.append("NO_WEB")
        if telephone:
            phones.append(telephone.text)
        else:
            print("No phone for " + href)
            phones.append("NO_PHONE")
        if name:
            if 'content' in name.attrs.keys():
                names.append(name.attrs['content'])
            else:
                names.append(name.text)
        else:
            print("No name for " + href)
            phones.append("NO_NAME")
    return web_pages, phones, names


# Function to find emails on web pages
def find_emails(web_pages):
    emails = []
    for page in web_pages:
        if page == 'NO_WEB':
            emails.append("NO_MAIL")
        else:
            try:
                response = requests.get(page, verify=False)
                soup = BeautifulSoup(response.text, 'html.parser')
                email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                email_elements = soup.find(['p', 'a', 'span', 'div'], string=re.compile(email_pattern))
                cleaned_emails = email_elements.text.strip()
                emails.append(cleaned_emails)
            except requests.exceptions.SSLError:
                print('SSL error in ' + page)
                emails.append("SSL ERROR")
            except requests.exceptions.ConnectionError:
                print('Connection error in ' + page)
                emails.append("CONN ERROR")
            except AttributeError:
                print('Mail not found in ' + page)
                emails.append("NOT_FOUND")
            except requests.exceptions.InvalidURL:
                print('Invalid url in ' + page)
                emails.append("Invalid URL")
            except requests.exceptions.ContentDecodingError:
                print('Content decoding error in ' + page)
                emails.append("Content decoding error")

    return emails
