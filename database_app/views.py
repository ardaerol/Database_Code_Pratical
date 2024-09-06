from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    data = models.Musician.objects.all()
    data_context = {"musicians":data}
    return render(request,'database_app/index.html',context=data_context)