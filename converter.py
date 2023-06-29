import subprocess
from pathlib import Path
import os

path = Path(os.path.dirname(os.path.realpath(__file__))+"\ImageMagick")
if not path.exists():
    path = Path(input("Enter ImageMagick-folder location: "))

inp = input("Enter input folder (empty for currPath\in): ")
if inp == "":
    inp=Path(os.path.dirname(path)+"\in")

out = input("Enter output folder (empty for currPath\out): ")
if out == "":
    out=Path(os.path.dirname(path)+"\out")

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
    subprocess.run(f"{path}\convert.exe in\{file.name} {resize} {out}\{name + ('.'+str(counter) if (counter > 0) and (not orig) else '')}.{ext}", shell=True)
    counter+=1