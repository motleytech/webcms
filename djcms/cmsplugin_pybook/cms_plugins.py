import os
import glob

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings

from .models import PyBookName

class PyBookListPlugin(CMSPluginBase):
    model = CMSPlugin
    name = "PyBook List"
    render_template = "pybook_list_plugin.html"

    def render(self, context, instance, placeholder):
        path = os.path.join(settings.PYBOOK_EXPORT_PATH, "full")
        namesAndUrls, error_string = getNamesAndUrls(path)
        context['namesAndUrls'] = namesAndUrls
        context['errors'] = error_string
        return context


class PyBookBasicView(CMSPluginBase):
    model = PyBookName
    name = "PyBook Basic"
    render_template = "pybook_basic_view.html"

    def render(self, context, instance, placeholder):
        path = os.path.join(settings.PYBOOK_EXPORT_PATH,
                            "basic/%s" % instance.pybookName)
        data, error_string = getPybookBasic(path)
        context['basic_data'] = data
        context['errors'] = error_string
        return context


plugin_pool.register_plugin(PyBookListPlugin)
plugin_pool.register_plugin(PyBookBasicView)


################################################################
#
# Support methods
#
################################################################


def getNamesAndUrls(fpath):
    namesAndUrls = []
    error_string = ""
    if not os.path.exists(fpath):
        error_string = "%s is not a valid folder path. Nothing to show" % fpath
    else:
        try:
            file_list = glob.glob("%s/*.html" % fpath)
            for path in file_list:
                name = path.split("/")[-1]
                url = "cmsplugin_pybook/%s" % name
                namesAndUrls.append((name, url))
        except:
            import traceback
            error_string = traceback.format_exc()

    return (namesAndUrls, error_string)

def getPybookBasic(bookpath):
    data = None
    errors = ""
    if not os.path.exists(bookpath):
        errors = "%s is not a valid file path. Nothing to show" % bookpath
    else:
        try:
            data = open(bookpath, 'r').read()
        except:
            from traceback import format_exc
            errors = format_exc()
    return (data, errors)

