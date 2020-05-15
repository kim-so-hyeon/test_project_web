from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import pickle

class Cal3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getPredict(self):
        c = int(self.x) + int(self.y)
        return c

def home(request):
    value01 = request.GET['value1']
    value02 = request.GET['value2']
    val3 = Cal3(value01,value02)
    pickle.dump(val3, open("./hello/pickle_kimsohyeon.pkl","wb"))
    with open("./hello/pickle_kimsohyeon.pkl","rb") as pc :
        val_pkl = pickle.load(pc)
    result = val_pkl.getPredict()
    requestDict = {'result_response':result}
    return JsonResponse(requestDict)
    # return HttpResponse("Hello, Django!")
# Create your views here.