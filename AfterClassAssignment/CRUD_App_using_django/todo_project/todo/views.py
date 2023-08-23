from django.shortcuts import render, get_object_or_404,redirect
from .models import Todo
from .Forms import TodoForm
def todo_list(request):
    # Assuming todos is your JSON data list
    todos = Todo.objects.all()
    return render(request, "todo/todo_list.html", {"todos": todos})

def create_todo(request):
    # todos = todos.objects.all()
    if request.method == 'POST':
       form = TodoForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('todo_list')
    else:
        form = TodoForm()
        return render(request,'todo/todo_form.html',{"form":form})

def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})
