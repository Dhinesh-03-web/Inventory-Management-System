from django.db import models
    
class Category(models.Model):
    cat_name=models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.cat_name

class Product(models.Model):
    cat_name=models.ForeignKey(Category, on_delete=models.CASCADE)    
    product_name=models.CharField(max_length=50, null=False, blank=False)
    in_stock=models.IntegerField(null=True, blank=True)
    min_stock=models.IntegerField(null=True, blank=True)

class Labours(models.Model):
    lab_name=models.CharField(max_length=50, null=False, blank=False)
    phone_no=models.BigIntegerField(null=True, blank=True)
    salary=models.IntegerField(null=True, blank=True)

class Suppliers(models.Model):
    company_name=models.CharField(max_length=50, null=False, blank=False)
    supplier_name=models.CharField(max_length=50, null=False, blank=False)
    phone_number=models.IntegerField(null=True, blank=True)
    company_address=models.CharField(max_length=100, null=False, blank=False)
    total_purchase=models.IntegerField(null=True, blank=True)
    purchase_due=models.IntegerField(null=True, blank=True)  

class Salesreport(models.Model):
    date=models.DateField(null=False, blank=False)
    amount=models.IntegerField(null=True, blank=True)  

class Settings(models.Model):
    store_name=models.CharField(max_length=100,null=False, blank=False)





