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
