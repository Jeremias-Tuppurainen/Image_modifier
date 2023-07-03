from pathlib import Path
import subprocess
import os

path = Path(os.path.dirname(os.path.realpath(__file__)))                                                                # Gets the current location of this file
magic_path = Path(path, "ImageMagick")                                                                                  # Checks if the default path for ImageMagick is valid
while not magic_path.exists():                                                                                          # if not asks the user to give the location, until a valid one is given
    magic_path = Path(input("Enter ImageMagick-folder location: "))

inp = Path(x) if not (x := input("Enter input folder (empty for currPath\in): ")) == "" else Path(path, "in")           # if user input is empty put default path for input folder
out = Path(x) if not (x := input("Enter output folder (empty for currPath\out): ")) == "" else Path(path, "out")        # same but for output folder
ext = input("Enter file extension (empty for no): ")                                                                    # change file extension, if user input is empty keep original extension
name = input("Rename? (empty for no): ")                                                                                # if input was empty keeps the original name, else stores the new given name
resize if (resize := input("Resize? (empty for no, leave x in between): ")) == "" else (resize := "-resize " + resize)  # if input was empty keeps the original size, else stores the new given size

out.mkdir(parents=True, exist_ok=True)                                                                                  # checks if the path is correct, if not it makes the correct new folders
counter = 0                                                                                                             # counter for image names, when renaming
for file in inp.glob("*"):                                                                                              # goes through all the files in the input folder
    outname = (name if name else file.stem) + ('.'+str(counter) if (counter > 0) and name else '')
    outext = '.'+ext if ext else Path(file).suffix
    subprocess.run(f"{magic_path}\convert.exe {inp}\{file.name} {resize} {out}\{outname}{outext}", shell=True)  
    counter+=1                                                                                                          # row above runs the convert.exe inside ImageMagick folder and gives it the necessary information.