#!/usr/bin/python3
import re
import urllib.request, urllib.parse, urllib.error

username = "roll no"
password = "password"
try:
    response = urllib.request.urlopen('http://detectportal.firefox.com/')
    magic = re.search("[0-9a-f]{16}", response.read().decode()).group()
    data = urllib.parse.urlencode({'4Tredir': '', 'magic': magic, 'username': username, 'password': password}).encode(
        'utf-8')
    url = urllib.parse.urlunparse((*urllib.parse.urlparse(response.geturl())[:2], *('',) * 4))
    response_final = urllib.request.urlopen(url, data=data)
    print("Failed" if b"Failed" in response_final.read() else "Success")
except AttributeError:
    print("Already Logged in")
except urllib.error.URLError as e:
    print("Can't connect:", e.args[0])
except Exception as e:
    print(type(e), e)
