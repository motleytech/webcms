#!/bin/python
import os
import subprocess
from pprint import pprint as pp
import ws_settings as settings

def confirm(msg, abort=False):
    inp = raw_input(msg)

    if inp != "yes":
        if abort:
            print "Aborting."
            exit(1)
        print "Skipping step...\n\n"
        retun False

    print "Continuing...\n\n"
    return True

# verify that user wants to uninstall
confirm("Are you sure you want to uninstall the webcms server? : ", True)


ENV_FILE = '~/envs/env_webcms.sh'


# import environment
command = ['bash', '-c', 'source %s && env' % ENV_FILE]
proc = subprocess.Popen(command, stdout = subprocess.PIPE)

for line in proc.stdout:
    (key, _, value) = line.partition("=")
    os.environ[key] = value.strip()

proc.communicate()


# shut down processes
# TODO - supervisor, nginx shutdowns


# delete folders
WEB_ROOT_FOLDER = os.environ.get('WEB_ROOT_FOLDER', None)
WEB_USER = os.environ.get('WEB_USER', None)
WEB_GROUP = os.environ.get('WEB_GROUP', None)
PG_USER = os.environ.get('PG_USER', None)
PG_DB = os.environ.get('PG_DB', None)
REPO_NAME = os.environ.get('REPO_NAME', None)
BACKUP_FOLDER = 

if WEB_ROOT_FOLDER is None:
    print "Failed to import environment."
    print "Ensure that %s exists." % ENV_FILE

if WEB_ROOT_FOLDER in (None, '', '/'):
    print "Cannot delete web root folder"
    print "Invalid path : '%s'" % WEB_ROOT_FOLDER
    exit(1)

if not WEB_ROOT_FOLDER.startswith('/'):
    print "Cannot delete web root folder"
    print "Invalid path : '%s'" % WEB_ROOT_FOLDER
    exit(1)

os.system('sudo supervisorctl stop webcms_motleytech')
os.system('sudo supervisorctl stop webcms_nagrajan')
os.system('sudo rm -f /etc/supervisor/conf.d/webcms_motleytech.conf')
os.system('sudo rm -f /etc/supervisor/conf.d/webcms_nagrajan.conf')

os.system('sudo rm -f /etc/nginx/sites-enabled/webcms')
os.system('sudo service nginx restart')

# remove database and db user
if confirm("\n\nDelete the DATABASE and DB user ? :"):
    os.system("sudo su postgres -c 'pg_dumpall > %s/%s'" % (settings.WS_ROOT_FOLDER, "backup.sql"))
    if PG_DB is not None:
        os.system('sudo su postgres -c "dropdb %s"' % PG_DB )

    if PG_USER is not None:
        os.system('sudo -u postgres psql -c "DROP ROLE %s;"' % PG_USER )

# delete folder
if confirm("About to delete git repository and virtualenv folders. Continue? : "):
    os.system('sudo rm -rf %s/envs' % (WEB_ROOT_FOLDER))
    os.system('sudo rm -rf %s/venvs' % (WEB_ROOT_FOLDER))
    os.system('sudo rm -rf %s/%s' % (WEB_ROOT_FOLDER, REPO_NAME))
    os.system('sudo chown -R `whoami`:`whoami` %s' % WEB_ROOT_FOLDER)
    os.system('sudo userdel %s' % WEB_USER)
    os.system('sudo groupdel %s' % WEB_GROUP)



# remove user and group



