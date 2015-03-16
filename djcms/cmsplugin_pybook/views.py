from django.shortcuts import render, HttpResponse
from django.conf import settings
import os

# Create your views here.
def showbook(request, bookname):
    if bookname.endswith("/"):
        bookname = bookname[:-1]
    path = os.path.join(settings.PYBOOK_EXPORT_PATH, "%s/%s" % ("full", bookname))
    data = open(path, 'r').read()
    return HttpResponse(data)

def customcss(request):
    return HttpResponse()
