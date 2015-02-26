import os
import subprocess

class bcolors(object):
    """Colors for the terminal"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def import_env_variables(env_file_path):
    env_vars = {}
    command = ['bash', '-c', 'source %s && env' % env_file_path]
    proc = subprocess.Popen(command, stdout = subprocess.PIPE)

    for line in proc.stdout:
        (key, _, value) = line.partition("=")
        env_vars[key] = os.environ[key] = value.strip()

    proc.communicate()
    return env_vars

#def get_command_output(cmd):
    #output = []
    #command = ['bash', '-c', cmd]
    #proc = subprocess.Popen(command, stdout = subprocess.PIPE)

    #for line in proc.stdout:
        #output.append(line)

    #proc.communicate()
    #return output

def print_fatal(msg):
    print "{}{}{}".format(bcolors.FAIL, msg, bcolors.ENDC)

def print_warn(msg):
    print "{}{}{}".format(bcolors.WARNING, msg, bcolors.ENDC)

def print_succ(msg):
    print "{}{}{}".format(bcolors.OKGREEN, msg, bcolors.ENDC)

def print_info(msg):
    print "{}{}{}".format(bcolors.OKBLUE, msg, bcolors.ENDC)



def createSites():
    import ws_settings as settings

    VENV_FOLDER = settings.VENV_FOLDER
    WS_ROOT_FOLDER = settings.WS_ROOT_FOLDER

    cmd = '/bin/bash -c "source %s/bin/activate; source %s/conf/env_webcms.sh; cd %s/webcms/djcms; python setup_sites.py"' % (VENV_FOLDER, WS_ROOT_FOLDER, WS_ROOT_FOLDER)

    return os.system(cmd)


def write_from_template(inp_path, out_path, kwargs):
    input_file = open(inp_path, 'r')
    input_template = input_file.read()
    config_data = input_template.format(**kwargs)

    output_file = open(out_path, 'w')
    output_file.write(config_data)

    input_file.close()
    output_file.close()


def createGunicornConfig():
    import ws_settings as settings
    REPO_FOLDER = "%s/%s" % (settings.WS_ROOT_FOLDER, settings.REPO_NAME)

    this_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.abspath(os.path.join(this_dir, "../config"))
    out_conf_dir = os.path.abspath(os.path.join(this_dir, "../../conf"))

    input_filepath = os.path.join(template_dir, "gunicorn_sh.template")


    for name, domain, forw, nump in settings.SITE_DETAILS:
        args = dict(
            WS_ROOT_FOLDER = settings.WS_ROOT_FOLDER,
            VENV_FOLDER = settings.VENV_FOLDER,
            SITE_NAME = name,
            REPO_FOLDER = REPO_FOLDER,
            WS_USER = settings.WS_USER,
            WS_GROUP = settings.WS_GROUP,
            NUM_WORKERS = nump,
            WSGI_MODULE = "${DJANGO_WSGI_MODULE}",
        )

        output_filepath = os.path.join(out_conf_dir, "gunicorn_%s.sh" % name)
        write_from_template(input_filepath, output_filepath, args)

        # make the file executable
        os.system("chmod a+x %s" % output_filepath)
    return 0

def createSupervisorConfig():
    import ws_settings as settings

    this_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.abspath(os.path.join(this_dir, "../config"))
    out_conf_dir = os.path.abspath(os.path.join(this_dir, "../../conf"))

    input_filepath = os.path.join(template_dir, "supervisor_conf.template")

    for name, domain, forw, nump in settings.SITE_DETAILS:
        args = dict(
            WS_ROOT_FOLDER = settings.WS_ROOT_FOLDER,
            SITE_NAME = name,
            WS_USER = settings.WS_USER,
        )

        output_filepath = os.path.join(out_conf_dir, "supervisor_%s.conf" % name)
        write_from_template(input_filepath, output_filepath, args)
    return 0


def createNginxConfig():
    import ws_settings as settings
    REPO_FOLDER = "%s/%s" % (settings.WS_ROOT_FOLDER, settings.REPO_NAME)

    this_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.abspath(os.path.join(this_dir, "../config"))
    out_conf_dir = os.path.abspath(os.path.join(this_dir, "../../conf"))

    input_filepath = os.path.join(template_dir, "nginx_conf.template")


    for name, domain, forw, nump in settings.SITE_DETAILS:
        args = dict(
            WS_ROOT_FOLDER = settings.WS_ROOT_FOLDER,
            SITE_NAME = name,
            DOMAIN = domain,
            REPO_FOLDER = REPO_FOLDER,
            FORWARD_DOMAIN = forw,
        )

        output_filepath = os.path.join(out_conf_dir, "nginx_%s" % name)
        write_from_template(input_filepath, output_filepath, args)
    return 0


def createDjangoSites():
    rv = createSites()
    if rv != 0:
        return rv
    return True


def createGuniSuperAndNginxConfigs():
    rv = createGunicornConfig()
    if rv != 0:
        return rv

    rv = createSupervisorConfig()
    if rv != 0:
        return rv

    rv = createNginxConfig()
    if rv != 0:
        return rv

    return True


def conf_supervisor_and_nginx():
    import ws_settings as settings

    this_dir = os.path.dirname(os.path.abspath(__file__))
    out_conf_dir = os.path.abspath(os.path.join(this_dir, "../../conf"))

    for name, domain, forw, nump in settings.SITE_DETAILS:
        sup_fname = "supervisor_%s.conf" % name
        sup_op_fpath = os.path.join(out_conf_dir, sup_fname)

        # copy supervisor config
        os.system("sudo cp %s /etc/supervisor/conf.d/%s" % (sup_op_fpath, sup_fname))
        # create supervisor log files
        os.system("touch %s/logs/supervisor_gunicorn_%s.log" % (
            settings.WS_ROOT_FOLDER, name))

        nginx_fname = "nginx_%s" % name
        nginx_op_fpath = os.path.join(out_conf_dir, nginx_fname)

        # copy nginx config
        os.system("sudo cp %s /etc/nginx/sites-available/%s" % (nginx_op_fpath, nginx_fname))
        os.system("sudo ln -sf /etc/nginx/sites-available/%s /etc/nginx/sites-enabled/%s" % (nginx_fname, nginx_fname))

    return True


def startSupervisorAndNginx():
    import ws_settings as settings

    os.system("sudo supervisorctl reread")
    os.system("sudo supervisorctl update")
    for name, domain, forw, nump in settings.SITE_DETAILS:
        os.system("sudo supervisorctl start webcms_%s" % name)

    os.system("sudo service nginx restart")

    return True
