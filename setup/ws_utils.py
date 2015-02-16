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

def print_fatal(msg):
    print "{}{}{}".format(bcolors.FAIL, msg, bcolors.ENDC)

def print_warn(msg):
    print "{}{}{}".format(bcolors.WARNING, msg, bcolors.ENDC)

def print_succ(msg):
    print "{}{}{}".format(bcolors.OKGREEN, msg, bcolors.ENDC)

def print_info(msg):
    print "{}{}{}".format(bcolors.OKBLUE, msg, bcolors.ENDC)
