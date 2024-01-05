# Project Name

[Shorty]

## Description

[Shorty] is a Django-based URL shortening service, inspired by Bitly, that allows users to create shortened versions of long URLs. This project provides a simple and efficient way to generate short links, making it easier to share and manage URLs.

## Features

- **URL Shortening:** Create short and custom URLs for easier sharing.
- **Link Analytics:** Track the number of clicks and other analytics for each shortened URL.
- **Custom Short URLs:** Allow users to customize the short part of the URL.
- **User Authentication:** Secure the service with user accounts and authentication.
- **Admin Panel:** Manage URLs, users, and analytics through the Django admin panel.

## Getting Started

### Prerequisites

- Python 3.
- asgiref==3.7.2
- crispy-tailwind==0.5.0
- Django==5.0.1
- django-crispy-forms==2.1
- sqlparse==0.4.

### Installation

1. Clone the repository:

```bash
git clone [repository URL]
cd [project directory]
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

Visit http://localhost:8000/ in your browser to access the application.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
