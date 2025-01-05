## Solution

View the Page Source for every page that can be traversed.

Nothing in `index.html` and `contact.html`

Within `about.html`, there is a string found within the `notify_true` attribute in one of the `<section>` tags.

Decoding that from base64 reveals the flag.

**Flag: `picoCTF{web_succ3ssfully_d3c0ded_283e62fe}`**

## Code

```python
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
```
