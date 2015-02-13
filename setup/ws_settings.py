DJANGO_DEBUG = True

WS_ROOT_FOLDER   = "/webserver"
WS_PIP_FOLDER    = "/webserver_pip_cache"
WS_BACKUP_FOLDER = "/webserver_backup"

WS_USER  = "webuser"
WS_GROUP = "webapps"
PG_USER  = "webdbuser"
PG_DB    = "webcmsdb"

VENV_NAME = "cms_venv"
REPO_URL  = "https://github.com/motleytech/webcms.git"
REPO_NAME = REPO_URL.split("/")[-1].split(".")[0]

# installing
# wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/bootstrap.sh
# bash ./bootstrap.sh

# uninstalling
# wget https://raw.githubusercontent.com/motleytech/webcms/master/setup/uninstall.py

# export WEB_ROOT_FOLDER="/webserver"
# export VENV_NAME="cms_venv"
# export PIP_CACHE_FOLDER='/pip-cache'
# export PG_USER_PW="c82qIrm7qGxzUrdaXoasLKJASFas1hTjsEG5F7w73LIiprFJPQJhq3Ljb"
# export PG_ADMIN_PW="mysqladmin6383"
