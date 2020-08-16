import glob
import os

for file in glob.glob("**/*.pyx", recursive=True):
    print(file)
    cmd = f"2to3 -w {file}"
    os.system(cmd)
