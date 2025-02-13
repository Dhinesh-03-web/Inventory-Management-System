from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.db.models import Sum
from .models import *
import datetime
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *



# Login and Logout Views
def login_page(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect("/dashboard/")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("")
    
    return render(request, "login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully")
    return redirect("")


# Dashboard Views
datetime=datetime.datetime.now()
def Dashboard(request):
    # Month Name Display
    month_name=datetime.strftime("%B")
    # Product Low in Stock Table Data
    product_data=Product.objects.order_by('in_stock')
    # Category, Product, Labours, Suppliers Count
    cat_count=Category.objects.aggregate(Count('id'))
    product_count=Product.objects.aggregate(Count('id'))
    labour_count=Labours.objects.aggregate(Count('id'))
    supplier_count=Suppliers.objects.aggregate(Count('id'))
    # Total sales, purchase and due
    total_purchase_sum = Suppliers.objects.aggregate(Sum('total_purchase'))['total_purchase__sum']
    total_purchase_due_sum= Suppliers.objects.aggregate(Sum('purchase_due'))['purchase_due__sum']
    total_sales_sum=Salesreport.objects.aggregate(Sum('amount'))['amount__sum']

    # if purchase, slaes, due is zero then print 0
    if total_purchase_sum is None:
        total_purchase_sum = 0
    if total_purchase_due_sum is None:
        total_purchase_due_sum= 0
    if total_sales_sum is None:
        total_sales_sum=0


    return render(request, "Dashboard.html", {'data':product_data,'cat_count':cat_count, 'product_count':product_count, 'labour_count':labour_count, 'supplier_count':supplier_count, 'month_name':month_name,'total_purchase':total_purchase_sum, 'total_due':total_purchase_due_sum, 'total_sales':total_sales_sum })


# Category Views
def CategoryViews(request):
    categories = Category.objects.all()
    return render(request, 'Manage_Category.html', {'data': categories})

def EditCategory(request,id):
    a=Category.objects.get(id=id)
    if request.method=="POST":
        cat_name=request.POST["cat_name"]
        a.cat_name=cat_name
        a.save()
        return redirect("/category/")
    return  render(request, "Edit_Category.html", {'a':a})

def NewCategory(request):
    if request.method == "POST":
        name=request.POST['cat_name']
        a=Category.objects.create(cat_name=name)
        a.save()
        return redirect("/category/")
    return  render(request, "New_Category.html")

def delete_category(request, id):
    a=Category.objects.get(id=id)
    a.delete()
    return redirect('category') 


# Product Views
def ProductManage(request):
    product_data=Product.objects.all()
    return render(request, "Manage_Products.html", {"data":product_data})
 
def EditProduct(request,id):
    categories=Category.objects.all()
    a=Product.objects.get(id=id)
    if request.method == "POST":
        product_name=request.POST['product_name']
        cat_name_id=request.POST['cat_name']
        in_stock=request.POST['in_stock']
        min_stock=request.POST['min_stock']
        cat_name=Category.objects.get(id=cat_name_id)
        a.product_name=product_name
        a.cat_name=cat_name
        a.in_stock=in_stock
        a.min_stock=min_stock
        a.save()
        return redirect("/manageproduct/")
    return  render(request, "Edit_Product.html", {'a':a,
                                                  'categories':categories, 
                                                  'current_category_id': a.cat_name.id})

def NewProduct(request):
    categories=Category.objects.all()
    if request.method == "POST":
        category_id=request.POST['cat_name']
        products_name=request.POST['product_name']
        instock=request.POST['in_stock']
        minstock=request.POST['min_stock']
        category = Category.objects.get(id=category_id) 
        a=Product.objects.create(cat_name=category, product_name=products_name , in_stock=instock, min_stock=minstock)
        a.save()
        return redirect("/manageproduct/")
    return  render(request, "New_Product.html" , {'categories':categories})

def delete_product(request, id):
    a=Product.objects.get(id=id)
    a.delete()
    return redirect('manageproduct') 


# Labours Views
def ManageLabour(request):
    labours_data=Labours.objects.all()
    return render(request, "Manage_Labours.html",{"data":labours_data})

def EditLabour(request,id):
    a=Labours.objects.get(id=id)
    if request.method == "POST":
        lab_name=request.POST['lab_name']
        phone_number=request.POST['phone_no']
        salary=request.POST['salary']
        a.lab_name=lab_name
        a.phone_no=phone_number
        a.salary=salary
        a.save()
        return redirect("/managelabour/")
    return  render(request, "Edit_Labour.html" ,{'a':a})

def NewLabour(request):
    if request.method == "POST":
        labour_name=request.POST['lab_name']
        phone=request.POST['phone_no']
        salary=request.POST['salary']
        a=Labours.objects.create(lab_name=labour_name, phone_no=phone, salary=salary)
        a.save()
        return redirect("/managelabour/")
    return  render(request, "New_Labour.html")

def delete_labour(request, id):
    a=Labours.objects.get(id=id)
    a.delete()
    return redirect('managelabour')


# Suppliers Views
def ManageSupplier(request):
    supplier_data=Suppliers.objects.all()
    return render(request, "Manage_suppliers.html",{'data':supplier_data})

def EditSupplier(request,id):
    edit=Suppliers.objects.get(id=id)
    if request.method=="POST":
        company_name=request.POST['company_name']
        supplier_name=request.POST['supplier_name']
        phone_number=request.POST['phone_number']
        company_address=request.POST['company_address']
        total_purchase=request.POST['total_purchase']
        purchase_due=request.POST['purchase_due']
        edit.company_name=company_name
        edit.supplier_name=supplier_name
        edit.phone_number=phone_number
        edit.company_address=company_address
        edit.total_purchase=total_purchase
        edit.purchase_due=purchase_due
        edit.save()
        return redirect('/managesupplier/')
    return  render(request, "Edit_Supplier.html", {'edit':edit})

def NewSupplier(request):
    if request.method =="POST":
        com_name=request.POST['company_name']
        sup_name=request.POST['supplier_name']
        phone=request.POST['phone_number']
        com_add=request.POST['company_address']
        add=Suppliers.objects.create(company_name=com_name, supplier_name=sup_name, phone_number=phone, company_address=com_add)
        add.save()
        return redirect("/managesupplier/")
    return  render(request, "New_Supplier.html")

def delete_supplier(request, id):
   a=Suppliers.objects.get(id=id)
   a.delete()
   return redirect('managesupplier')

# Sales Report Views
def SalesReport(request):
    sales_data=Salesreport.objects.all()
    if request.method == "POST":
        enter_date=request.POST['date']
        amount=request.POST['amount']
        a=Salesreport.objects.create(date=enter_date, amount=amount)
        a.save()
    return  render(request, "Sales_Report.html",{'data':sales_data})

def delete_sales_report(request, id):
    a=Salesreport.objects.get(id=id)
    a.delete()
    return redirect('salesreport')  # Redirect to your actual list view name

def SettingsViews(request):
    store_name=Settings.objects.all()
    return render(request, "Settings.html", {'data':store_name})

def SettingsEditView(request,id):
    a=Settings.objects.get(id=id)
    if request.method == "POST":
        store_name=request.POST['store_name']
        a.store_name=store_name
        a.save()
        return redirect("/settings/")
    return  render(request, "Settings_Edit.html" ,{'a':a})

# ----------------------------------------------------------------------------------------
# API for all functionality

# category API for view,add,edit,delete
# view API(GET method)
@api_view(["GET"])
def cat_view(request):
    datas= Category.objects.all()
    serializer =categoryserializer(datas,many=True)
    return Response(serializer.data)

# Add API (POST Method)
@api_view(['POST'])
def cat_add(request):
    serializer = categoryserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"The data is required"})
    
# Edit API (PUT Method)
@api_view(["PUT"])
def cat_edit(request,pk):
    data= Category.objects.get(id=pk)
    serializer=categoryserializer(data,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"Enter the data"})
    
# Delete API (DELETE Method)
@api_view(["DELETE"])
def cat_delete(request,id):
    data= Category.objects.get(id=id)
    serializer= categoryserializer(data,many=False)
    data.delete()
    return Response(serializer.data)

# Products API
# View API (GET Method)
@api_view(['GET'])
def pro_view(request):
    datas=Product.objects.all()
    serializer = productserializer(datas,many=True)
    return Response(serializer.data)

# Add API (POST Method)
@api_view(["POST"])
def pro_add(request):
    serializer = productserializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"The data is required"})
    
# Edit API for product (PUT Method)
@api_view(["PUT"])
def pro_edit(request,pk):
    data=Product.objects.get(id=pk)
    serializer = productserializer(data,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"Enter the data"})
    
# Delete API for product (DELETE Method)
@api_view(["DELETE"])
def pro_delete(request,pk):
    data =Product.objects.get(id=pk)
    serializer = productserializer(data, many=False)
    data.delete()
    return Response(serializer.data)


# Labour API
# View API (GET Method)
@api_view(['GET'])
def lab_view(request):
    datas=Labours.objects.all()
    serializer = labourserializer(datas,many=True)
    return Response(serializer.data)

# Add API (POST Method)
@api_view(["POST"])
def lab_add(request):
    serializer = labourserializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"The data is required"})
    
# Edit API (PUT Method)
@api_view(["PUT"])
def lab_edit(request,pk):
    data=Labours.objects.get(id=pk)
    serializer = labourserializer(data,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"Enter the data"})
    
# Delete API (DELETE Method)
@api_view(["DELETE"])
def lab_delete(request,pk):
    data =Labours.objects.get(id=pk)
    serializer = labourserializer(data, many=False)
    data.delete()
    return Response(serializer.data)


# Supplier API
# View API (GET Method)
@api_view(['GET'])
def sup_view(request):
    datas=Suppliers.objects.all()
    serializer = supplierserializer(datas,many=True)
    return Response(serializer.data)

# Add API (POST Method)
@api_view(["POST"])
def sup_add(request):
    serializer = supplierserializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"The data is required"})
    
# Edit API (PUT Method)
@api_view(["PUT"])
def sup_edit(request,pk):
    data=Suppliers.objects.get(id=pk)
    serializer = supplierserializer(data,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"Enter the data"})
    
# Delete API (DELETE Method)
@api_view(["DELETE"])
def sup_delete(request,pk):
    data =Suppliers.objects.get(id=pk)
    serializer = supplierserializer(data, many=False)
    data.delete()
    return Response(serializer.data)


# Supplier API
# View API (GET Method)
@api_view(['GET'])
def sal_view(request):
    datas=Salesreport.objects.all()
    serializer = salesreportserializer(datas,many=True)
    return Response(serializer.data)

# Add API (POST Method) 
@api_view(["POST"])
def sal_add(request):
    serializer = salesreportserializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"The data is required"})
    
# Edit API (PUT Method)
@api_view(["PUT"])
def sal_edit(request,pk):
    data=Salesreport.objects.get(id=pk)
    serializer = salesreportserializer(data,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response({"data":"Enter the data"})
    
# Delete API (DELETE Method)
@api_view(["DELETE"])
def sal_delete(request,pk):
    data =Salesreport.objects.get(id=pk)
    serializer = salesreportserializer(data, many=False)
    data.delete()
    return Response(serializer.data)