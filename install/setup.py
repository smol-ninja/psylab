import subprocess
import os
from os.path import dirname, realpath, pardir, join, sep

################################################
# Adding psylab to PYTHONPATH in .bashrc, .zshrc
################################################

HOME_PATH = os.getenv('HOME')
BASHRC = HOME_PATH + sep + '.bashrc'
ZSHRC = HOME_PATH + sep + '.zshrc'
PSYLAB_DIR = join(dirname(realpath(__file__)), pardir)

export_command = "export PYTHONPATH=$PYTHONPATH:%s" % (PSYLAB_DIR, )

isExport = False

if os.path.exists(BASHRC):
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

if os.path.exists(ZSHRC):
    with open(ZSHRC, mode='r') as zshrc_file:
        lines = zshrc_file.readlines()
        for line in lines:
            if 'psylab' in line:
                isExport = True
    zshrc_file.close()

    if not isExport:
        # .zshrc will be created if it does not exist
        e = "echo %s >> %s" % (export_command, ZSHRC, )
        subprocess.call(e, shell=True)

###################################################
# Installing dependencies
###################################################

DEPENDENCIES = PSYLAB_DIR + sep + 'requirements.txt'
e = "sudo pip install -r %s" % (DEPENDENCIES, )
subprocess.call(e, shell=True)
