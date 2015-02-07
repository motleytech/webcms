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
sudo mkdir -p $WEB_ROOT_FOLDER
sudo mkdir -p $WEB_ROOT_FOLDER/envs
sudo cp -n ~/envs/env_webcms.sh $WEB_ROOT_FOLDER/envs

# create user webuser and group webapps
sudo groupadd -f --system $WEB_GROUP
sudo useradd --system --gid $WEB_GROUP --shell /bin/bash --home $WEB_ROOT_FOLDER $WEB_USER

# change the owner for $WEB_ROOT_FOLDER
sudo chown -R $WEB_USER:$WEB_GROUP $WEB_ROOT_FOLDER
sudo chmod -R g+w $WEB_ROOT_FOLDER

# add current user to group users
sudo usermod -a -G $WEB_GROUP `whoami`

# clone git repo
sudo su $WEB_USER -c "git clone $REPO_URL $WEB_ROOT_FOLDER/$REPO_NAME"



# execute the real installer script now
sudo su $WEB_USER -c "cd $WEB_ROOT_FOLDER/$REPO_NAME; python setup/install.py"
