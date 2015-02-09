import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djcms.settings")
from django.contrib.sites.models import Site

new_site = Site.objects.create(domain="www.motleytech.net", name="motleytech.net")
print "\n\nSite Motleytech.net created with id : %s\n" % new_site.id
os.system('echo "\nSITE_ID = %s" >> djcms/settings.py' % new_site.id)
print "www.motleytech.net site id appended to settings."

new_site = Site.objects.create(domain="www.nagrajan.net", name="nagrajan.net")
print "\n\nSite nagrajan.net created with id : %s\n" % new_site.id

new_site = Site.objects.create(domain="www.nagrajan.com", name="nagrajan.com")
print "\n\nSite nagrajan.com created with id : %s\n" % new_site.id
