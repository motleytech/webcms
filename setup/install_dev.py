#!/usr/bin/python

# create /webserver folder
# remove /webserver/conf and /webserver/webcms folders
# copy conf and webcms folder
# run prod install script... pass dev=true

import os
from bootstrap_prod import run_command
import ws_settings as settings
from ws_utils import print_fatal, print_info

def main():
    dev_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

    # run the main install script with dev=true
    run_command("cd %s/%s/%s; python install.py debug developer_mode" % (settings.WS_ROOT_FOLDER, settings.REPO_NAME, "setup"))


if __name__ == "__main__":
    main()
