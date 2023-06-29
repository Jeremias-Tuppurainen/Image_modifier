import subprocess
from pathlib import Path
import os

path = Path(os.path.dirname(os.path.realpath(__file__))+"\ImageMagick")
while not path.exists():
    path = Path(input("Enter ImageMagick-folder location: "))

inp = input("Enter input folder (empty for currPath\in): ")
if inp == "":
    inp=os.path.dirname(path)+"\in"
inp = Path(inp)

out = input("Enter output folder (empty for currPath\out): ")
if out == "":
    out=os.path.dirname(path)+"\out"
out = Path(out)

ext = input("Enter file extension (empty for png): ")
if ext == "":
    ext="png"

name = input("Rename? (empty for no): ")
if name=="":
    orig = True
else:
    orig = False

resize = input("Resize? (empty for no, leave x in between): ")
if resize != "":
    resize = "-resize " + resize

counter = 0
for file in inp.glob("*"):
    if orig:
        name = file.stem
    subprocess.run(f"{path}\convert.exe {inp}\{file.name} {resize} {out}\{name + ('.'+str(counter) if (counter > 0) and (not orig) else '')}.{ext}", shell=True)
    counter+=1