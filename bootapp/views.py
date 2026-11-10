from django.shortcuts import render

# Create your views here.
def starter_page(request):
    return render(request,'starter-page.html')
def pricing(request):
    return render(request,'pricing.html')
def get_a_quote(request):
    return render(request,'get-a-quote.html')
def contact(request):
    return render(request,'contact.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def service_details(request):
    return render(request,'service-details.html')
