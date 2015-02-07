import os

WEB_ROOT_FOLDER = os.environ.get('WEB_ROOT_FOLDER', '/webserver')
WEB_USER = os.environ.get('WEB_USER', 'webuser')

VENV_ROOT_FOLDER = os.path.join(WEB_ROOT_FOLDER, 'venvs')
VENV_NAME = os.path.join(WEB_ROOT_FOLDER, 'cms')
VENV_FOLDER = os.path.join(VENV_ROOT_FOLDER, VENV_NAME)

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

package_info = [
    ('aptitude', {
        'exists': [
            ('dpkg -s aptitude', 0),
            ],
        'install': [
            'sudo apt-get install -y aptitude',
            ],
    }),

    ('geany', {
        'exists': [
            ('dpkg -s geany', 0),
            ],
        'install': [
            'sudo aptitude install -y geany',
            ],
    }),

    ('git', {
        'exists': [
            ('dpkg -s git', 0),
            ],
        'install': [
            'sudo aptitude install -y git',
            ],
    }),

    ('diffuse', {
        'exists': [
            ('dpkg -s diffuse', 0),
            ],
        'install': [
            'sudo aptitude install -y diffuse',
            '''
            if grep -q "alias diffuse" ~/.bashrc; then
                echo "alias diffuse already exists"
            else
                echo "alias diffuse='/usr/bin/python /usr/bin/diffuse'" >> ~/.bashrc
            fi''',
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
            'sudo aptitude install -y build-essential',
            ],
    }),

    ('python-dev', {
        'exists': [
            ('dpkg -s python-dev', 0),
            ],
        'install': [
            'sudo aptitude install -y python-dev',
            ],
    }),

    ('python-setuptools', {
        'exists': [
            ('dpkg -s python-setuptools', 0),
            ],
        'install': [
            'sudo aptitude install -y python-setuptools',
            ],
    }),

    ('ipython', {
        'exists': [
            ('dpkg -s ipython', 0),
            ],
        'install': [
            'sudo aptitude install -y ipython',
            ],
    }),

    ('python-pip', {
        'exists': [
            ('dpkg -s python-pip', 0),
            ],
        'install': [
            'sudo aptitude install -y python-pip',
            ],
    }),

    ('python-imaging', {
        'exists': [
            ('dpkg -s python-imaging', 0),
            ],
        'install': [
            'sudo aptitude install -y python-imaging',
            ],
    }),

    ('virtualenvwrapper', {
        'exists': [
            ('dpkg -s python-virtualenv', 0),
            ],
        'install': [
            'sudo aptitude install -y python-virtualenv',
            ],
    }),

    ('vim', {
        'exists': [
            ('dpkg -s vim', 0),
            ],
        'install': [
            'sudo aptitude install -y vim',
            ],
    }),

    ('openssh-server', {
        'exists': [
            ('dpkg -s openssh-server', 0),
            ],
        'install': [
            'sudo aptitude install -y openssh-server',
            ],
    }),

    ('postgresql', {
        'exists': [
            ('dpkg -s postgresql', 0),
            ],
        'install': [
            'sudo aptitude install -y postgresql',
            ],
    }),

    ('pgadmin3', {
        'exists': [
            ('dpkg -s pgadmin3', 0),
            ],
        'install': [
            'sudo aptitude install -y pgadmin3',
            ],
    }),

    ('pillow-libs', {
        'exists': [
            ('dpkg -s libjpeg8-dev', 0),
            ('dpkg -s zlibc', 0),
            ('dpkg -s libtiff4-dev', 0),
            ],
        'install': [
            'sudo aptitude install -y zlibc',
            'sudo aptitude install -y libjpeg8-dev',
            'sudo aptitude install -y libtiff4-dev',
            ],
    }),


    ('create-virt-env', {
        'options': {
            'as_user': WEB_USER
        },
        'exists': [
            ('[ -d %s ]' % (VENV_FOLDER), 0)
            ],
        'install': [
            'mkdir -p %s; cd %s; virtualenv %s' % (VENV_ROOT_FOLDER, VENV_ROOT_FOLDER, VENV_NAME),
            ],
    }),

    ('install-virt-pkgs', {
        'options': {
            'as_user': WEB_USER
        },
        'install': [
            'source %s/bin/activate; pip install -r %s/requirements_cms.txt' % (VENV_FOLDER, THIS_DIR),
            ],
    }),

]
