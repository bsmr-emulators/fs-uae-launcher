#!/usr/bin/env python
from __future__ import print_function

import os
import shutil
import tempfile
import subprocess

dirs = [
    "fs_uae_launcher",
    "fs_uae_workspace",
    "fsui",
    "fsbc",
    "fsgs",
    "game_center",
]
files = []
extensions = [".py"]

temp = tempfile.NamedTemporaryFile(delete=False)
for dir in dirs:
    for dir_path, dir_names, file_names in os.walk(dir):
        for file in file_names:
            name, ext = os.path.splitext(file)
            if ext not in extensions:
                continue
            path = os.path.join(dir_path, file)
            files.append(path)

with temp:
    for path in sorted(files):
        temp.write(path)
        temp.write("\n")

args = ["xgettext",
        "--output-dir=po",
        "--files-from=" + temp.name,
        "--keyword=_",
        "--keyword=N_",
        "--package-name=fs-uae-launcher",
        "--msgid-bugs-address=fs-uae@fengestad.no",
        "--copyright-holder=Frode Solheim",
        "--add-comments=#",
        "--no-location",
        "--sort-output",
        "--from-code=ISO-8859-1",
        ]

print(args)
p = subprocess.Popen(args)
p.wait()
shutil.move("po/messages.po", "po/messages.pot")

#for file in os.listdir("po"):
#    if file.endswith(".po"):
#        path = os.path.join("po", file)
#        print(path)
#        p = subprocess.Popen(["msgmerge",
#                              "--no-fuzzy-matching",
#                              "--sort-output",
#                              "--update",
#                              path,
#                              "po/messages.pot"])
#        p.wait()

os.system("find share -name fs-uae.mo -delete")
#os.system("make -C .. po-dist")
os.system("make mo")
