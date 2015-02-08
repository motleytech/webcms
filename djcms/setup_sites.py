import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djcms.settings")
from django.contrib.sites.models import Site

new_site = Site.objects.create(domain="motleytech.net", name="motleytech.net")

print "\n\nSite Motleytech.net created with id : %s\n" % new_site.id
os.system('echo -e "\nSITE_ID = %s" >> djcms/settings.py' % new_site.id)

print "New site id appended to settings."
