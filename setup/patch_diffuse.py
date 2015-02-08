#!/usr/bin/python

import os
import subprocess
from pprint import pprint as pp

def diffuse_has_python_path_problem(dpath):
    fdata = open(dpath, 'r')

    first_line = fdata.readline()
    if first_line.startswith("#!/usr/bin/env python"):
        return True
    return False


def fix_diffuse_python_path(dpath, tempfile):
    inp_file = open(dpath, 'r')
    out_file = open(tempfile, 'w')

    first_line = inp_file.readline()
    first_line = first_line.replace("#!/usr/bin/env python", "#!/usr/bin/python")
    out_file.write(first_line)
    for line in inp_file.readlines():
        out_file.write(line)

    inp_file.close()
    out_file.close()


def check_and_apply_patch(diffuse_path):
    if diffuse_has_python_path_problem(diffuse_path):
        # fix problem
        tempfile = "/tmp/diffuse"
        fix_diffuse_python_path(diffuse_path, tempfile)
        result1 = os.system("mv %s %s" % (tempfile, diffuse_path))
        result2 = os.system("chmod a+x %s" % (diffuse_path))

        if result1 == 0 and result2 == 0:
            print "Successfully patched diffuse"
        else:
            print "Error in patching diffuse"
            exit(1)
    else:
        # no problem... happy message and exit
        print "Patching not required or already patched"

if __name__ == "__main__":
    command = ['bash', '-c', 'which diffuse']
    proc = subprocess.Popen(command, stdout = subprocess.PIPE)

    diffuse_path = [line.strip() for line in proc.stdout][0]

    proc.communicate()
    print "Running script to patch diffuse... %s" % diffuse_path

    check_and_apply_patch(diffuse_path)

