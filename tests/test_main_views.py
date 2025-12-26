from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages
from datetime import date
from main.models import Category, Habit, HabitEntry


class HabitListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.other_user = User.objects.create_user(
            username="otheruser",
            password="testpass123"
        )
        self.category = Category.objects.create(
            name="Health",
            color="#ff5722"
        )
        self.habit1 = Habit.objects.create(
            name="Exercise",
            category=self.category,
            user=self.user
        )
        self.habit2 = Habit.objects.create(
            name="Reading",
            category=self.category,
            user=self.other_user
        )

    def test_login_required(self):
        response = self.client.get(reverse('habit:habit-list'))
        self.assertEqual(response.status_code, 302)

    def test_user_can_see_only_own_habits(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse('habit:habit-list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Exercise")
        self.assertNotContains(response, "Reading")


class HabitCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.category = Category.objects.create(
            name="Health",
            color="#ff5722"
        )

    def test_login_required(self):
        response = self.client.get(reverse('habit:habit-create'))
        self.assertEqual(response.status_code, 302)

    def test_create_habit_success(self):
        self.client.login(username="testuser", password="testpass123")

        form_data = {
            'name': 'Morning Run',
            'description': 'Run 5km every morning',
            'category': self.category.id
        }

        response = self.client.post(reverse('habit:habit-create'), data=form_data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Habit.objects.filter(name='Morning Run', user=self.user).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Habit "Morning Run" created successfully!')


class HabitDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.other_user = User.objects.create_user(
            username="otheruser",
            password="testpass123"
        )
        self.category = Category.objects.create(
            name="Health",
            color="#ff5722"
        )
        self.habit = Habit.objects.create(
            name="Exercise",
            category=self.category,
            user=self.user
        )
        self.other_habit = Habit.objects.create(
            name="Other Exercise",
            category=self.category,
            user=self.other_user
        )

    def test_login_required(self):
        response = self.client.get(reverse('habit:habit-delete', kwargs={'pk': self.habit.pk}))
        self.assertEqual(response.status_code, 302)

    def test_delete_own_habit(self):
        self.client.login(username="testuser", password="testpass123")

        response = self.client.post(reverse('habit:habit-delete', kwargs={'pk': self.habit.pk}))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Habit.objects.filter(pk=self.habit.pk).exists())


    def test_cannot_delete_other_user_habit(self):
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse('habit:habit-delete', kwargs={'pk': self.other_habit.pk}))
        self.assertEqual(response.status_code, 404)


class ToggleHabitViewTest(TestCase):
    def setUp(self):
        self.client = Client()
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
            category=self.category,
            user=self.user
        )

    def test_login_required(self):
        response = self.client.post(reverse('habit:toggle-habit', kwargs={'habit_id': self.habit.id}))
        self.assertEqual(response.status_code, 302)

    def test_toggle_habit_creates_entry(self):
        self.client.login(username="testuser", password="testpass123")

        response = self.client.post(reverse('habit:toggle-habit', kwargs={'habit_id': self.habit.id}))

        self.assertEqual(response.status_code, 302)
        entry = HabitEntry.objects.get(habit=self.habit, date=date.today())
        self.assertTrue(entry.completed)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Great job! You completed "Exercise" today!')

    def test_toggle_habit_toggles_existing_entry(self):
        self.client.login(username="testuser", password="testpass123")

        HabitEntry.objects.create(
            habit=self.habit,
            date=date.today(),
            completed=True
        )

        response = self.client.post(reverse('habit:toggle-habit', kwargs={'habit_id': self.habit.id}))

        entry = HabitEntry.objects.get(habit=self.habit, date=date.today())
        self.assertFalse(entry.completed)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), '"Exercise" marked as not completed.')