#!/usr/bin/python
"""
Bootstrapping script for webcms personal webserver.
"""

import os
import time
import subprocess
import bootstrap_prod as bp

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

bp.INSTALL_TYPE = "dev"

bp.WS_ROOT_FOLDER = THIS_DIR
bp.REPO_URL = "git@github.com:motleytech/webcms.git"

bp.REPO_PATH = os.path.join(bp.WS_ROOT_FOLDER, bp.REPO_NAME)
bp.CONF_PATH = os.path.join(bp.WS_ROOT_FOLDER, "conf")

bp.BLOG_REPO_URL = "git@github.com:motleytech/djangocms-blog.git"
bp.BLOG_REPO_PATH = os.path.join(bp.REPO_PATH, "djcms/djangocms-blog")

bp.PYBOOK_REPO = "git@github.com:motleytech/pybook.git"
bp.PYBOOK_REPO_PATH = os.path.join(bp.REPO_PATH, "djcms/pybook")

if __name__ == "__main__":
    bp.main()

