# Simple Habits 🌟

> **Build Your Future One Habit at a Time**

A minimalist, modern web application for tracking daily habits and building better routines. Built with Django and designed with simplicity and user experience in mind.

[Visit my website](https://habit-tracker-m3j0.onrender.com/habits/)

---

You can test my website:
Username: test_user
Password: user1234

## ✨ Features

### 🎯 **Core Functionality**
- **One-Click Tracking** - Mark habits as complete with a single click
- **Smart Statistics** - Current streaks, completion rates, and total progress
- **Custom Categories** - Organize habits with color-coded categories
- **Progress Analytics** - 30-day completion rates and visual feedback

### 🔐 **User Management**
- **Secure Authentication** - Registration, login, and logout system
- **Personal Data** - Each user sees only their own habits
- **Profile Management** - Email-based user accounts

### 🎨 **Modern Design**
- **Minimalist Interface** - Clean, distraction-free design
- **Responsive Layout** - Works perfectly on desktop and mobile
- **Smooth Animations** - Subtle hover effects and transitions
- **Elegant Typography** - Modern system fonts for readability

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/simple-habits.git
   cd simple-habits
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django==5.2.5
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:8000
   ```

---


```

---

## 🛠️ Technology Stack

| Component | Technology   | Purpose |
|-----------|--------------|---------|
| **Backend** | Django 5.2.5 | Web framework |
| **Database** | Postgres     |
| **Frontend** | HTML5, CSS3  | User interface |
| **Authentication** | Django Auth  | 
| **Styling** | Custom CSS   | Modern design |

---

## 🎨 Design Philosophy

### Minimalism First
- **Clean Interface** - No clutter, only essential elements
- **Purposeful Color** - Black and white with strategic accent colors
- **Typography Focus** - System fonts for optimal readability

### User Experience
- **Intuitive Navigation** - Clear information hierarchy
- **Instant Feedback** - Immediate visual confirmation of actions
- **Progressive Enhancement** - Works without JavaScript

### Performance
- **Lightweight** - Minimal dependencies and optimized assets
- **Fast Loading** - Efficient queries and caching strategies
- **Mobile Optimized** - Responsive design for all devices

```

```

---

## 🔧 Configuration

```


```

---

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up proper database (PostgreSQL recommended)
- [ ] Configure static file serving
- [ ] Set up HTTPS
- [ ] Configure email backend
- [ ] Set up monitoring and logging

### Quick Deploy with Heroku
```bash
# Install Heroku CLI and login
pip install gunicorn
echo "web: gunicorn config.wsgi" > Procfile
git add .
git commit -m "Deploy to Heroku"
heroku create habit_tracker
git push heroku main
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit changes** (`git commit -m 'Add amazing feature'`)
4. **Push to branch** (`git push origin feature/amazing-feature`)
5. **Open Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Django Community** - For the excellent web framework
- **Modern CSS** - Inspired by contemporary design trends
- **Minimalist Design** - Influenced by Apple's design philosophy
- **Habit Science** - Based on behavioral psychology research

---

## 📞 Contact

- **GitHub**: [@mileantkostya2002](https://github.com/mileantkostya2002)
- **Email**: kostya.m.2002@gmail.com


---

