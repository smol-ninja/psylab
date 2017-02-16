import subprocess
import os
from os.path import dirname, realpath, pardir, join, sep

###################################################
# Adding psylab to PYTHONPATH in .bashrc
###################################################

HOME_PATH = os.getenv('HOME')
BASHRC = HOME_PATH + sep + '.bashrc'
PSYLAB_DIR = join(dirname(realpath(__file__)), pardir)

export_command = "export PYTHONPATH=$PYTHONPATH:%s" % (PSYLAB_DIR, )

isExport = False
with open(BASHRC, mode='r') as bashrc_file:
    lines = bashrc_file.readlines()
    for line in lines:
        if 'psylab' in line:
            isExport = True
bashrc_file.close()

if not isExport:
    # .bashrc will be created if it does not exist
    e = "echo %s >> %s" % (export_command, BASHRC, )
    subprocess.call(e, shell=True)

###################################################
# Installing dependencies
###################################################

DEPENDENCIES = PSYLAB_DIR + sep + 'requirements.txt'
e = "sudo pip install -r %s" % (DEPENDENCIES, )
subprocess.call(e, shell=True)
