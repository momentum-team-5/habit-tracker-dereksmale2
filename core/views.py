from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from django.contrib.auth.decorators import login_required
from .models import Habit, Record
from .forms import HabitForm, RecordForm, SearchForm


def habit_list(request):
    habits = Habit.objects.all()

    return render(request, "habit_list.html", {"habits": habits})


def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    return render(request, "habit_detail.html", {"habit": habit})


@login_required
def create_habit(request):
    if request.method == 'GET':
        form = HabitForm()

    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect("habit_detail", pk=habit.pk)

    return render(request, "create_habit.html", {"form": form})


@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request == 'GET':
        form = HabitForm(instance=habit)

    else:
        form = HabitForm(instance=habit, data=request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect("habit_detail", pk=habit.pk)

    return render(request, "edit_habit.html", {"habit": habit, "form": form})


@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.method == 'POST':
        habit.delete()
        return redirect("habit_list")

    return render(request, "delete_habit.html", {"habit": habit})


@login_required
def record_list(request):
    records = Record.objects.all()

    return render(request, "record_list.html", {"records": records})


@login_required
def create_record(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == 'GET':
        form = RecordForm()
        
    else:
        form = RecordForm(data=request.POST)
    
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            return redirect(to='habit_list')

    return render(request, "create_record.html", {"form": form, "habit": habit})


@login_required
def edit_record(request, pk):
    record = get_object_or_404(Record.objects.filter(habit__user=request.user), pk=pk)

    if request == 'GET':
        form = RecordForm(instance=record)

    else:
        form = RecordForm(instance=record, data=request.POST)
        if form.is_valid():
            record = form.save()
            return redirect("habit_detail", pk=record.pk)

    return render(request, "edit_record.html", {"record": record, "form": form})


@login_required
def delete_record(request, pk):
    record = get_object_or_404(Record.objects.filter(habit__user=request.user), pk=pk)

    if request.method == 'POST':
        record.delete()
        return redirect("habit_list")

    return render(request, "delete_record.html", {"record": record})


def search(request):
    if request.method == "GET":
        form = SearchForm()

    elif request.method == "POST":
        form = SearchForm(data=request.POST)

    if form.is_valid():
        habit = form.cleaned_data['habit']
        habit = Habit.objects.filter(habit__contains=habit)

        return render(request, "search_results.html", {"habit": habit})

    return render(request, "search.html", {"form": form})