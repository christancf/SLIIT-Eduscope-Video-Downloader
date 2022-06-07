#!/usr/bin/env python

import subprocess
import struct
import sys
import json

# On Windows, the default I/O mode is O_TEXT. Set this to O_BINARY
# to avoid unwanted modifications of the input/output streams.
if sys.platform == "win32":
    import os
    import msvcrt
    msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)


def read_thread_func(qu):
    while 1:
        # Read the message length (first 4 bytes).
        text_length_bytes = sys.stdin.read(4)

        if len(text_length_bytes) == 0:
            if qu:
                qu.put(None)
            sys.exit(0)

        # Unpack message length as 4 byte integer.
        text_length = struct.unpack('i', bytes(text_length_bytes, "utf8"))[0]

        # Read the text (JSON object) of the message.
        text = sys.stdin.read(text_length)
        loadedJson = json.loads(text)

        subprocess.run(["start", "./main.exe", loadedJson["link"]], shell=True)


if __name__ == '__main__':
    read_thread_func(None)
