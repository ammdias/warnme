#!/usr/bin/env bash

if ! [ -x "$(command -v python3)" ]; then
    echo '"python3" command not found.' >&2
    echo 'Please ensure that Python version 3 is installed and try again.' >&2
    exit 1
fi

chmod +x warnme.py
chmod +x gwarnme.py
chmod +x wmnotify.py

DIR="`dirname \"$0\"`"
DIR="`( cd \"$DIR\" && pwd )`"
PROG="`basename \"$DIR\"`"
BIN="$HOME/.local/bin"
LIB="$HOME/.local/lib"

mkdir -p "$BIN" "$LIB"
cp -r "$DIR" "$LIB"

ln -sf "$LIB/$PROG/warnme.py" "$BIN/warnme"
ln -sf "$LIB/$PROG/gwarnme.py" "$BIN/gwarnme"
