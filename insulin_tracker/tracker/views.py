from django.shortcuts import render, redirect
from .forms import InjectionForm
from django.utils import timezone



def add_injection(request):
    if request.method == 'POST':
        form = InjectionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.date = timezone.now()
            instance.save()
            return redirect('add_injection') # обновляет страницу, избегает повторной отправки формы
    else:
        form = InjectionForm()
    return render(request, 'tracker/add_injection.html', {'form': form})