from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    value01 = request.GET['value1']
    value02 = request.GET['value2']
    # val = C3(4,6)
    import pickle
    # pickle.dump(val, open("./pickle_kimsohyeon.pkl","wb"))
    val_pkl = pickle.load(open("./pickle_kimsohyeon.pkl","rb"))
    result = val_pkl.getPredict()
    requestDict = {'result_response':result}
    return JsonResponse(requestDict)
    # return HttpResponse("Hello, Django!")
# Create your views here.