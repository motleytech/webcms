import os

import ws_settings as settings
from ws_utils import import_env_variables, print_fatal, print_info

################################################
#
#  CONSTANTS
#
################################################

ENV_WEBCMS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../conf/env_webcms.sh"))
env_vars = import_env_variables(ENV_WEBCMS_PATH)

WS_ROOT_FOLDER = settings.WS_ROOT_FOLDER
WS_USER = settings.WS_USER
VENV_ROOT_FOLDER = settings.VENV_ROOT_FOLDER
VENV_NAME = settings.VENV_NAME
VENV_FOLDER = settings.VENV_FOLDER
VENV_ACTIVATE_PATH = "%s/bin/activate" % VENV_FOLDER


PG_USER = settings.PG_USER
PG_DB = settings.PG_DB

try:
    PG_USER_PW = env_vars["PG_USER_PW"]
    PG_ADMIN_PW = env_vars["PG_ADMIN_PW"]
except:
    print_fatal("Could not load environment variables from conf/env_webcms.sh")
    print_fatal("Please follow install directions.\n\nAborting")
    exit(1)

BACKUP_FOLDER = settings.WS_BACKUP_FOLDER
PIP_CACHE_FOLDER = settings.WS_PIP_CACHE

MEDIA_FOLDER = os.path.join(WS_ROOT_FOLDER, 'media')
STATIC_FOLDER = os.path.join(WS_ROOT_FOLDER, 'static')
LOGS_FOLDER = os.path.join(WS_ROOT_FOLDER, 'logs')
RUN_FOLDER = os.path.join(WS_ROOT_FOLDER, 'run')

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


################################################
#
#  methods
#
################################################

def check_debug_setting():
    if settings.DJANGO_DEBUG:
        return 1  # debug is True
    return 0  # debug is False


################################################
#
#  CONFIGURATION
#
################################################

package_info = [
    ('check-debug', {
        'options': {
            'ignore_in_dev': True,
            },
        'install': [
            check_debug_setting,
            ],
    }),

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
            "sudo aptitude install -y diffuse",
            "sudo python %s/patch_diffuse.py" % THIS_DIR,
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

    ('libpq-dev', {
        'exists': [
            ('dpkg -s libpq-dev', 0),
            ],
        'install': [
            'sudo aptitude install -y libpq-dev',
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

    ('postgresql-contrib', {
        'exists': [
            ('dpkg -s postgresql-contrib', 0),
            ],
        'install': [
            'sudo aptitude install -y postgresql-contrib',
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

    ('python-virtualenv', {
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

    ('supervisor', {
        'exists': [
            ('dpkg -s supervisor', 0),
            ],
        'install': [
            'sudo aptitude install -y supervisor',
            ],
    }),

    ('nginx', {
        'exists': [
            ('dpkg -s nginx', 0),
            ],
        'install': [
            'sudo aptitude install -y nginx',
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



    ('create-pgsql-user', {
        'options': {
            'ignore_result': True,
            },
        'install': [
            'sudo su postgres -c \'psql -q -c "CREATE ROLE %s WITH CREATEDB LOGIN PASSWORD \'\\\'\'%s\'\\\'\'";\'' % (PG_USER, PG_USER_PW),
            ],
    }),

    ('create-pgsql-user', {
        'options': {
            'ignore_result': True,
            },
        'install': [
            'echo "ALTER USER postgres WITH PASSWORD \'%s\';" | sudo -u postgres psql postgres' % (PG_ADMIN_PW),
            ],
    }),

    ('create-pgsql-db', {
        'options': {
            'ignore_result': True,
            },
        'install': [
            'sudo su postgres -c "createdb -O %s -E UTF8 %s"' % (PG_USER, PG_DB),
            ],
    }),

    ('modify-pgsql-config', {
        'exists': [
            ('sudo su -c "cat /etc/postgresql/9.1/main/pg_hba.conf | grep %s"' % PG_USER, 0),
            ('sudo su -c "cat /etc/postgresql/9.1/main/pg_hba.conf | grep %s"' % PG_DB, 0),
            ],
        'install': [
            "sudo su -c 'echo \"local   %s   %s       md5\" >> /etc/postgresql/9.1/main/pg_hba.conf'" % (PG_DB, PG_USER),
            ],
    }),

    ('restart-postgres', {
        'install': [
            'sudo service postgresql restart',
            ],
    }),


    ('create-folders', {
        'exists': [
            ('[ -d %s ]' % MEDIA_FOLDER, 0),
            ('[ -d %s ]' % LOGS_FOLDER, 0),
            ('[ -d %s ]' % BACKUP_FOLDER, 0),
            ('[ -d %s ]' % RUN_FOLDER, 0),
            ('[ -d %s ]' % PIP_CACHE_FOLDER, 0),
            ],
        'install': [
            'mkdir -p %s' % MEDIA_FOLDER,
            'mkdir -p %s' % LOGS_FOLDER,

            'sudo mkdir -p %s' % BACKUP_FOLDER,
            'sudo chown -R `whoami`:`whoami` %s' % BACKUP_FOLDER,
            'sudo chmod -R a+w %s' % BACKUP_FOLDER,

            'mkdir -p %s' % RUN_FOLDER,
            'touch %s/gunicorn_motleytech_supervisor.log' % LOGS_FOLDER,
            'touch %s/gunicorn_nagrajan_supervisor.log' % LOGS_FOLDER,

            'sudo mkdir -p %s' % PIP_CACHE_FOLDER,
            'sudo chown -R `whoami`:`whoami` %s' % PIP_CACHE_FOLDER,
            'sudo chmod -R a+w %s' % PIP_CACHE_FOLDER,
            ],
    }),


    ('create-virt-env', {
        'exists': [
            ('[ -d %s ]' % (VENV_FOLDER), 0)
            ],
        'install': [
            'mkdir -p %s; cd %s; virtualenv %s' % (VENV_ROOT_FOLDER, VENV_ROOT_FOLDER, VENV_NAME),
            ],
    }),

    ('install-virt-pkgs', {
        'install': [
            # this needs bash for the source command
            '/bin/bash -c "source %s; pip install --download-cache %s -r %s/requirements_cms.txt"' % (VENV_ACTIVATE_PATH, PIP_CACHE_FOLDER, THIS_DIR),
            ],
    }),

    ('syncdb&migrate', {
        'options': {
            'stdout_redirect': False,
            },
        'install': [
            # this needs bash for the source command
            '/bin/bash -c "source %s; source %s/conf/env_webcms.sh; cd %s/webcms/djcms; python manage.py syncdb; python manage.py migrate"' % (VENV_ACTIVATE_PATH, WS_ROOT_FOLDER, WS_ROOT_FOLDER),
            '/bin/bash -c "source %s/bin/activate; source %s/conf/env_webcms.sh; cd %s/webcms/djcms; python manage.py collectstatic"' % (VENV_FOLDER, WS_ROOT_FOLDER, WS_ROOT_FOLDER),
            ],
    }),

    ('create_django_site', {
        'options': {
            'stdout_redirect': False,
            },
        'install': [
            '/bin/bash -c "source %s/bin/activate; source %s/conf/env_webcms.sh; cd %s/webcms/djcms; python setup_sites.py"' % (VENV_FOLDER, WS_ROOT_FOLDER, WS_ROOT_FOLDER),
            ],
    }),

    ('final-config', {
        'options': {
            'stdout_redirect': False,
            },
        'install': [
            # this needs bash for the source command
            'cp %s/webcms/config/env.sh %s/env.sh' % (WS_ROOT_FOLDER, WS_ROOT_FOLDER),

            'sudo cp %s/../config/webcms_motleytech.supervisor.conf /etc/supervisor/conf.d/webcms_motleytech.conf' % THIS_DIR,
            'sudo cp %s/../config/webcms_nagrajan.supervisor.conf /etc/supervisor/conf.d/webcms_nagrajan.conf' % THIS_DIR,
            'sudo supervisorctl reread',
            'sudo supervisorctl update',
            'sudo supervisorctl restart webcms_motleytech',
            'sudo supervisorctl restart webcms_nagrajan',

            'sudo cp %s/../config/webcms.nginx.conf /etc/nginx/sites-available/webcms' % THIS_DIR,
            'sudo ln -sf /etc/nginx/sites-available/webcms /etc/nginx/sites-enabled/webcms',
            'sudo service nginx restart',
            ],
    }),

]
