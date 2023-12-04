from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def submit_form(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        return render(request, 'form.html', {'name':name,'email':email})
    else:
        return render(request, 'form.html')