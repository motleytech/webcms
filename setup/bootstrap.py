#!/usr/bin/python

import os
import ws_settings as settings

def run_command(cmd):
    print "\nRunning cmd : %s" % cmd
    rv = os.system(cmd)
    if rv != 0:
        print "Error while running %s. Stopping" % cmd
        exit(1)


def apt_get_install(package):
    cmd = "sudo apt-get install -y %s" % package
    print "\n\nInstalling %s...\n" % package
    run_command(cmd)

def aptitude_update_and_upgrade():
    run_command("sudo aptitude -y update")
    run_command("sudo aptitude -y upgrade")

def aptitude_install(package):
    cmd = "sudo aptitude install -y %s" % package
    print "\n\nInstalling %s...\n" % package
    run_command(cmd)

def make_directory(dpath):
    cmd = "sudo mkdir -p %s" % dpath
    run_command(cmd)

def take_ownership(dpath):
    cmd = "sudo chown -R `whoami`:`whoami` %s" % dpath
    run_command(cmd)

def set_permission(dpath, perm):
    cmd = "sudo chmod -R %s %s" % (perm, dpath)
    run_command(cmd)

def git_clone(repo, directory):
    cmd = "cd %s; git clone %s" % (directory, repo)
    run_command(cmd)

def delete_dir(dpath):
    cmd = "sudo rm -rf %s" % dpath
    run_command(cmd)



WS_ROOT_FOLDER = settings.server_root_folder
PIP_CACHE_FOLDER = settings.pip_cache_folder
REPO_NAME = settings.repo_url.split("/")[-1].split(".")[0]

apt_get_install("aptitude")
aptitude_update_and_upgrade()
aptitude_install("git")


print "Creating top level directories"

make_directory(WS_ROOT_FOLDER)
make_directory(PIP_CACHE_FOLDER)
make_directory(os.path.join(WS_ROOT_FOLDER, 'conf')

take_ownership(WS_ROOT_FOLDER)
take_ownership(PIP_CACHE_FOLDER)
set_permission(PIP_CACHE_FOLDER, 'a+rw')


if not os.path.exists(os.path.join(WS_ROOT_FOLDER, REPO_NAME)):
    print "Cloning git repository"
    make_clone = True
else:
    make_clone = False
    decision = raw_input("Git repo already exists. Overwrite (yes, no)? ")
    while decision.lower() not in ('yes', 'no'):
        print "Sorry... you need to enter 'yes' or 'no'."
        decision = raw_input("Git repo already exists. Overwrite (yes, no)? ")

    if decision == 'yes':
        make_clone = True
        delete_dir(os.path.join(WS_ROOT_FOLDER, REPO_NAME))


if make_clone is True:
    print "Cloning git repository..."
    git_clone(settings.repo_url, WS_ROOT_FOLDER)


# create user webuser and group webapps
print "\n\nCreating users and groups... \n\n"
run_command("sudo groupadd -f --system %s" % settings.user_group)
run_command("sudo useradd --system --gid %s --shell /bin/bash --home %s %s" % (settings.user_group, WS_ROOT_FOLDER, settings.user_name))
run_command("sudo usermod -a -G %s `whoami`" % settings.user_group)


# execute the real installer script now
print "\n\nRunning the main install script now... \n\n"
run_command("cd %s; python setup/install.py debug" % os.path.join(WS_ROOT_FOLDER, REPO_NAME))

# at the end... change permissions of folders

run_command("sudo chown -R %s:%s %s" % (settings.user_name, settings.user_group, WS_ROOT_FOLDER)
run_command("sudo chmod -R g+w %s" % WS_ROOT_FOLDER)

print "Setup Complete."
print "\n\nIf you intend to run the server in production, you should now copy your secrets file to %s folder." % os.path.join(WS_ROOT_FOLDER, 'conf')
print "\n\nYou should also edit the secrets file to change all the keys. The keys can be any random set of characters. The more and random, the better."

