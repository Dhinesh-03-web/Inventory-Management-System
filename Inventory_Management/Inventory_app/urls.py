"""
URL configuration for Inventory_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_page, name=''),
    path('logout', views.logout_page, name='logout'),
    path('dashboard/',views.Dashboard, name='dashboard'),
    path('category/',views.CategoryViews, name='category'),
    path('editlabour/<int:id>',views.EditLabour, name='editlabour'),
    path('editproduct/<int:id>',views.EditProduct, name='editproduct'),
    path('editcategory/<int:id>',views.EditCategory, name='editcategory'),
    path('editsupplier/<int:id>',views.EditSupplier, name='editsupplier'),
    path('managelabour/',views.ManageLabour, name='managelabour'),
    path('manageproduct/',views.ProductManage, name='manageproduct'),
    path('managesupplier/',views.ManageSupplier, name='managesupplier'),
    path('newlabour/',views.NewLabour, name='newlabour'),
    path('newcategory/',views.NewCategory, name='newcategory'),
    path('newproduct/',views.NewProduct, name='newproduct'),
    path('newsupplier/',views.NewSupplier, name='newsupplier'),
    path('salesreport/',views.SalesReport, name='salesreport'),
    path('settings/',views.SettingsViews, name='settings'),
    path('settingsedit/<int:id>',views.SettingsEditView, name='settingsedit'),
    path('delete_labour/<int:id>', views.delete_labour, name="delete_labour"),
    path('delete_category/<int:id>', views.delete_category, name="delete_category"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"),
    path('delete_supplier/<int:id>', views.delete_supplier, name="delete_supplier"),
    path('delete_sales_report/<int:id>', views.delete_sales_report, name="delete_sales_report"),
    
    # api urls
    path('cat_view/', views.cat_view, name='cat_view'),
    path('pro_view/', views.pro_view, name='pro_view'),
    path('lab_view/', views.lab_view, name='lab_view'),
    path('sup_view/', views.sup_view, name='sup_view'),
    path('sal_view/', views.sal_view, name='sal_view'),
    path('cat_add/', views.cat_add, name='cat_add'),
    path('pro_add/', views.pro_add, name='pro_add'),
    path('lab_add/', views.lab_add, name='lab_add'),
    path('sup_add/', views.sup_add, name='sup_add'),
    path('sal_add/', views.sal_add, name='sal_add'),
    path('cat_edit/<int:pk>', views.cat_edit, name='cat_edit'),
    path('pro_edit/<int:pk>', views.pro_edit, name='pro_edit'),
    path('lab_edit/<int:pk>', views.lab_edit, name='lab_edit'),
    path('sup_edit/<int:pk>', views.sup_edit, name='sup_edit'),
    path('sal_edit/<int:pk>', views.sal_edit, name='sal_edit'),
    path('cat_delete/<int:id>', views.cat_delete, name='cat_delete'),
    path('pro_delete/<int:pk>', views.pro_delete, name='pro_delete'),
    path('lab_delete/<int:pk>', views.lab_delete, name='lab_delete'),
    path('sup_delete/<int:pk>', views.sup_delete, name='sup_delete'),
    path('sal_delete/<int:pk>', views.sal_delete, name='sal_delete'),
]
