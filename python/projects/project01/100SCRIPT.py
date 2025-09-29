import os
import sys
import json
import shutil
from subprocess import PIPE, run

def get_apps(sourceDir, targetDir):
    
    for filename in os.listdir(sourceDir):
        if filename.endswith('.py'):
            file_path   = os.path.join(sourceDir, filename)
            shutil.move(file_path, targetDir)
            print(f"Successfully moved {filename} from {source} to {target}!")

def main(source, target):
    currentDir = os.getcwd()
    sourceDir = os.path.join(currentDir, source)
    targetDIr = os.path.join(currentDir, target)
    return sourceDir, targetDIr

if __name__ == "__main__":
    args = sys.argv
    
    if len(args) != 3:
        raise Exception("Please pass two arguments, the source and destination")
    
    source, target = args[1:]
    print(args)
    
    sourceDir, targetDir = main(source, target)
    
    get_apps(sourceDir, targetDir)
    
    
    
