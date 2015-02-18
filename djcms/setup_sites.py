import os
from pprint import pformat
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djcms.settings")
from django.contrib.sites.models import Site
import sys

def load_ws_settings():
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    setup_folder = os.path.abspath(os.path.join(THIS_DIR, "../setup"))

    sys.path.append(setup_folder)
    import ws_settings
    sys.path.pop()

    return ws_settings


def main():
    site_dict = {}
    existing_sites = dict([(s.domain, s.id) for s in Site.objects.all()])

    site_id = None

    ws_settings = load_ws_settings()

    for name, domain, forw, nump in ws_settings.SITE_DETAILS:
        if name in existing_sites:
            site_id = existing_sites[name]
        else:
            new_site = Site.objects.create(domain=domain, name=name)
            site_id = new_site.id

        site_dict[name] = site_id
        print "\n\nSite %s id : %s\n" % (name, site_id)

    outstr0 = "import os"
    outstr1 = "SITES_DICT = %s" % pformat(site_dict)
    outstr2 = "# INSTANCE_SITE_NAME is set in gunicorn run script"
    outstr3 = "SITE_ID = SITES_DICT.get(os.environ.get('INSTANCE_SITE_NAME'), 1)"
    outstr = "%s\n\n%s\n\n%s\n%s\n" % (outstr0, outstr1, outstr2, outstr3)

    os.system('echo "%s" > djcms/site_list.py' % outstr)

    print "Site ids added to djcms/site_list.py."


if __name__ == "__main__":
    main()
