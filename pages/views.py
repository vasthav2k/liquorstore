from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category
from star_ratings.models import Rating
# Create your views here.
def index(request):
    categorys=Category.objects.all()
    context={
        'categorys' : categorys
    }


    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')