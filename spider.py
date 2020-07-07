import requests
import re
from urllib.parse import urljoin

target_links = []


def extract_links_from(url):
    response = requests.get(url)
    _href_links = re.findall('(?:href=")(.*?)"', response.content.decode())
    return _href_links


def crawl(target_url):
    target_domain = target_url.strip("'").strip('"').split("//")[-1]
    target_url = "http://" + target_domain
    href_links = extract_links_from(target_url)

    for link in href_links:
        # Make Links from relative paths
        link = urljoin(target_url, link)

        # Remove contents after '#' form the link
        # Example: http://example.com/page#aContentOfPage
        if "#" in link:
            link = link.split("#")[0]

        # If the link is from same domain
        # And if the link is not already appended in target_links
        if target_domain in link and link not in target_links:
            target_links.append(link)
            print(link)
            try:
                crawl(link)
                pass
            except UnicodeDecodeError:
                pass


if __name__ == '__main__':
    target_url = input("Target URL > ")
    try:
        crawl(target_url)
    except requests.exceptions.ConnectionError:
        print("[-] Connection Error!")
