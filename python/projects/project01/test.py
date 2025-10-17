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




github_token = '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'
github_token_classic = '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'

ssh-token = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEquf8LvPYsQtAsOx3M0RNsMMP1NAgEr2i6hwtPNlJEL omegathunder564@gmail.com"