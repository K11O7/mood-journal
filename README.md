# 📒 Mood Journal

A modern web-based journaling application built with Django that leverages Google's Gemini API to intelligently analyze and display the emotional state of journal entries.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-latest-green.svg)](https://www.djangoproject.com/)

## ✨ Features

- **AI-Powered Mood Analysis**: Utilizes Google Gemini API to automatically detect and display the emotional tone of your journal entries
- **Clean, Modern UI**: Built with Tailwind CSS for a responsive and intuitive user experience
- **Personal Journaling**: Create, read, update, and delete your personal journal entries
- **Mood Insights**: Gain deeper understanding of your emotional patterns through AI-powered sentiment analysis
- **Privacy-Focused**: Your thoughts and feelings remain secure in your personal journal

## 🛠️ Tech Stack

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **AI Integration**: Google Gemini API
- **Database**: SQLite (development) / PostgreSQL (production ready)

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git
- A Google Gemini API key ([Get one here](https://ai.google.dev/))

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/K11O7/mood-journal.git
   cd mood-journal
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   
   Open your browser and navigate to `http://localhost:8000`

## 📖 Usage

1. **Create an Entry**: Write your thoughts and feelings in the journal entry form
2. **AI Analysis**: The Gemini API automatically analyzes your entry and displays the detected mood
3. **View History**: Browse through your past entries and see how your mood has evolved
4. **Edit & Delete**: Manage your entries with full CRUD functionality

## 🎨 Customization

### Tailwind CSS Configuration

The project uses Tailwind CSS for styling. To customize the design:

1. Edit the Tailwind configuration in `tailwind.config.js`
2. Modify the styles in your templates
3. Rebuild the CSS if needed

## 🌐 Deployment

The application is configured for deployment on Render.com (see `render.yaml`). To deploy:

1. Connect your GitHub repository to Render
2. Set environment variables in the Render dashboard
3. Deploy!

For other platforms, ensure you:
- Set `DEBUG=False` in production
- Configure your database settings
- Set up static file serving
- Add your domain to `ALLOWED_HOSTS`

## 🔒 Security Notes

- Never commit your `.env` file or API keys to version control
- Always use environment variables for sensitive data
- Keep your dependencies updated regularly
- Use HTTPS in production

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used
- [Google Gemini API](https://ai.google.dev/) - AI-powered mood analysis
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework

## 📧 Contact

Krish Choukse - [@K11O7](https://github.com/K11O7)

Project Link: [https://github.com/K11O7/mood-journal](https://github.com/K11O7/mood-journal)

---

⭐ If you find this project helpful, please consider giving it a star!
