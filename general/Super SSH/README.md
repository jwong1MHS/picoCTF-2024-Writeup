## Solution 

To connect to a machine via ssh, run `ssh <user>@<ip> -p <port>`.

After running `ssh -p 52799 ctf-player@titan.picoctf.net`, we are greeted with the following message:

> Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_07a987ac}

**Flag: `picoCTF{s3cur3_c0nn3ct10n_07a987ac}`**

## Code

```python
from pwn import *

username = 'ctf-player'
host = 'titan.picoctf.net'
port = 50564
password = '84b12bae'

ssh_client = ssh(user=username, host=host, port=port, password=password)
remote_shell = ssh_client.shell()
output = remote_shell.recv()
print(output.decode())
```
