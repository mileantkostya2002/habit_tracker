from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta

class Category(models.Model):
    color = models.CharField(max_length=20, default='#007bff')
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Habit(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated')
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')

    def __str__(self):
        return f'{self.name} - {self.user.first_name}'

    def get_absolute_url(self):
        return reverse('habit_detail', kwargs={'pk': self.pk})

    def get_current_streak(self):
        streak = 0
        current_date = date.today()

        while True:
            try:
                entry = self.entries.get(date=current_date)
                if entry.completed:
                    streak += 1
                    current_date -= timedelta(days=1)
                else:
                    break
            except HabitEntry.DoesNotExist:
                break
            return streak

    def get_total_completed_days(self):
        return self.entries.filter(completed=True).count()

    def is_completed_today(self):
        try:
            today_entry = self.entries.get(date=date.today())
            return today_entry.completed
        except HabitEntry.DoesNotExist:
            return False

    def get_completion_rate(self, days=30):
        end_date = date.today()
        start_date = end_date - timedelta(days=days - 1)

        total_days = days
        completed_days = self.entries.filter(
            date__range=[start_date, end_date],
            completed=True
        ).count()

        if total_days == 0:
            return 0

        return round((completed_days / total_days) * 100, 1)


class HabitEntry(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, verbose_name='habits', related_name='entries')
    date = models.DateField(verbose_name='Date')
    notes = models.TextField(blank=True, verbose_name='Notes')
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['habit', 'date']
        ordering = ['-date']
        verbose_name = 'Habit entry'
        verbose_name_plural = 'Habit entries'

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{self.habit.name} - {self.date} {status}"

