import os
import sys
import json
import shutil
from subprocess import PIPE, run


x = os.getcwd()

args = sys.argv
source, target = args[1:]

source_path = os.path.join(x, source)
target_path = os.path.join(x, target)

for filename in os.listdir(source_path):
    if filename.endswith('.py'):
        file_path   = os.path.join(source_path, filename)
        target_file = os.path.join(target_path, filename)
        shutil.move(file_path, target_path)
        print(f"Successfully moved {filename} from {source} to {target}!")




