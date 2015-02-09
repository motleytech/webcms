import os
from pprint import pformat
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djcms.settings")
from django.contrib.sites.models import Site

site_dict = {}
existing_sites = dict([(s.domain, s.id) for s in Site.objects.all()])

site_id = None


if 'www.motleytech.net' in existing_sites:
	site_id = existing_sites["www.motleytech.net"]
else:
	new_site = Site.objects.create(domain="www.motleytech.net", name="motleytech")
	site_id = new_site.id

site_dict["www.motleytech.net"] = site_id
print "\n\nSite www.motleytech.net id : %s\n" % site_id


if 'www.nagrajan.com' in existing_sites:
	site_id = existing_sites["www.nagrajan.com"]
else:
	new_site = Site.objects.create(domain="www.nagrajan.com", name="nagrajan")
	site_id = new_site.id

site_dict["www.nagrajan.com"] = site_id
print "\n\nSite www.nagrajan.com id : %s\n" % site_id

outstr0 = "import os"
outstr1 = "SITES_DICT = %s" % pformat(site_dict)
outstr2 = "SITE_ID = SITES_DICT.get(os.environ.get('INSTANCE_SITE_NAME'), 1)"
outstr = "%s\n\n%s\n%s\n" % (outstr0, outstr1, outstr2)

os.system('echo "%s" > djcms/site_list.py' % outstr)

print "Site ids added to djcms/site_list.py."
