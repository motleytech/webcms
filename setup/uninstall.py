#!/bin/python
import os
import subprocess
from pprint import pprint as pp

def confirm(msg):
    inp = raw_input(msg)

    if inp != "yes":
        print "Aborting."
        exit(1)

    print "Continuing...\n\n"
    return True

# verify that user wants to uninstall
confirm("Are you sure you want to uninstall everything? : ")


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

# finally delete folder
confirm("About to delete '%s' folder. Continue? : " % WEB_ROOT_FOLDER)
os.system('sudo rm -rf %s' % (WEB_ROOT_FOLDER))


# remove user and group
os.system('sudo userdel %s' % WEB_USER)
os.system('sudo groupdel %s' % WEB_GROUP)


# remove database and db user
confirm("About to delete DATABASE. Continue? : ")

if PG_DB is not None:
    os.system('sudo su postgres -c "dropdb %s"' % PG_DB )

if PG_USER is not None:
    os.system('sudo -u postgres psql -q -c "DROP ROLE %s;"' % PG_USER )

os.system('sudo rm -f /etc/supervisor/conf.d/webcms.conf')
os.system('sudo supervisorctl reread')
os.system('sudo supervisorctl update')
