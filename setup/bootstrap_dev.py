#!/usr/bin/python

"""
Bootstrapping script for webcms personal webserver.
"""


import os

PROJECT_ROOT = "~/ws_project"
REPO_URL = "https://github.com/motleytech/webcms.git"
REPO_NAME = "webcms"
REPO_PATH = '%s/%s' % (PROJECT_ROOT, REPO_NAME)
CONF_PATH = "%s/%s" % (PROJECT_ROOT, "conf")


class bcolors(object):
    """Colors for the terminal"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def run_command(cmd, ignore_error=False):
    """run a shell command"""
    print "\nRunning cmd : %s" % cmd
    rv = os.system(cmd)
    if rv != 0:
        if ignore_error is False:
            print "{}Error while running {}. Stopping{}".format(bcolors.FAIL, cmd, bcolors.ENDC)
            exit(1)
        print "{}Error while running command. {}\n{}".format(bcolors.WARNING, cmd, bcolors.ENDC)
    print "{}Success{}".format(bcolors.OKGREEN, bcolors.ENDC)
    return True


def confirm(msg, abort=False):
    """Get user input to confirm action"""
    inp = raw_input(msg)

    if inp != "yes":
        if abort:
            print "Aborting."
            exit(1)
        print "Skipping step...\n\n"
        return False

    print "Continuing...\n\n"
    return True

#run_command("sudo apt-get -y install aptitude")
#run_command("sudo aptitude -y update")
#run_command("sudo aptitude -y upgrade")
#run_command("sudo aptitude -y install git")

print "Creating project directory (%s) and cloning git repo" % PROJECT_ROOT

run_command("mkdir -p %s " % CONF_PATH)

if not run_command("[ -d %s ]" % REPO_PATH) or \
        confirm("Git repo already exists. Overwrite (yes, no)?"):
    if run_command("[ -d %s ]" % REPO_PATH):
        run_command("rm -rf %s" % REPO_PATH)
    run_command("cd %s; git clone %s" % (PROJECT_ROOT, REPO_URL))


print """\

NOTE
====
Repository cloned into %s.

Please create a file %s in %s to store PG_PW and DJANGO_SECRET.
These values should be kept scrictly secret in a production environment.

You can additionally modify %s to configure installation settings.

To start the installation, run command

python %s

""" % (REPO_PATH, "env_webcms.sh",
       CONF_PATH, "%s/setup/install_settings.py" % REPO_PATH,
       "%s/setup/install.py" % REPO_PATH)


