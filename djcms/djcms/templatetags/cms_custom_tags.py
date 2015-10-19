from django import template
from django.conf import settings
from traceback import print_exc
import logging
import json

register = template.Library()

@register.assignment_tag(takes_context=True)
def getHtml(context):

    try:
        data = json.loads(context.get('html', "{}"))
        html = data['html']
        return html
    except:
        logging.exception("Error in input html content: %s" % html)

    # fallback value in case nothing works
    return "getDivId_ran_into_error"

@register.assignment_tag(takes_context=True)
def getJavascript(context):
    try:
        data = json.loads(context.get('html', "{}"))
        js = data['javascript']
        return js
    except:
        logging.exception("Error in input html content: %s" % html)

    # fallback value in case nothing works
    return "getJs_ran_into_error"
