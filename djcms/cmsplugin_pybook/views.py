from django.shortcuts import render, HttpResponse
from mycms.settings import PYBOOK_EXPORT_PATH
import os

# Create your views here.
def showbook(request, bookname):
    if bookname.endswith("/"):
        bookname = bookname[:-1]
    path = os.path.join(PYBOOK_EXPORT_PATH, "%s/%s" % ("full", bookname))
    data = open(path, 'r').read()
    return HttpResponse(data)

def customcss(request):
    return HttpResponse()
