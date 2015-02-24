import os

SITES_DICT = {}
SITE_ID = SITES_DICT.get(os.environ.get('INSTANCE_SITE_NAME'), 2)
