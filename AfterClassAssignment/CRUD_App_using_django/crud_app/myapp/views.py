from django.shortcuts import render,redirect

def create(request):
    # Your code here
    if request.method == 'POST':
        return redirect(request, 'create.html')
    return render(request, 'create.html')

def read(request):
    # Your code here
    tasks = []
    return render(request, 'read.html',{"tasks":tasks})

def update(request):
    # Your code here
    pass

def delete(request):
    # Your code here
    pass
