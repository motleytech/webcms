import os
from pprint import pformat
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djcms.settings")
from django.contrib.sites.models import Site

site_dict = {}

new_site = Site.objects.create(domain="www.motleytech.net", name="motleytech")
print "\n\nSite www.motleytech.net created with id : %s\n" % new_site.id

site_dict["www.motleytech.net"] = new_site.id

new_site = Site.objects.create(domain="www.nagrajan.com", name="nagrajan")
print "\n\nSite www.nagrajan.com created with id : %s\n" % new_site.id

site_dict["www.nagrajan.com"] = new_site.id


os.system('echo "\nSITES_DICT = %s" >> djcms/settins.py' % pformat(sites))
os.system('echo "\nSITE_ID = SITES_DICT[os.environ.get(\'INSTANCE_SITE_NAME\')]" >> djcms/settings.py')

print "Site ids appended to settings."
