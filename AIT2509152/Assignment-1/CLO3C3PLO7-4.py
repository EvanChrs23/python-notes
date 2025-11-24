from sys import argv
from os.path import exists
import time

script, source_file, destination_file = argv

if not exists(source_file):
    print("Source file doesn't exist")
    exit()
if not exists(destination_file):
    print("Destination file doesn't exist")
    exit()

print(f"Opening source file...")
time.sleep(2)
data = open(source_file).read()
destination = open(destination_file,'w')
print("Rewriting destination file...")
time.sleep(2)
destination.write(data)

print("Done")
destination.close()