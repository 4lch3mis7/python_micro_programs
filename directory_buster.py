import requests


def request(url):
    # Remove http:// or https:// from URL
    if r"//" in url:
        url = url.strip('"').strip("'").split("//")[-1]

    # Send GET request
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


def enumerate_directories(wordlist_file):
    with open(wordlist_file, 'r') as wordlist:
        for word in wordlist:
            word = word.strip()
            test_url = f"{target_url}/{word}"
            response = request(test_url)
            if response:
                print("[+] Discovered Directories --> " + test_url)


target_url = "owasp-juice-shop.herokuapp.com"
wordlist_file = "/usr/share/wordlists/dirb/common.txt"


if __name__ == '__main__':
    try:
        target_url = input("Target URL > ")
        enumerate_directories(input("Wordlist File > ").strip('"').strip("'"))
    except Exception as msg:
        print("[-]" + str(msg))

