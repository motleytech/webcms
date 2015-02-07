import logging
import os
import sys
import manifest

logger = logging.getLogger()
logger.setLevel(logging.INFO)
DEBUG = False

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def check_result(result, cmd, exit_on_error=True):
    if result == 0:
        logging.info("{}Success.{}".format(bcolors.OKGREEN, bcolors.ENDC))
        return True
    else:
        logging.error("Failed during command \n{}{}{}".format(bcolors.FAIL, cmd, bcolors.ENDC))
        if exit_on_error is True:
            logging.error("Quitting!!")
            exit(1)
        return False


def run_command(cmd,
                exit_on_error=True,
                check_res=True,
                stdout_redirect=True,
                as_user=None):
    logging.info("Running command \n{}{}{}".format(bcolors.OKBLUE, cmd, bcolors.ENDC))
    if (stdout_redirect is True) and (DEBUG is False):
        cmd += " > /dev/null"

    if as_user is not None:
        cmd = "sudo su %s -c '%s'" % (as_user, cmd)

    result = os.system(cmd)
    if check_res is True:
        return check_result(result, cmd, exit_on_error)
    return result


def run_commands(cmds,
                 exit_on_error=True,
                 check_res=True,
                 stdout_redirect=True,
                 as_user=None):
    result = True
    for cmd in cmds:
        rv = run_command(cmd,
                         exit_on_error,
                         check_res,
                         stdout_redirect,
                         as_user)
        result = result and rv
    return result


def check_exists(pkg, info):
    cmds = info.get('exists', None)
    if (cmds is None) or (cmds == []):
        return False

    for cmd, result in cmds:
        rv = run_command(cmd, exit_on_error=False, check_res=False)
        if rv != result:
            return False
    return True


def install_package(pkg, info):
    cmds = info.get('install', None)
    options = info.get('options', {})
    stdout_redirect = options.get('stdout_redirect', True)
    ignore_result = options.get('ignore_result', False)
    verify_install = options.get('verify_install', None)
    as_user = options.get(as_user, None)

    if (cmds is None) or (cmds == []):
        return False

    run_commands(cmds,
                 exit_on_error=(not ignore_result),
                 stdout_redirect=stdout_redirect,
                 as_user=as_user)

    if verify_install is not None:
        run_command(verify_install)


def run_install():
    for package, info in manifest.package_info:
        print "\n"
        logging.info("Processing package {}{}{}".format(bcolors.OKBLUE, package, bcolors.ENDC))
        exists = check_exists(package, info)
        if exists is False:
            logging.info("{}{}{} not satisfied. Processing...".format(
                bcolors.WARNING, package, bcolors.ENDC))
            install_package(package, info)
            logging.info("{}Satisfactory{}".format(bcolors.WARNING, bcolors.ENDC))
        else:
            logging.info("{}{}{} already satisfied. Skipping.".format(
                bcolors.OKGREEN, package, bcolors.ENDC))


if __name__ == "__main__":
    if 'debug' in sys.argv:
        DEBUG = True
    run_install()
