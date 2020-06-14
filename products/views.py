from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Category,Product
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
# Create your views here.

def products(request):
    if request.method == 'GET':
        products=Product.objects.order_by('product_date')
        categories=Category.objects.all()
        paginator=Paginator(products,6)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        context={
            'products':paged_products,
            'categories':categories
        }
        return render(request,"products/products.html",context)
    else:
        if "name" in request.POST:
            products=Product.objects.order_by('product_date')
        else:
            products=Product.objects.order_by('product_date').filter(category__name__icontains=request.POST['category'])
        paginator=Paginator(products,6)
        page=request.GET.get('page')
        categories=Category.objects.all()
        paged_products=paginator.get_page(page)
        context={
            'products':paged_products,
            'categories':categories
        }
        return render(request,"products/products.html",context)

def product(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    context={
        'product':product
    }
    return render(request,'products/product.html',context)