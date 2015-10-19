from django.shortcuts import HttpResponse
from time import time
from top_inf import getTopData

API_GTR_CALL_PERIOD = 5

class ApiData(object):
    """
    Dummy class to hold useful attributes.
    """
    pass

apiData = ApiData()
apiData.lastGtrTime = time()
apiData.lastGtrData = getTopData()


# Create your views here.
def getTopResult(request):
    """
    Return the result of running the `top` command.
    """
    now = time()
    if now - apiData.lastGtrTime >= API_GTR_CALL_PERIOD:
        apiData.lastGtrData = getTopData()
        apiData.lastGtrTime = now
    return HttpResponse(apiData.lastGtrData)
