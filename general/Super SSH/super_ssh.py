from pwn import *

username = 'ctf-player'
host = 'titan.picoctf.net'
port = 50564
password = '84b12bae'

ssh_client = ssh(user=username, host=host, port=port, password=password)
remote_shell = ssh_client.shell()
output = remote_shell.recv()
print(output.decode())
