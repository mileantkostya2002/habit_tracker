from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta
from main.models import Category, Habit, HabitEntry


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Health",
            color="#ff5722"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Health")
        self.assertEqual(self.category.color, "#ff5722")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Health")

    def test_category_default_color(self):
        category = Category.objects.create(name="Work")
        self.assertEqual(category.color, "#007bff")


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )
        self.category = Category.objects.create(
            name="Health",
            color="#ff5722"
        )
        self.habit = Habit.objects.create(
            name="Morning Exercise",
            description="30 minutes of exercise",
            category=self.category,
            user=self.user
        )

    def test_habit_creation(self):
        self.assertEqual(self.habit.name, "Morning Exercise")
        self.assertEqual(self.habit.description, "30 minutes of exercise")
        self.assertEqual(self.habit.category, self.category)
        self.assertEqual(self.habit.user, self.user)
        self.assertTrue(self.habit.is_active)

    def test_habit_str(self):
        expected = f'{self.habit.name} - {self.user.username}'
        self.assertEqual(str(self.habit), expected)

    def test_get_absolute_url(self):
        self.assertEqual(self.habit.get_absolute_url(), reverse('habit:habit-list'))

    def test_is_completed_today_false(self):
        self.assertFalse(self.habit.is_completed_today())

    def test_is_completed_today_true(self):
        HabitEntry.objects.create(
            habit=self.habit,
            date=date.today(),
            completed=True
        )
        self.assertTrue(self.habit.is_completed_today())

    def test_get_current_streak_zero(self):
        self.assertEqual(self.habit.get_current_streak(), 0)

    def test_get_current_streak_with_entries(self):
        today = date.today()
        for i in range(3):
            HabitEntry.objects.create(
                habit=self.habit,
                date=today - timedelta(days=i),
                completed=True
            )
        self.assertEqual(self.habit.get_current_streak(), 3)

    def test_get_total_completed_days(self):
        today = date.today()
        HabitEntry.objects.create(
            habit=self.habit,
            date=today,
            completed=True
        )
        HabitEntry.objects.create(
            habit=self.habit,
            date=today - timedelta(days=1),
            completed=False
        )
        HabitEntry.objects.create(
            habit=self.habit,
            date=today - timedelta(days=2),
            completed=True
        )

        self.assertEqual(self.habit.get_total_completed_days(), 2)

    def test_get_completion_rate(self):
        today = date.today()
        for i in range(5):
            completed = i < 3
            HabitEntry.objects.create(
                habit=self.habit,
                date=today - timedelta(days=i),
                completed=completed
            )

        rate = self.habit.get_completion_rate(days=10)
        self.assertEqual(rate, 30.0)


class HabitEntryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )
        self.category = Category.objects.create(
            name="Health",
            color="#ff5722"
        )
        self.habit = Habit.objects.create(
            name="Morning Exercise",
            description="30 minutes of exercise",
            category=self.category,
            user=self.user
        )
        self.entry = HabitEntry.objects.create(
            habit=self.habit,
            date=date.today(),
            notes="Did 30 pushups and ran 2km",
            completed=True
        )

    def test_habit_entry_creation(self):
        self.assertEqual(self.entry.habit, self.habit)
        self.assertEqual(self.entry.date, date.today())
        self.assertEqual(self.entry.notes, "Did 30 pushups and ran 2km")
        self.assertTrue(self.entry.completed)

    def test_habit_entry_str(self):
        expected = f"{self.habit.name} - {date.today()} ✅"
        self.assertEqual(str(self.entry), expected)

    def test_habit_entry_str_not_completed(self):
        entry = HabitEntry.objects.create(
            habit=self.habit,
            date=date.today() - timedelta(days=1),
            completed=False
        )
        expected = f"{self.habit.name} - {date.today() - timedelta(days=1)} ❌"
        self.assertEqual(str(entry), expected)

    def test_habit_entry_default_completed(self):
        entry = HabitEntry.objects.create(
            habit=self.habit,
            date=date.today() - timedelta(days=1)
        )
        self.assertFalse(entry.completed)

    def test_unique_together_constraint(self):
        with self.assertRaises(Exception):
            HabitEntry.objects.create(
                habit=self.habit,
                date=date.today(),
                completed=False
            )