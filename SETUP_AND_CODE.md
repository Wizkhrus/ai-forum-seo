# AI Forum SEO - Complete Setup Guide

## Quick Start

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your-api-key-here
python app.py
```

Visit http://localhost:5000 and admin at http://localhost:5000/admin

## Features
- 120+ AI-generated unique users
- SEO-optimized forum structure with slug URLs
- Automatic content generation every 30 minutes
- Admin panel for managing posts and dates
- Realistic post dates spanning 3 years
- 6 themed categories with 6+ topics each

## File Structure

ai-forum-seo/
├── app.py (Flask application)
├── database.py (SQLAlchemy models)
├── ai_generator.py (OpenAI content generation)
├── config.py (Configuration)
├── requirements.txt (Dependencies)
└── templates/ (HTML templates)
    ├── base.html (Main template with SEO)
    ├── index.html (Homepage)
    ├── category.html (Category page)
    └── thread.html (Thread page)
