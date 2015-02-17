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

def main():
    # verify that user wants to uninstall
    confirm("Are you sure you want to uninstall the webcms server? : ", True)


    # shut down processes
    # TODO - supervisor, nginx shutdowns

    # delete folders
    WS_ROOT_FOLDER = settings.WS_ROOT_FOLDER
    WS_USER = settings.WS_USER
    WS_GROUP = settings.WS_GROUP
    PG_USER = settings.PG_USER
    PG_DB = settings.PG_DB
    REPO_NAME = settings.REPO_NAME

    if WS_ROOT_FOLDER in (None, '', '/'):
        print "Cannot delete web root folder"
        print "Invalid path : '%s'" % WS_ROOT_FOLDER
        exit(1)

    if not WS_ROOT_FOLDER.startswith('/'):
        print "Cannot delete web root folder"
        print "Invalid path : '%s'" % WS_ROOT_FOLDER
        exit(1)

    for site in settings.SITE_DETAILS:
        site_name = "webcms_%s" % site['name']
        os.system('sudo supervisorctl stop %s' % site_name)
        os.system('sudo rm -f /etc/supervisor/conf.d/%s.conf' % site_name)

        os.system('sudo rm -f /etc/nginx/sites-enabled/%s' % site_name)

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
        os.system('sudo rm -rf %s/conf' % (WS_ROOT_FOLDER))
        os.system('sudo rm -rf %s/venvs' % (WS_ROOT_FOLDER))
        os.system('sudo rm -rf %s/%s' % (WS_ROOT_FOLDER, REPO_NAME))
        os.system('sudo chown -R `whoami`:`whoami` %s' % WS_ROOT_FOLDER)
        os.system('sudo userdel %s' % WS_USER)
        os.system('sudo groupdel %s' % WS_GROUP)



# remove user and group

if __name__ == "__main__":
    main()

