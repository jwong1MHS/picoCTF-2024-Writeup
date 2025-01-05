import subprocess

process = subprocess.Popen(['./home/ctf-player/drop-in/guessing_game.sh'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE, text=True)

print(process.stdout.readline().strip())
print(process.stdout.readline().strip())

upper_bound = 1000
lower_bound = 1
while True:
    n = (upper_bound + lower_bound) // 2
    print(str(n))
    process.stdin.write(str(n)+'\n')
    process.stdin.flush()
    output = process.stdout.readline().strip()
    print(output)
    if 'Lower' in output:
        upper_bound = n
    elif 'Higher' in output:
        lower_bound = n
    else:
        break
