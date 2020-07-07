import requests


def request(url):
    if r"//" in url:
        url = url.strip('"').strip("'").split("//")[-1]
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "google.com"


with open("/usr/share/dnsrecon/subdomains-top1mil.txt", 'r') as wordlist_file:
    for word in wordlist_file:
        word = word.strip()
        test_url = f"{word}.{target_url}"
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> " + test_url)


