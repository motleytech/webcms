#!/usr/bin/python
import os
import time
import ws_settings as settings
import glob
import server_ctl

def get_backup_prefix():
    return time.strftime("%Y_%m_%d__%H_%M_%S")

def get_daily_backup_name():
    return "%s__%s" % (get_backup_prefix(), "Daily.zip")

def get_weekly_backup_name():
    return "%s__%s" % (get_backup_prefix(), "Weekly.zip")

def get_monthly_backup_name():
    return "%s__%s" % (get_backup_prefix(), "Monthly.zip")

def get_yearly_backup_name():
    return "%s__%s" % (get_backup_prefix(), "Yearly.zip")


def create_daily_backup():
    temp_folder = "/tmp/ws_backup"
    out_folder = settings.WS_BACKUP_FOLDER

    os.system("sudo rm -rf %s" % temp_folder)
    os.system("sudo mkdir -p %s" % temp_folder)
    os.system("sudo chmod -R a+rw %s" % temp_folder)

    filename = get_daily_backup_name()
    out_temp_file = os.path.join(temp_folder, "backup.sql")
    out_file = os.path.join(out_folder, filename)

    server_ctl.main("stop")

    os.system("sudo su postgres -c 'pg_dump --create %s > %s'" % (settings.PG_DB, out_temp_file))
    os.system("sudo cp -r %s/%s %s" % (settings.WS_ROOT_FOLDER, "media", temp_folder))

    os.system("sudo zip -r9 %s %s" % (out_file, temp_folder))
    print "Written backup file: %s" % out_file
    server_ctl.main("start")
    return out_file


def create_weekly_backup(out_file):
    if time.strftime("%A") == "Monday":
        new_file = out_file.replace("Daily", "Weekly")
        os.system("sudo cp %s %s" % (out_file, new_file))
        print "Written backup file: %s" % new_file


def create_monthly_backup(out_file):
    if time.strftime("%d") == "15":
        new_file = out_file.replace("Daily", "Monthly")
        os.system("sudo cp %s %s" % (out_file, new_file))
        print "Written backup file: %s" % new_file

def create_yearly_backup(out_file):
    if time.strftime("%m_%d") == "01_01":
        new_file = out_file.replace("Daily", "Yearly")
        os.system("sudo cp %s %s" % (out_file, new_file))
        print "Written backup file: %s" % new_file


def prune_backup_files(filt, count):
    backup_folder = settings.WS_BACKUP_FOLDER

    file_list = glob.glob("%s/*" % backup_folder)
    if filt is not None:
        file_list = [fname for fname in file_list if filt in fname]

    files_info = []
    for fpath in file_list:
        files_info.append((os.path.getmtime(fpath), fpath))

    files_info = sorted(files_info, reverse=True)

    for ftime, fpath in files_info[count:]:
        print "Deleting old backup file: %s" % fpath
        os.system("sudo rm -f %s" % fpath)

def prune_backups():
    prune_backup_files("Daily.zip", 9)
    prune_backup_files("Weekly.zip", 6)
    prune_backup_files("Monthly.zip", 14)
    prune_backup_files("Yearly.zip", 5)


def main():
    print "Creating daily backup"
    out_file = create_daily_backup()

    create_weekly_backup(out_file)
    create_monthly_backup(out_file)
    create_yearly_backup(out_file)

    print "Pruning old backups"
    prune_backups()

if __name__ == "__main__":
    main()