import sys
import base64


if len(sys.argv) != 2:
    print("USAGE: PyGetBase85 <TARGET_FILE_PATH>")
    sys.exit(1)


data = ""
with open(sys.argv[1], "rb") as f:
    data = f.read()
with open(sys.argv[1]+"_Base85.txt", "w") as out:
    out.write(base64.a85encode(data).decode("ascii"))

