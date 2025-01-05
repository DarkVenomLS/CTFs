import requests
import urllib3
import sys


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http':'http:127.0.0.1:8080',
    'https': 'http:127.0.0.1:8080'
}

def deleteUser(url):
    pass

def main():
    if len(sys.argv) != 2:
        print("(*) Usage: \nSyntax: python file.py <url>\nEg: python file,py www.example.com")
        sys.exit(-1)
    
    url = sys.argv[1]
    deleteUser(url)


if __name__ == '__main__':
    main()