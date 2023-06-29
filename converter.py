from pathlib import Path
import subprocess
import os

orig = False
path = Path(os.path.dirname(os.path.realpath(__file__)))
magic_path = Path(path, "ImageMagick")
while not magic_path.exists():
    magic_path = Path(input("Enter ImageMagick-folder location: "))

inp = Path(x) if not (x := input("Enter input folder (empty for currPath\in): ")) == "" else Path(path, "in")
out = Path(x) if not (x := input("Enter output folder (empty for currPath\out): ")) == "" else Path(path, "out")
ext = x if not (x := input("Enter file extension (empty for png): ")) == "" else "png"
name if not (name := input("Rename? (empty for no): ")) == "" else (orig := True)
resize if (resize := input("Resize? (empty for no, leave x in between): ")) == "" else (resize := "-resize " + resize)

counter = 0
for file in inp.glob("*"):
    if orig: name = file.stem
    subprocess.run(f"{magic_path}\convert.exe {inp}\{file.name} {resize} {out}\{name + ('.'+str(counter) if (counter > 0) and (not orig) else '')}.{ext}", shell=True)
    counter+=1