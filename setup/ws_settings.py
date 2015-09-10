import os

###############################################################
#
# CONFIGURABLE VALUES FOLLOW
#
###############################################################

# site will be created for 'domain' field.
# with forwarding, 'myblog.com' or '*.myblog.com' will lead to 'www.myblog.com'
SITE_DETAILS = [
    # name(unique), domain, forwarding, num_django_processes
    ('motleytechnet', 'www.motleytech.net', '.motleytech.net', 2),
    ('nagarajancom', 'www.nagarajan.com', '.nagarajan.com', 1),

    # we can also serve multiple domains using the same server (different processes).
    #('mypersonalweb', 'www.mypersonalweb.com', '.mypersonalweb.com', 1),
]

WS_ROOT_FOLDER   = "/webserver"
WS_PIP_CACHE     = "/webserver_pip_cache"
WS_BACKUP_FOLDER = "/webserver_backup"

WS_USER  = "webuser"
WS_GROUP = "webapps"
PG_USER  = "webdbuser"
PG_DB    = "webcmsdb"

# set this to a valid disqus shortname, if you want to use disqus comments
DISQUS_SHORTNAME = "motleytech"


###############################################################
#
# NOT CONFIGURABLE - DO NOT MODIFY ANYTHING BELOW THIS LINE
#
###############################################################

from ws_utils import import_env_variables

ENV_WEBCMS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../conf/env_webcms.sh"))
import_env_variables(ENV_WEBCMS_PATH)

# this should be FALSE in production
DJANGO_DEBUG = (os.environ["DJANGO_DEBUG"] == "True")

WS_ROOT_FOLDER   = WS_ROOT_FOLDER if os.environ['PRODUCTION_ENV'] == "True" else \
    os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../"))

VENV_ROOT_FOLDER = os.path.join(WS_ROOT_FOLDER, 'venvs')
VENV_NAME = "cms_venv"
VENV_FOLDER = os.path.join(VENV_ROOT_FOLDER, VENV_NAME)

REPO_URL  = "git@github.com:motleytech/webcms.git"
REPO_NAME = REPO_URL.split("/")[-1].split(".")[0]

DESKTOP_INSTALL = (os.system("dpkg -l ubuntu-desktop > /dev/null ") == 0)

# installing
# wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/bootstrap.sh
# bash ./bootstrap.sh

# uninstalling
# wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/uninstall.py
