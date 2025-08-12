# Portfolio - Mohammed Kazim Shaikh

A modern, responsive portfolio website built with Django showcasing my skills, projects, and experience in web development.

## 🌟 Features

- **Responsive Design**: Mobile-first approach with Bootstrap integration
- **Contact Form**: Functional contact form with message validation
- **Project Showcase**: Displays key projects with technology stack
- **Skills Section**: Organized display of technical skills
- **Multi-Platform Deployment**: Ready for Render, Vercel, PythonAnywhere
- **Admin Panel**: Django admin for managing contact messages

## 🚀 Live Demo

[Visit Portfolio](https://your-portfolio-url.com) <!-- Update with your actual deployment URL -->

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7, Python 3.11
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Render, Vercel, PythonAnywhere ready
- **Static Files**: WhiteNoise for static file serving

## 📁 Project Structure

```
Portfolio/
├── portfolio/
│   ├── home/                 # Main app
│   │   ├── models.py         # Contact model
│   │   ├── views.py          # Views logic
│   │   └── ...
│   ├── portfolio/            # Project settings
│   │   ├── settings.py       # Django settings
│   │   ├── urls.py          # URL configuration
│   │   └── ...
│   ├── static/              # Static files (CSS, JS)
│   ├── templates/           # HTML templates
│   └── manage.py           # Django management
├── requirements.txt         # Python dependencies
├── Procfile                # Heroku/Render deployment
├── render.yaml             # Render deployment config
├── runtime.txt             # Python version
└── README.md              # This file
```

## ⚡ Quick Start

### Prerequisites

- Python 3.11+
- pip (Python package manager)
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/portfolio.git
   cd portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env file with your settings
   # Set DEBUG=True for development
   ```

5. **Database setup**
   ```bash
   cd portfolio
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser  # Optional: for admin access
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` to view the portfolio.

## 🌐 Deployment

### Render Deployment

1. **Connect GitHub repository** to Render
2. **Use the included `render.yaml`** for automatic configuration
3. **Set environment variables** (SECRET_KEY will be auto-generated)
4. **Deploy** - Render will handle the rest!

### Manual Deployment Steps

1. **Render/Heroku**:
   - Set `RENDER_EXTERNAL_HOSTNAME` or configure via `render.yaml`
   - Database will be auto-provisioned

2. **Vercel**:
   - Set `VERCEL=1` and `VERCEL_URL`
   - Uses in-memory SQLite for stateless deployment

3. **PythonAnywhere**:
   - Set `PA_DOMAIN` to your PythonAnywhere domain
   - Configure static files serving

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Django secret key | Yes |
| `DEBUG` | Debug mode (False for production) | Yes |
| `DATABASE_URL` | Production database URL | No |
| `RENDER_EXTERNAL_HOSTNAME` | Render deployment URL | No |
| `VERCEL_URL` | Vercel deployment URL | No |
| `PA_DOMAIN` | PythonAnywhere domain | No |

## 📧 Contact Form

The portfolio includes a functional contact form that:
- Validates required fields (name, email, message)
- Stores messages in the database
- Provides user feedback via Django messages
- Works in demo mode on Vercel (no database writes)

## 🎨 Customization

### Content Updates
- **Personal Info**: Edit `templates/index.html`
- **Projects**: Update project cards in the template
- **Styling**: Modify `static/css/style.css`
- **Contact Info**: Update social links in footer

### Adding New Sections
1. Update the template in `templates/index.html`
2. Add corresponding CSS in `static/css/style.css`
3. Update navigation menu if needed

## 🔧 Key Features Explained

### Multi-Platform Support
- **Automatic platform detection** in settings.py
- **Flexible database configuration** (SQLite → PostgreSQL)
- **Static files handling** via WhiteNoise

### Security Features
- **Environment-based configuration**
- **CSRF protection** enabled
- **Secure headers** via Django middleware
- **SSL redirect** for production

## 📱 Responsive Design

- Mobile-first CSS approach
- Bootstrap 5 integration
- Custom responsive components
- Cross-browser compatibility

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Mohammed Kazim Shaikh**
- GitHub: [@kazimshaikh07](https://github.com/kazimshaikh07)
- LinkedIn: [kazim-shaikh](https://www.linkedin.com/in/kazim-shaikh)
- Email: kazim.shaikh0@gmail.com

## 🙏 Acknowledgments

- Django framework for the robust backend
- Bootstrap for responsive UI components
- Font Awesome for icons
- Render/Vercel for hosting platforms

---

⭐ **Star this repository** if you found it helpful!
