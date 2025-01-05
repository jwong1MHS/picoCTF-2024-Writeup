Looking at the attachment `flag2of2-final.pdf`, it seems normal, but we have to run `file` on it to verify what the file type is.

```bash
└─$ file flag2of2-final.pdf 
flag2of2-final.pdf: PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced
```

Just to verify, let's look at the file signature (magic bytes) of the file:

```bash
└─$ xxd flag2of2-final.pdf | head -1
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```

The file signature matches the first 8 bytes of a standard PNG file. The only thing that was modified was the file extension.

After changing the file extension and opening the image, we obtain the first part of the flag: `picoCTF{f1u3n7_`

Changing the file back to a `.pdf`, we obtain the second part of the flag: `1n_pn9_&_pdf_2a6a1ea8}`

Flag: `picoCTF{f1u3n7_1n_pn9_&_pdf_2a6a1ea8}`
