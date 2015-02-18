import os
import sys

def main(cmd):
    import ws_settings as settings
    for name, domain, forw, nump in settings.SITE_DETAILS:
        os.system("sudo supervisorctl %s webcms_%s" % (cmd, name))

    os.system("sudo service nginx %s" % cmd)

if __name__ == "__main__":
    if ((len(sys.argv) != 2) or
        (sys.argv[1] not in ("start", "stop", "restart"))):
        print "usage: python server_ctl.py [start|stop|restart]"
        exit(1)
    main(sys.argv[1])
