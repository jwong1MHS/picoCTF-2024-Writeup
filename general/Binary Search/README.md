Looking at `guessing_game.sh` in `home/ctf-player/drop-in`, we can see that the guessing game has many indents.

We can fix this by running `sed -i '1d;s/^ \{9\}//;$d' guessing_game.sh`.

This will remove the first line, 9 spaces before each line, and then remove the last line. The `-i` will modify the file in-place.
