from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from django.contrib.auth.decorators import login_required
from .models import User, Habit, Record
from .forms import HabitForm, RecordForm


def habit_list(request):
    habits = Habit.objects.all()

    return render(request, "habits/habit_list.html", {"habits": habits})


def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    return render(request, "habits/habit_detail.html", {"habit": habit})


def create_habit(request, pk):
    if request.method == 'GET':
        form = HabitForm()

    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect("habit_detail", pk=habit.pk)

    return render(request, "habits/create_habit.html", {"form": form})


def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request == 'GET':
        form = HabitForm(instance=habit)

    else:
        form = HabitForm(instance=habit, data=request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect("habit_detail", pk=habit.pk)

    return render(request, "habits/edit_habit.html", {"habit": habit, "form": form})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)

    if request.mthod == 'POST':
        habit.delete()
        return redirect("habit_list")

    return render(request, "habits/delete_habit.html", {"habit": habit})