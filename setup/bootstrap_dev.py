#!/usr/bin/python
"""
Bootstrapping script for webcms personal webserver.
"""

import os
import time
import subprocess
from bootstrap_prod import *

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALL_TYPE = "dev"

WS_ROOT_FOLDER = THIS_DIR
REPO_URL = "git@github.com:motleytech/webcms.git"

REPO_PATH = os.path.join(WS_ROOT_FOLDER, REPO_NAME)
CONF_PATH = os.path.join(WS_ROOT_FOLDER, "conf")

BLOG_REPO_URL = "git@github.com:motleytech/djangocms-blog.git"
BLOG_REPO_PATH = os.path.join(REPO_PATH, "djcms/djangocms-blog")

PYBOOK_REPO = "git@github.com:motleytech/pybook.git"
PYBOOK_REPO_PATH = os.path.join(REPO_PATH, "djcms/pybook")

if __name__ == "__main__":
    main()
