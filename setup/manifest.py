import os

import ws_settings as settings
from ws_utils import import_env_variables, print_fatal, print_info
from traceback import print_exc

################################################
#
#  CONSTANTS
#
################################################

ENV_WEBCMS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../conf/env_webcms.sh"))
env_vars = import_env_variables(ENV_WEBCMS_PATH)

WS_ROOT_FOLDER = settings.WS_ROOT_FOLDER
WS_USER = settings.WS_USER
WS_GROUP = settings.WS_GROUP
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

def create_sites():
    from ws_utils import createDjangoSites
    try:
        result = createDjangoSites()
        if result is True:
            return 0
        return 1
    except:
        print_exc()
        return 1


def create_configs():
    from ws_utils import createGuniSuperAndNginxConfigs
    try:
        result = createGuniSuperAndNginxConfigs()
        if result is True:
            return 0
        return 1
    except:
        print_exc()
        return 1


def create_pybook_config():
    from ws_utils import createPybookSupervisorConfig
    try:
        result = createPybookSupervisorConfig()
        if result is True:
            return 0
        return 1
    except:
        print_exc()
        return 1

def configure_supervisor_and_nginx():
    from ws_utils import conf_supervisor_and_nginx

    try:
        result = conf_supervisor_and_nginx()
        if result is True:
            return 0
        return 1
    except:
        print_exc()
        return 1
    return 0


def config_supervisor_for_pybook():
    from ws_utils import conf_supervisor_for_pybook

    try:
        result = conf_supervisor_for_pybook()
        if result is True:
            return 0
        return 1
    except:
        print_exc()
        return 1
    return 0

def start_supervisor_pybook_and_nginx():
    from ws_utils import startSupervisorPybookAndNginx
    try:
        result = startSupervisorPybookAndNginx()
        if result is True:
            return 0
        return 1
    except:
        print_exc()
        return 1
    return 0

################################################
#
#  CONFIGURATION
#
################################################

package_info = [
    ('check-debug', {
        'options': {
            'only_in_prod': True,
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

    ('upgrade-pip', {
        'install': [
            'sudo pip install -U pip',
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
    } if settings.DESKTOP_INSTALL is True else None),

    ('geany', {
        'exists': [
            ('dpkg -s geany', 0),
            ],
        'install': [
            'sudo aptitude install -y geany',
            ],
    } if settings.DESKTOP_INSTALL is True else None),

    ('build-essential', {
        'exists': [
            ('dpkg -s build-essential', 0),
            ],
        'install': [
            'sudo aptitude install -y build-essential',
            ],
    }),

    ('zip', {
        'exists': [
            ('dpkg -s zip', 0),
            ],
        'install': [
            'sudo aptitude install -y zip',
            ],
    }),

    ('htop', {
        'exists': [
            ('dpkg -s htop', 0),
            ],
        'install': [
            'sudo aptitude install -y htop',
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
    } if settings.DESKTOP_INSTALL is True else None),

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
            'no_echo': True,
            },
        'install': [
            'sudo su postgres -c \'psql -q -c "CREATE ROLE %s WITH CREATEDB LOGIN PASSWORD \'\\\'\'%s\'\\\'\'";\'' % (PG_USER, PG_USER_PW),
            'echo "ALTER USER %s WITH PASSWORD \'%s\';" | sudo -u postgres psql postgres' % (PG_USER, PG_USER_PW),
            ],
    }),

    ('modify-postgres-pw', {
        'options': {
            'ignore_result': True,
            'no_echo': True,
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
        'install': [
            'mkdir -p %s' % MEDIA_FOLDER,
            'mkdir -p %s' % LOGS_FOLDER,
            'mkdir -p %s' % RUN_FOLDER,

            'sudo mkdir -p %s' % BACKUP_FOLDER,
            'sudo chown -R `whoami`:`whoami` %s' % BACKUP_FOLDER,
            'sudo chmod -R a+w %s' % BACKUP_FOLDER,


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
            '/bin/bash -c "source %s; pip install distribute==0.7.3"' % VENV_ACTIVATE_PATH,
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

    ('create_sites', {
        'install': [
            create_sites,
            ],
    }),

    ('install_pybook', {
        'options': {
            'stdout_redirect': False,
            },
        'install': [
            'cd %s; python install.py' % ("%s/webcms/djcms/pybook/setup" % WS_ROOT_FOLDER),
            ],
    }),

    ('create_configs', {
        'options': {
            'only_in_prod': True,
            },
        'install': [
            create_configs,
            create_pybook_config,
            config_supervisor_for_pybook,
            configure_supervisor_and_nginx,
        ],
    }),

    ('set_owner_and_permissions', {
        'options': {
            'stdout_redirect': False,
            'ignore_result': True,
            'only_in_prod': True,
            },
        'install': [
            "sudo groupadd -f --system %s" % WS_GROUP,
            "sudo useradd --system --gid %s --shell /bin/bash --home %s %s" % (WS_GROUP, WS_ROOT_FOLDER, WS_USER),
            "sudo usermod -a -G %s `whoami`" % WS_GROUP,
            "sudo chown -R %s:%s %s" % (WS_USER, WS_GROUP, WS_ROOT_FOLDER),
            "sudo chmod -R g+w %s" % WS_ROOT_FOLDER,
            ],
    }),

    ('start_supervisor_pybook_and_nginx', {
        'options': {
            'stdout_redirect': False,
            'only_in_prod': True,
            },
        'install': [
            start_supervisor_pybook_and_nginx,
        ],
    }),

    ("setup_backup_cron", {
        'options': {
            'stdout_redirect': False,
            'only_in_prod': True,
            },
        'exists': [
            ('sudo crontab -l | grep %s/backup.py' % (THIS_DIR), 0)
            ],
        'install': [
            "sudo su -c 'crontab -l | { cat; echo \"30 3 * * * python %s/backup.py 2>&1 | logger\"; } | crontab -'" % (THIS_DIR),
        ],
    }),
]
