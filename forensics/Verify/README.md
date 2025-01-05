We are given the task to connect via `ssh -p 55650 ctf-player@rhea.picoctf.net` with the password `84b12bae`.

If we run `ls -l` we get the following:

```bash
ctf-player@pico-chall$ ls -l
total 20
-rw-r--r-- 1 root       root         65 Mar 12  2024 checksum.txt
-rwxr-xr-x 1 root       root        856 Mar 12  2024 decrypt.sh
drwxr-xr-x 2 ctf-player ctf-player 8192 Mar 12  2024 files
```

We can see that `files` is a directory, and it seems we have to match the checksum from `checksum.txt` to one of the checksums from the `files` directory.

We can accomplish this by running `sha256sum` and then piping it to grep.

```bash
ctf-player@pico-chall$ sha256sum files/* | grep $(cat checksum.txt)
3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4  files/e018b574
```

We found the correct file, and with that let's decrypt the file.

```bash
ctf-player@pico-chall$ ./decrypt.sh files/e018b574 
picoCTF{trust_but_verify_e018b574}
```

Flag: `picoCTF{trust_but_verify_e018b574}`
