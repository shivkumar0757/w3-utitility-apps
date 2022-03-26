from django.shortcuts import render
from django.http import HttpResponse

from staking_status_app.st_pool_status import get_status

# Create your views here.
def index(request):
    st_data= get_status()
    return render(request,'stake/index.html',{'data':st_data})