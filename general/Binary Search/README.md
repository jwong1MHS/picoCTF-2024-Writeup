## Solution

Looking at `guessing_game.sh` in `home/ctf-player/drop-in`, we can see that the guessing game has many indents.

We can fix this by running `sed -i '1d;s/^ \{9\}//;$d' guessing_game.sh`.

This will remove the first line, 9 spaces before each line, and then remove the last line. The `-i` will modify the file in-place.

The idea is to update n based on the middle value of the lower and upper bounds of n.

For starters, we start with 500 because `floor(1 + 1000) = 500`.

The rule is that if we see 'Higher!', we change the lower bound, and if we see 'Lower!', we change the upper bound.

The only time this challenge would fail is if the number is exactly 1000.

> 500 -> 750 -> 875 -> 937 -> 968 -> 984 -> 992 -> 996 -> 998 -> 999

**Flag: `picoCTF{g00d_gu355_2e90d29b}`**

## Code

```python
import paramiko
import time

username = 'ctf-player'
host = 'atlas.picoctf.net'
port = 60455
password = '84b12bae'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(host, port=port, username=username, password=password)
shell = client.invoke_shell()

time.sleep(0.2)
output = shell.recv(100)
print(output.decode())

upper_bound = 1000
lower_bound = 1
while True:
    n = (upper_bound + lower_bound) // 2
    shell.send(str(n)+'\n')
    time.sleep(0.1)
    output = shell.recv(110).decode()
    print(output)
    if 'Lower' in output:
        upper_bound = n
    elif 'Higher' in output:
        lower_bound = n
    else:
        break
```
