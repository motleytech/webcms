import os

# make this FALSE in production
DJANGO_DEBUG = True

# make sure this path is absolute. Do not give relative paths here.
WS_ROOT_FOLDER   = "/webserver"
WS_PIP_CACHE    = "/webserver_pip_cache"
WS_BACKUP_FOLDER = "/webserver_backup"

WS_USER  = "webuser"
WS_GROUP = "webapps"
PG_USER  = "webdbuser"
PG_DB    = "webcmsdb"

# set this to a valid disqus shortname, if you want to use disqus comments
DISQUS_SHORTNAME = ""

#########################################
#
# DO NOT CHANGE ANYTHING BELOW THIS
#
#########################################

VENV_ROOT_FOLDER = os.path.join(WS_ROOT_FOLDER, 'venvs')
VENV_NAME = "cms_venv"
VENV_FOLDER = os.path.join(VENV_ROOT_FOLDER, VENV_NAME)


REPO_URL  = "https://github.com/motleytech/webcms.git"
REPO_NAME = REPO_URL.split("/")[-1].split(".")[0]

# installing
# wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/bootstrap.sh
# bash ./bootstrap.sh

# uninstalling
# wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/uninstall.py
