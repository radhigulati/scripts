import os, glob

os.chdir("/Users/radhigulati")
for file in glob.glob("*.ipynb"):
    print(file)
