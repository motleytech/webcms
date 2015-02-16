#!/usr/bin/python

# create /webserver folder
# remove /webserver/conf and /webserver/webcms folders
# copy conf and webcms folder
# run prod install script... pass dev=true

import os
from bootstrap_dev import run_command
import ws_settings as settings
from ws_utils import print_fatal, print_info

def main():
    # assert that we are not in the settings.ws_root_folder
    currpath = os.path.abspath(__file__)
    if currpath.startswith("%s/" % settings.WS_ROOT_FOLDER):
        print_fatal("Cannot run this script from within %s folder." % settings.WS_ROOT_FOLDER)
        print_info("Change your server root folder in settings (WS_ROOT_FOLDER), or run this script from your dev folder")
        exit(1)

    dev_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

    # create directories
    run_command("sudo mkdir -p %s" % settings.WS_ROOT_FOLDER)
    run_command("sudo chown -R `whoami`:`whoami` %s" % settings.WS_ROOT_FOLDER)

    # remove old conf and repo, keep everything else
    run_command("rm -rf %s/%s" % (settings.WS_ROOT_FOLDER, "conf"))
    run_command("rm -rf %s/%s" % (settings.WS_ROOT_FOLDER, settings.REPO_NAME))

    run_command("cp -R %s/%s %s/%s" % (dev_folder, "conf", settings.WS_ROOT_FOLDER, "conf"))
    run_command("cp -R %s/%s %s/%s" % (dev_folder, settings.REPO_NAME, settings.WS_ROOT_FOLDER, settings.REPO_NAME))

    # run the main install script with dev=true
    run_command("cd %s/%s/%s; python install.py dev=true" % (settings.WS_ROOT_FOLDER, settings.REPO_NAME, "setup"))


if __name__ == "__main__":
    main()

