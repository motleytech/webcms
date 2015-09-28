
import subprocess

command = ["/bin/bash", "-c", "ssh root@motleytech.net 'ls -lrt /webserver_backup'"]
res = subprocess.check_output(command, stderr=subprocess.STDOUT)

res = res.strip().split("\n")
lastLine = res[-1]

fname = lastLine.split(" ")[-1]

print "Copying file \"%s\" to ~/backup folder." % fname


command2 = ["/bin/bash", "-c", "mkdir ~/backup; scp root@motleytech.net:/webserver_backup/%s ~/backup" % fname]

res = subprocess.check_output(command2, stderr=subprocess.STDOUT)

print res
