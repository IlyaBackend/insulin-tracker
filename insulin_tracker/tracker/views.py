from django.shortcuts import render, redirect, get_object_or_404
from .forms import InjectionForm
from django.utils import timezone
from .models import InsulinInjection


def home(request):
    return render(request, 'tracker/home.html')


def add_injection(request):
    '''Добавить запись'''
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


def records_list(request):
    '''Показать последние 5 записей'''
    records = InsulinInjection.objects.all().order_by('-date')[:10]
    return render(request, 'tracker/records_list.html', {'records': records})


def edit_records(request):
    '''Показываем записи для редактирования'''
    records = InsulinInjection.objects.all().order_by('date')
    return render(request, 'tracker/edit_list.html', {'records': records})


def edit_single_record(request, record_id):
    '''Изменить одну запись'''
    record = get_object_or_404(InsulinInjection, id=record_id) # ошибка 404 если запись не найдена
    if request.method == 'POST':
        form = InjectionForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('records_list')
    else:
        form = InjectionForm(instance=record)
    return render(request, 'tracker/edit_form.html', {'form': form})
