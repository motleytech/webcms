#!/usr/bin/python
"""
Bootstrapping script for webcms personal webserver.
"""

import os
import time
import subprocess

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALL_TYPE = "prod"

WS_ROOT_FOLDER = "/webserver"
REPO_URL = "https://github.com/motleytech/webcms.git"
REPO_NAME = "webcms"
REPO_PATH = os.path.join(WS_ROOT_FOLDER, REPO_NAME)
CONF_PATH = os.path.join(WS_ROOT_FOLDER, "conf")
BRANCH_NAME = "motleytechnet"

BLOG_REPO_URL = "https://github.com/motleytech/djangocms-blog.git"
BLOG_REPO_PATH = os.path.join(REPO_PATH, "djcms/djangocms-blog")
BLOG_UPSTREAM = "https://github.com/nephila/djangocms-blog.git"

PYBOOK_REPO = "https://github.com/motleytech/pybook.git"
PYBOOK_REPO_PATH = os.path.join(REPO_PATH, "djcms/pybook")

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

def run_command(cmd, ignore_error=False, quiet=False):
    """run a shell command"""
    if not quiet:
        print "\nRunning cmd : {}{}{}".format(bcolors.OKBLUE, cmd, bcolors.ENDC)
    rv = os.system(cmd)
    if rv != 0:
        if ignore_error is False:
            if not quiet:
                print "{}Error while running {}. Stopping{}".format(bcolors.FAIL, cmd, bcolors.ENDC)
            exit(1)
        if not quiet:
            print "{}Error while running command. {}\n{}".format(bcolors.WARNING, cmd, bcolors.ENDC)
        return False
    if not quiet:
        print "{}Success{}".format(bcolors.OKGREEN, bcolors.ENDC)
    return True

def get_command_output(cmd):
    output = []
    command = ['bash', '-c', cmd]
    proc = subprocess.Popen(command, stdout = subprocess.PIPE)

    for line in proc.stdout:
        output.append(line)

    proc.communicate()
    return output

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


def main():
    if run_command("dpkg -s aptitude", ignore_error=True) is False:
        run_command("sudo apt-get -y install aptitude")

    now = time.time()
    try:
        update_time = int(get_command_output("stat -c %Y /var/lib/apt/periodic/update-success-stamp")[0].strip())
    except:
        update_time = 0

    if ((now - update_time) > 3600*24):
        run_command("sudo aptitude -y update")
        run_command("sudo aptitude -y upgrade")

    if run_command("dpkg -s git", ignore_error=True) is False:
        run_command("sudo aptitude -y install git")

    if INSTALL_TYPE == 'prod':
        run_command("sudo mkdir -p %s" % CONF_PATH, ignore_error=True)
        run_command("sudo chown -R `whoami`:`whoami` %s" % WS_ROOT_FOLDER)
    else:
        run_command("mkdir -p %s " % CONF_PATH, True)

    print "Cloning git repo..."
    repo_exists = run_command("[ -d %s ]" % REPO_PATH, True, False)

    if not repo_exists or \
            confirm("\nGit repo already exists. Overwrite (yes, no)? "):
        if repo_exists:
            run_command("rm -rf %s" % REPO_PATH)
        run_command("cd %s; git clone %s" % (WS_ROOT_FOLDER, REPO_URL))
        run_command("cd %s; git checkout %s" % (REPO_PATH, BRANCH_NAME))

    blog_repo_exists = run_command("[ -d %s ]" % BLOG_REPO_PATH, True, True)

    if not blog_repo_exists or \
            confirm("\nCMS Blog repo already exists. Overwrite (yes, no)? "):
        if blog_repo_exists:
            run_command("rm -rf %s" % BLOG_REPO_PATH)
        run_command("cd %s; git clone %s;" % (os.path.dirname(BLOG_REPO_PATH), BLOG_REPO_URL))
        run_command("cd %s; git checkout develop" % BLOG_REPO_PATH)
        run_command("cd %s; git remote add upstream %s" % (BLOG_REPO_PATH, BLOG_UPSTREAM))

    pybook_repo_exists = run_command("[ -d %s ]" % PYBOOK_REPO_PATH, True, True)

    if not pybook_repo_exists or \
            confirm("\nCMS Blog repo already exists. Overwrite (yes, no)? "):
        if pybook_repo_exists:
            run_command("rm -rf %s" % PYBOOK_REPO_PATH)
        run_command("cd %s; git clone %s;" % (os.path.dirname(PYBOOK_REPO_PATH), PYBOOK_REPO))

    envcms_exists = run_command("[ -e %s/env_webcms.sh ]" % CONF_PATH, True, False)

    if INSTALL_TYPE == "prod":
        ENV_PATH = "%s/config/sample_env_webcms_prod.sh" % REPO_PATH
        INSTALL_SCRIPT = "%s/setup/install.py" % REPO_PATH
    else:
        ENV_PATH = "%s/config/sample_env_webcms_dev.sh" % REPO_PATH
        INSTALL_SCRIPT = "%s/setup/install_dev.py" % REPO_PATH

    if envcms_exists:
        if confirm("env_webcms.sh already exists. Overwrite (yes, no)? "):
            run_command("cp %s %s/env_webcms.sh" % (ENV_PATH, CONF_PATH))
    else:
        run_command("cp %s %s/env_webcms.sh" % (ENV_PATH, CONF_PATH))

    print """\

    NOTE
    ====
    Repository cloned into %s.

    Please edit %s in %s folder and change the passowords/secrets.
    These values should be kept scrictly secret in a production environment.

    You can additionally modify %s to configure installation settings.

    To clear the database and start fresh, you can type
    'sudo su postgres -c "dropdb webcmsdb"'

    To start the installation, run command

    python %s

    """ % (REPO_PATH, "env_webcms.sh",
           CONF_PATH, "%s/setup/ws_settings.py" % REPO_PATH,
           INSTALL_SCRIPT)

if __name__ == "__main__":
    main()
