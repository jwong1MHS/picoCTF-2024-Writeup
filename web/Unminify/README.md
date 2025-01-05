## Solution

Even though the HTML code has went under [Minification](https://en.wikipedia.org/wiki/Minification_(programming)), the source code can still be prettified using an in-browser tool such as Inspect Element.

We can see that the flag is found as the name of a class within a `<p>` tag.

**Flag: `picoCTF{pr3tty_c0d3_743d0f9b}`**

## Code

```python
import re
import requests
from bs4 import BeautifulSoup

port = 52441
url='http://titan.picoctf.net:'+str(port)

# Do an HTTP Request
page = requests.get(url)
# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')
# soup.prettify()
# Search for pattern where it starts with p (^), ends with right curly bracket ($), and has one or more character (.+)
pattern = r'^picoCTF{.+}$'
output = soup.find('p', {'class': re.compile(pattern)})
# # Grab the value of the 'class' attribute in the tag
flag, = output.attrs['class']
print(flag)
```
