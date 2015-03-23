#!/usr/bin/python
import os
import sys
import ws_settings as settings
import server_ctl

def restore_from_backup(zip_file, env):
    # create temporary folder
    # unzip into folder
    # psql run db restore command
    temp_folder = "/tmp/ws_restore"

    os.system("sudo rm -rf %s" % temp_folder)
    os.system("mkdir -p %s" % temp_folder)
    os.system("chmod -R a+rw %s" % temp_folder)

    further_path = "tmp/ws_backup"

    os.system("unzip %s -d %s" % (zip_file, temp_folder))
    restore_folder = os.path.join(temp_folder, further_path)
    dump_file = os.path.join(restore_folder, "backup.sql")

    if env != "dev":
        server_ctl.main("stop")
    else:
        os.system("sudo pkill -9 -f 'python manage.py runserver'")

    os.system("sudo su postgres -c 'dropdb %s'" % settings.PG_DB)
    os.system("sudo su postgres -c 'psql -q -f %s'" % dump_file)

    os.system("sudo cp -r %s/%s %s" % (restore_folder, "media", settings.WS_ROOT_FOLDER))

    if env != "dev":
        os.system("sudo chown -R %s:%s %s/media" % (settings.WS_USER, settings.WS_GROUP, settings.WS_ROOT_FOLDER))
        os.system("sudo chmod -R g+w %s/media" % settings.WS_ROOT_FOLDER)
        server_ctl.main("start")
    else:
        os.system("sudo chown -R motley:motley %s/media" % settings.WS_ROOT_FOLDER)

    print "Restored postgres db and media folder"


def main():
    if len(sys.argv) < 2:
        print "Usage: python restore.py backup_zip_file"
        exit(1)
    backup_zip = sys.argv[1]

    ENV = ""
    if len(sys.argv) == 3:
        ENV = sys.argv[2]

    restore_from_backup(backup_zip, ENV)

if __name__ == "__main__":
    main()