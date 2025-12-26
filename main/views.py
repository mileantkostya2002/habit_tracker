from datetime import date

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .forms import HabitUpdateForm, HabitCreationForm, CategoryCreateForm
from .models import HabitEntry, Habit, Category
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin


class HabitListView(LoginRequiredMixin, generic.ListView):
    model = Habit
    template_name = 'habits/habit_list_view.html'
    paginate_by = 10
    context_object_name = 'habit_list'

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitCreateView(LoginRequiredMixin, generic.CreateView):
    model = Habit
    form_class = HabitCreationForm
    success_url = reverse_lazy('habit:habit-list')
    template_name = 'habits/habit_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Habit "{form.instance.name}" created successfully!')
        return super().form_valid(form)


class HabitDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Habit
    template_name = 'habits/habit_confirm_delete.html'
    success_url = reverse_lazy('habit:habit-list')

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        habit_name = self.get_object().name
        messages.success(request, f'Habit "{habit_name}" deleted successfully!')
        return super().delete(request, *args, **kwargs)


class HabitUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Habit
    form_class = HabitUpdateForm
    success_url = reverse_lazy('habit:habit-list')
    template_name = 'habits/habit_update.html'

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, f'Habit "{form.instance.name}" updated successfully!')
        return super().form_valid(form)


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('habit:habit-list')
    template_name = 'category/category_form.html'

    def form_valid(self, form):
        messages.success(self.request, f'Category "{form.instance.name}" created successfully!')
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Category
    success_url = reverse_lazy('habit:habit-list')
    template_name = 'category/category_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        category_name = self.get_object().name
        messages.success(request, f'Category "{category_name}" deleted successfully!')
        return super().delete(request, *args, **kwargs)


class ToggleHabitView(LoginRequiredMixin, View):
    def post(self, request, habit_id):
        habit = get_object_or_404(Habit, id=habit_id, user=request.user)
        entry, created = HabitEntry.objects.get_or_create(
            habit=habit,
            date=date.today(),
            defaults={'completed': True}
        )
        if not created:
            entry.completed = not entry.completed
            entry.save()

        if entry.completed:
            messages.success(request, f'Great job! You completed "{habit.name}" today!')
        else:
            messages.info(request, f'"{habit.name}" marked as not completed.')

        return redirect('habit:habit-list')