#!/bin/bash

# check if env.sh exists in ~ folder
if [ -f ~/envs/env_webcms.sh ]; then
    echo "Environment file found. Good."
    # if it does, source env
    source ~/envs/env_webcms.sh
else
    # if it does not, output error message and exit
    echo "Error: Environment file is missing."
    echo ""
    echo "Please place env_webcms.sh file in ~/env folder"
    exit 1
fi

# install aptitude
sudo apt-get install -y aptitude

# update and upgrade aptitude
sudo aptitude -y update
sudo aptitude -y upgrade

# install git
sudo aptitude install -y git

# make folders and copy env file
sudo mkdir -p $ROOTFOLDER
sudo mkdir -p $ROOTFOLDER/envs
sudo cp -n ~/envs/env_webcms.sh $ROOTFOLDER/envs

# create user webuser and group webapps
sudo groupadd -f --system $WEBGROUP
sudo useradd --system --gid $WEBGROUP --shell /bin/bash --home $ROOTFOLDER $WEBUSER

# change the owner for $ROOTFOLDER
sudo chown -R $WEBUSER:$WEBGROUP $ROOTFOLDER
sudo chmod -R g+w $ROOTFOLDER

# add current user to group users
sudo usermod -a -G $WEBGROUP `whoami`

# clone git repo

sudo su $WEBUSER -c "git clone https://github.com/motleytech/webcms.git $ROOTFOLDER/webcms"


# 

