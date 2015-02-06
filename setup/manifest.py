VENV_FOLDER = '~/.virtualenvs'
VENV_NAME = 'cms'
APT_GET_DELAY = 24*60*60  # in seconds

package_info = [
    ('apt-get-update',
     {
         'exists': [
             ('[ $(($(date +%s) - $(stat -c %Y /var/lib/apt/periodic/update-success-stamp) - {})) -le 0 ]'.format(APT_GET_DELAY), 0),
             ],
         'install': [
             'sudo apt-get -y update',
             'sudo apt-get -y upgrade',
             ],
     }),

    ('sublime',
     {
         'exists': [
             ('cat ~/.bashrc | grep -q sublime_text', 0),
             ('ls /usr/local/bin | grep -q sublime', 0)
             ],
         'install': [
             'rm -rf /tmp/sublime',
             'sudo rm -rf /usr/local/bin/sublime',
             'wget http://c758482.r82.cf2.rackcdn.com/Sublime%20Text%202.0.2%20x64.tar.bz2 -O /tmp/sublime.tar.bz2',
             'cd /tmp; tar -xvjf sublime.tar.bz2',
             'mv /tmp/Sublime\ Text\ 2 /tmp/sublime',
             'sudo mv /tmp/sublime /usr/local/bin/sublime',
             '''
             if grep -q "alias sublime" ~/.bashrc; then
                 echo "alias sublime already exists"
             else
                 echo "alias sublime=/usr/local/bin/sublime/sublime_text" >> ~/.bashrc
             fi''',
             ],
     }),

    ('chrome',
     {
         'options':{
             'ignore_result': True,
             'verify_install': 'which google-chrome',
             },
         'exists': [
             ('which google-chrome', 0),
             ],
         'install': [
             'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/google-chrome-stable_current_amd64.deb',
             'sudo dpkg -i /tmp/google-chrome-stable_current_amd64.deb',
             'sudo apt-get -fy install',
             ],
     }),

    ('wingide', {
        'exists': [
            ('which wing4.1', 0)
            ],
        'install': [
            'sudo apt-get -y install enscript',
            'wget http://wingware.com/pub/wingide/4.1.14/wingide4.1_4.1.14-1_amd64.deb -O /tmp/wingide.deb',
            'sudo dpkg -i /tmp/wingide.deb',
            'sudo apt-get -fy install',
            ],
    }),

    ('fix-scrollbar-menubar', {
        'exists': [
            ('dpkg -s overlay-scrollbar', 256),
            ('dpkg -s liboverlay-scrollbar-0.2-0', 256),
            ('dpkg -s liboverlay-scrollbar3-0.2-0', 256),
            ('dpkg -s appmenu-gtk', 256),
            ('dpkg -s appmenu-gtk3', 256),
            ('dpkg -s appmenu-qt', 256),
            ],
        'install': [
            'sudo apt-get -y purge "scrollbar*"',
            'sudo apt-get -y purge appmenu-gtk appmenu-gtk3 appmenu-qt',
            ],
    }),

    ('geany', {
        'exists': [
            ('dpkg -s geany', 0),
            ],
        'install': [
            'sudo apt-get install -y geany',
            ],
    }),

    ('restricted-extras (fonts)', {
        'options': {
            'stdout_redirect': False,
            },
        'exists': [
            ('dpkg -s ubuntu-restricted-extras', 0)
            ],
        'install': [
            'sudo apt-get install -y ubuntu-restricted-extras'
            ],
    }),

    ('adobe reader', {
        'options': {
            'stdout_redirect': False,
            },
        'exists': [
            ('dpkg -s acroread', 0),
            ],
        'install': [
            'sudo apt-add-repository -y "deb http://archive.canonical.com/ $(lsb_release -sc) partner"',
            'sudo apt-get update',
            'sudo apt-get install -y acroread',
            ],
    }),

    ('ccsm',
     {
         'exists': [
             ('dpkg -s compizconfig-settings-manager', 0),
             ],
         'install': [
             'sudo apt-get install -y compizconfig-settings-manager',
             ],
     }),

    ('diffuse', {
        'exists': [
            ('dpkg -s diffuse', 0),
            ],
        'install': [
            'sudo apt-get install -y diffuse',
            '''
            if grep -q "alias diffuse" ~/.bashrc; then
                echo "alias diffuse already exists"
            else
                echo "alias diffuse='/usr/bin/python /usr/bin/diffuse'" >> ~/.bashrc
            fi''',
            ],
    }),

    ('git', {
        'exists': [
            ('dpkg -s git', 0),
            ],
        'install': [
            'sudo apt-get install -y git',
            ],
    }),

    ('git-configuration', {
        'exists': [
            ('cat ~/.gitconfig | grep motleytech', 0),
            ('cat ~/.gitconfig | grep motleytechnet', 0),
            ],
        'install': [
            'git config --global user.name motleytech',
            'git config --global user.email motleytechnet@gmail.com',
            'git config --global alias.st "status"',
            'git config --global alias.stat "status"',
            'git config --global alias.wdiff "diff --color-words"',
            'git config --global merge.tool diffuse',
            'git config --global merge.summary true',
            'git config --global difftool.prompt false',
            'git config --global diff.tool diffuse',
            'git config --global color.ui true',
            ],
    }),

    ('build-essential', {
        'exists': [
            ('dpkg -s build-essential', 0),
            ],
        'install': [
            'sudo apt-get install -y build-essential',
            ],
    }),

    ('python-dev', {
        'exists': [
            ('dpkg -s python-dev', 0),
            ],
        'install': [
            'sudo apt-get install -y python-dev',
            ],
    }),

    ('python-yaml', {
        'exists': [
            ('dpkg -s python-yaml', 0),
            ],
        'install': [
            'sudo apt-get install -y python-yaml',
            ],
    }),

    ('python-setuptools', {
        'exists': [
            ('dpkg -s python-setuptools', 0),
            ],
        'install': [
            'sudo apt-get install -y python-setuptools',
            ],
    }),

    ('ipython', {
        'exists': [
            ('dpkg -s ipython', 0),
            ],
        'install': [
            'sudo apt-get install -y ipython',
            ],
    }),

    ('pylint', {
        'exists': [
            ('dpkg -s pylint', 0),
            ],
        'install': [
            'sudo apt-get install -y pylint',
            ],
    }),

    ('python-pip', {
        'exists': [
            ('dpkg -s python-pip', 0),
            ],
        'install': [
            'sudo apt-get install -y python-pip',
            ],
    }),

    ('python-imaging', {
        'exists': [
            ('dpkg -s python-imaging', 0),
            ],
        'install': [
            'sudo apt-get install -y python-imaging',
            ],
    }),

    ('virtualenvwrapper', {
        'exists': [
            ('dpkg -s virtualenvwrapper', 0),
            ],
        'install': [
            'sudo apt-get install -y virtualenvwrapper',
            ],
    }),

    ('vim', {
        'exists': [
            ('dpkg -s vim', 0),
            ],
        'install': [
            'sudo apt-get install -y vim',
            ],
    }),

    ('openssh-server', {
        'exists': [
            ('dpkg -s openssh-server', 0),
            ],
        'install': [
            'sudo apt-get install -y openssh-server',
            ],
    }),

    ('postgresql', {
        'exists': [
            ('dpkg -s postgresql', 0),
            ],
        'install': [
            'sudo apt-get install -y postgresql',
            ],
    }),

    ('pgadmin3', {
        'exists': [
            ('dpkg -s pgadmin3', 0),
            ],
        'install': [
            'sudo apt-get install -y pgadmin3',
            ],
    }),

    ('pillow-libs', {
        'exists': [
            ('dpkg -s libjpeg8-dev', 0),
            ('dpkg -s zlibc', 0),
            ('dpkg -s libtiff4-dev', 0),
            ],
        'install': [
            'sudo apt-get install -y zlibc',
            'sudo apt-get install -y libjpeg8-dev',
            'sudo apt-get install -y libtiff4-dev',
            ],
    }),

    ('apt-cleanup', {
        'install': [
            'sudo apt-get -fy install',
            'sudo apt-get -y autoclean',
            'sudo apt-get -y autoremove',
        ],
    }),

    ('create-virt-env', {
        'exists': [
            ('[ -d %s/%s ]' % (VENV_FOLDER, VENV_NAME), 0)
            ],
        'install': [
            'mkdir -p %s; cd %s; virtualenv %s' % (VENV_FOLDER, VENV_FOLDER, VENV_NAME),
            ],
    }),

    ('install-virt-pkgs', {
        'install': [
            '/bin/bash -c "source %s/%s/bin/activate; pip install -r requirements_cms.txt"' % (VENV_FOLDER, VENV_NAME),
            ],
    }),

]
