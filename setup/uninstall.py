#!/bin/python
import os
import subprocess
from pprint import pprint as pp
import ws_settings as settings

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def confirm(msg, abort=False):
    inp = raw_input(msg)

    if inp != "yes":
        if abort:
            print "Aborting."
            exit(1)
        print "Skipping step...\n\n"
        return False

    print "Continuing...\n\n"
    return True

def main():
    # verify that user wants to uninstall
    confirm("Are you sure you want to uninstall the webcms server? : ", True)

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

    for name, domain, forw, nump in settings.SITE_DETAILS:
        sup_fname = "supervisor_%s.conf" % name

        os.system("sudo supervisorctl stop webcms_%s" % name)
        # delete supervisor config
        os.system("sudo rm /etc/supervisor/conf.d/%s" % (sup_fname))

        nginx_fname = "nginx_%s" % name
        # delete nginx config
        os.system("sudo rm /etc/nginx/sites-enabled/%s" % (nginx_fname))
        os.system("sudo rm /etc/nginx/sites-available/%s" % (nginx_fname))

    os.system('sudo service nginx restart')

    # remove database
    if confirm("\n\nDelete the DATABASE ? :"):
        os.system("sudo python %s/backup.py --no-process-restart" % THIS_DIR)
        if PG_DB is not None:
            # sudo su postgres -c "dropdb webcmsdb"
            os.system('sudo su postgres -c "dropdb %s"' % PG_DB )

    # delete folder
    if confirm("About to delete git repository. Continue? : "):
        os.system('sudo rm -rf %s/conf' % (WS_ROOT_FOLDER))
        os.system('sudo rm -rf %s/%s' % (WS_ROOT_FOLDER, REPO_NAME))
        os.system('sudo chown -R `whoami`:`whoami` %s' % WS_ROOT_FOLDER)

    os.system("sudo su -c 'crontab -l | grep -v \"webcms\" | crontab -'")

if __name__ == "__main__":
    main()

