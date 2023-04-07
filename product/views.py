from django.shortcuts import render, redirect
from .models import ProductModel

# Create your views here.
def product_list(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return redirect('/product')
    else:
        return redirect('/sign-in')

def product_create(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_product = ProductModel.objects.all().order_by()
            return render(request, 'product/home.html', {'product': all_product})
        else:
            return redirect('/sign-in')

    elif request.method == 'POST':
        create_product = ProductModel()
        create_product.code = request.POST.get('code', '')
        create_product.name = request.POST.get('name', '')
        create_product.description = request.POST.get('description', '')
        create_product.price = request.POST.get('price', '')
        create_product.size = request.POST.get('size', '')
        create_product.save()
        return redirect('/product')


