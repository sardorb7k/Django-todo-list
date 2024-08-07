from django.shortcuts import render, redirect, get_object_or_404
from .models import Todos
from .forms import TodoForm, TodoUpdateForm

def index(request):
    todos = Todos.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    
    return render(request, 'index.html', {'todos': todos, 'form': form})

def update_todo(request, pk):
    todo = get_object_or_404(Todos, pk=pk)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoUpdateForm(instance=todo)
    
    return render(request, 'update_todo.html', {'form': form, 'todo': todo})

def delete_todo(request, pk):
    todo = get_object_or_404(Todos, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'delete_todo.html', {'todo': todo})

def complete_todo(request, pk):
    todo = get_object_or_404(Todos, pk=pk)
    if request.method == 'POST':
        todo.completed = True
        todo.save()
        return redirect('index')
