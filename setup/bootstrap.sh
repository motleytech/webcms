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
echo -e "\n\nInstalling and updating aptitude... \n\n"
sudo apt-get install -y aptitude
sudo aptitude -y update
sudo aptitude -y upgrade

# install git
echo -e "\n\nInstalling git... \n\n"
sudo aptitude install -y git

# make folders and copy env file
echo -e "\n\nCreating directories... \n\n"
sudo mkdir -p $WEB_ROOT_FOLDER
sudo mkdir -p $WEB_ROOT_FOLDER/envs
sudo cp -n ~/envs/env_webcms.sh $WEB_ROOT_FOLDER/envs

sudo chown -R `whoami`:`whoami` $WEB_ROOT_FOLDER

# clone git repo
echo -e "\n\nCloning git repo... \n\n"
cd $WEB_ROOT_FOLDER

if [ -d $WEB_ROOT_FOLDER/$REPO_NAME ]; then
	echo "git repo already exists"
	cd $WEB_ROOT_FOLDER/$REPO_NAME
	sudo su $WEB_USER -c "git checkout ."
	sudo su $WEB_USER -c "git fetch origin"
	sudo su $WEB_USER -c "git merge origin/master"
else
	echo "cloning git repo now..."
	git clone $REPO_URL $WEB_ROOT_FOLDER/$REPO_NAME
fi


# create user webuser and group webapps
echo -e "\n\nCreating users and groups... \n\n"
sudo groupadd -f --system $WEB_GROUP
sudo useradd --system --gid $WEB_GROUP --shell /bin/bash --home $WEB_ROOT_FOLDER $WEB_USER
sudo usermod -a -G $WEB_GROUP `whoami`


# execute the real installer script now
echo -e "\n\nRunning the main install script now... \n\n"
cd $REPO_NAME
python setup/install.py debug


# at the end... change permissions of folders
sudo chown -R $WEB_USER:$WEB_GROUP $WEB_ROOT_FOLDER
sudo chmod -R g+w $WEB_ROOT_FOLDER

