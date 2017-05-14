# glob is the module that finds all the pathnames matches a specified pattern
# os module provides portable way of using OS dependent functionality
import os, glob

# os.chidr changes to directory given a path
os.chdir("/Users/radhigulati")
for file in glob.glob("*.ipynb"):
# glob.glob returns a possibly-empty list of path names that match the specific
# pathname
    print(file)
