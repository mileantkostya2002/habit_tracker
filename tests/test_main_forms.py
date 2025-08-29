from django.test import TestCase
from django.contrib.auth.models import User
from main.models import Category, Habit
from main.forms import HabitUpdateForm, HabitCreationForm, CategoryCreateForm


class HabitUpdateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.category = Category.objects.create(
            name="Health",
            color="#ff5722"
        )
        self.habit = Habit.objects.create(
            name="Exercise",
            description="Daily workout",
            category=self.category,
            user=self.user
        )

    def test_valid_form(self):
        form_data = {
            'name': 'Updated Exercise',
            'description': 'Updated description',
            'category': self.category.id
        }
        form = HabitUpdateForm(data=form_data, instance=self.habit)
        self.assertTrue(form.is_valid())

    def test_invalid_form_empty_name(self):
        form_data = {
            'name': '',
            'description': 'Some description',
            'category': self.category.id
        }
        form = HabitUpdateForm(data=form_data, instance=self.habit)
        self.assertFalse(form.is_valid())

    def test_form_fields(self):
        form = HabitUpdateForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('category', form.fields)

    def test_form_save(self):
        form_data = {
            'name': 'Updated Exercise',
            'description': 'Updated description',
            'category': self.category.id
        }
        form = HabitUpdateForm(data=form_data, instance=self.habit)
        if form.is_valid():
            updated_habit = form.save()
            self.assertEqual(updated_habit.name, 'Updated Exercise')
            self.assertEqual(updated_habit.description, 'Updated description')


class HabitCreationFormTest(TestCase):


    def test_invalid_form_no_category(self):
        form_data = {
            'name': 'Morning Run',
            'description': 'Run 5km every morning'
        }
        form = HabitCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_form_fields(self):
        form = HabitCreationForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('category', form.fields)

    def test_form_save(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        form_data = {
            'name': 'Morning Run',
            'description': 'Run 5km every morning',
        }
        form = HabitCreationForm(data=form_data)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = user
            habit.save()
            self.assertEqual(habit.name, 'Morning Run')
            self.assertEqual(habit.category, self.category)
            self.assertEqual(habit.user, user)


class CategoryCreateFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Work',
            'color': '#4caf50'
        }
        form = CategoryCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_fields(self):
        form = CategoryCreateForm()
        self.assertIn('name', form.fields)
        self.assertIn('color', form.fields)


