from .models import Settings  

def my_model_data(request):
    data = Settings.objects.all()  
    return {'my_model_data': data}
