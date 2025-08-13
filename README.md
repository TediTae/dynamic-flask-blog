# TediTae's Flask Blog

A dynamic Flask blog fetching posts from an external API, demonstrating web development skills using Python, Flask, Jinja2, and Bootstrap.

## Features
- **Dynamic Web Application** built with Flask
- **API-driven Posts** using the `requests` module
- **Dynamic URL routing** for individual blog posts (`/post/<id>`)
- **Jinja2 Templating** for rendering dynamic content
- **Responsive Design** with Bootstrap 5
- **Reusable Templates**: Header and Footer are separate files (`header.html`, `footer.html`) and included in all pages

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/flask-blog.git
cd flask-blog
pip install -r requirements.txt
python main.py
```
---

- Open your browser and go to http://127.0.0.1:5000.
    - ⚠️ Note: debug=True is set for development purposes. Remember to disable it in production.

---

## Usage
- Home page lists all blog posts dynamically
- Clicking a post navigates to the Post Detail Page
- Post Detail Page shows title, subtitle, author, date, image, and content
- Fully responsive layout ensures optimal reading experience on all devices

---

## Page Overview
### Home Page
- Lists all blog posts with title, subtitle, author, and date
- Each post links to its detail page
- Clean, modern, and responsive design

---

### Post Detail Page
- Displays the selected post with title, subtitle, author, date, image, and full content
- Dynamic header image (post.image_url) enhances visual appeal
- Single-column readable layout for better user experience

---

## Technologies
- Python 3.x
- Flask
- Jinja2
- Bootstrap 5
- Requests
- HTML / CSS / JavaScript

---

## License
- MIT License

---

## Contact
- tolgayilmaz1377@gmail.com
