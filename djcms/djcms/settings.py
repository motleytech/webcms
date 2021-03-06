import os
import sys
import logging

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

"""
Django settings for djcms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

def load_ws_settings():
    setup_folder = os.path.abspath(os.path.join(THIS_DIR, "../../setup"))

    sys.path.append(setup_folder)
    import ws_settings
    sys.path.pop()
    return ws_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ws_settings = load_ws_settings()

WS_ROOT_FOLDER = ws_settings.WS_ROOT_FOLDER
PG_USER = ws_settings.PG_USER
PG_USER_PW = os.environ["PG_USER_PW"]
PG_DB = ws_settings.PG_DB


# add djangocms_blog's parent folder to python path
djangocms_blog_folder = os.path.abspath(os.path.join(THIS_DIR, "../djangocms-blog"))
sys.path.append(djangocms_blog_folder)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# '5f+2nreb_i&7roc6o-qf5jv=&f1oe+-v9_l8t3orz%4%u(zx1c'
SECRET_KEY = os.environ["DJANGO_SECRET"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ws_settings.DJANGO_DEBUG

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

ROOT_URLCONF = 'djcms.urls'

WSGI_APPLICATION = 'djcms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(WS_ROOT_FOLDER, 'media')
STATIC_ROOT = os.path.join(WS_ROOT_FOLDER, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'djcms', 'static'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings'
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'djcms', 'templates'),
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'mptt',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'south',
    'reversion',
    'djcms',

    # djangocms-blog apps
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'django_select2',
    'meta',
    'meta_mixin',
    'admin_enhancer',
    'djangocms_blog',

    'cmsplugin_disqus',
)

DISQUS_SHORTNAME = ws_settings.DISQUS_SHORTNAME

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
    'taggit': 'taggit.south_migrations',
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

PARLER_LANGUAGES = {
    1: (
        {'code': 'en',},
    ),
}

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': PG_DB,
        'HOST': u'localhost',
        'USER': PG_USER,
        'PASSWORD': PG_USER_PW,
        'PORT': ''
    }
}


# import sites from config directory
import imp

try:
    siteListPath = os.path.abspath(os.path.join(THIS_DIR, "../../../conf/site_list.py"))
    site_list = imp.load_source('site_list', siteListPath)

    SITE_ID = site_list.SITE_ID
except IOError:
    # site_list.py file has not been created yet
    # we are probably in syncdb / migrate step in the install
    logging.error("Failed to import site_list.py.\nCan be safely ignored during setup")
    SITE_ID = 1

