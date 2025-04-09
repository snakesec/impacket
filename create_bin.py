import os
save_dir = "andraxbin"
progpath = "/opt/ANDRAX/PYENV/python3"

str_file = """#!/bin/bash

source {progdir}/bin/activate

{progdir}/bin/python3 {progdir}/bin/{progname} "$@"
"""

os.system("rm -rf "+save_dir)
os.system("mkdir "+save_dir)

if os.path.exists("examples"):

    exfiles = os.listdir("examples")
    
    for exfile in exfiles:
        with open(save_dir+"/"+exfile, 'w') as out:
            content = str_file.format(progdir = progpath, progname = exfile)
            out.write(content)
else:
    print("examples dir not found")
