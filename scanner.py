import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class Scanner:
    def __init__(self, url, ignore_links):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.links_to_ignore = ignore_links

    def extract_links_from(self, url):
        response = self.session.get(url)
        _href_links = re.findall('(?:href=")(.*?)"', response.content.decode())
        return _href_links

    def crawl(self, url=None):
        if url is None:
            url = self.target_url
        target_domain = url.strip("'").strip('"').split("//")[-1]
        target_url = "http://" + target_domain
        href_links = self.extract_links_from(target_url)

        for link in href_links:
            # Make Links from relative paths
            link = urljoin(target_url, link)

            # Remove contents after '#' form the link
            # Example: http://example.com/page#aContentOfPage
            if "#" in link:
                link = link.split("#")[0]

            # If the link is from same domain
            # And if the link is not already appended in target_links
            if target_domain in link and link not in self.target_links and link not in self.links_to_ignore:
                self.target_links.append(link)
                print(link)
                try:
                    self.crawl(link)
                except UnicodeDecodeError:
                    pass

    def extract_forms(self, url):
        resp = self.session.get(url)
        parsed_html = BeautifulSoup(resp.content, features="html.parser")
        _forms = parsed_html.findAll('form')

        return _forms

    def submit_form(self, form, value, url, token=None):
        action = form.get('action')
        post_url = urljoin(url, action)

        print('\n\n', post_url, '\n\n')

        method = form.get('method')
        post_data = {}

        inputs_list = form.findAll('input')
        for input in inputs_list:
            input_name = input.get('name')
            input_type = input.get('type')
            input_value = input.get('value')

            if input_type == 'text':
                input_value = value

            post_data[input_name] = input_value
        if method == 'post':
            return requests.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)

    def run_scanner(self):
        for link in self.target_links:
            forms = self.extract_forms(link)
            for form in forms:
                print("[+] Testing form in: " + link)

                # fuzzing get parameters (e.g. index.php?id=1)
                if "=" in link:
                    print("[+] Testing " + link)

    def test_xss_in_form(self, form, url):
        xss_test_script = "<sCript>alert('Vulnerable')</scriPt>"
        response = self.submit_form(form, xss_test_script, url)
        if xss_test_script in response.content.decode():
            return True


if __name__ == '__main__':
    target_url = 'http://ec2-35-174-211-112.compute-1.amazonaws.com/DVWA/login.php'
    s1 = Scanner(target_url, [])
    s1.extract_forms(target_url)
    s1.crawl()
    print(s1.extract_forms(target_url))
