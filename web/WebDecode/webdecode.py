import base64
import requests
from bs4 import BeautifulSoup

port = 64384
url='http://titan.picoctf.net:'+str(port)+'/about.html'

# Do an HTTP Request
page = requests.get(url)
# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')
# Find the section tag with class='about'
output = soup.find('section', {'class': 'about'})
# Grab the value of the 'notify_true' attribute in the tag
encoded_flag = output.attrs['notify_true']
# Decode from base64
flag = base64.b64decode(encoded_flag).decode()
print(flag)

# Flag: picoCTF{web_succ3ssfully_d3c0ded_283e62fe}
