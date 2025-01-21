# Definitely Not Reddit (DNR) Backend 

This documentation covers the backend part of the project built with Django,  Django Rest Framework and React.<br>

[Tthe Frontend can be found here:](https://github.com/Salerys/frontend)

[The deployed API can be found here!](https://ppt5-social-media-app-frontend-816a29351b29.herokuapp.com)

# Introduction

This is the 5th Portfolio Project for the Code Institute course, with AdvFE chosen.

[For the full introduction please check the Frontend part:](https://github.com/Salerys/frontend)

<br>

## Use Case

[For the use case please visit the Frontend part.](https://github.com/Salerys/frontend)

## User Experience

[Please visit the Frontend part linked above to find the corresponding details.](https://github.com/Salerys/frontend)

## Agile Project Management

[See the frontend documentation](https://github.com/Salerys/frontend)

## API Endpoints

This application offers the following API endpoints with the displayed CRUD functionality.



| API Endpoint                                  | Method | CRUD Functionality                                  |
| --------------------------------------------- | ------ | --------------------------------------------------- |
| `/user-activity/<str:username>/`              | GET    | Read (Retrieve user activity based on username)     |
| `/posts/<int:post_id>/vote/`                  | POST   | Create (Vote on a post)                             |
| `/posts/delete/all/`                          | DELETE | Delete (Delete all posts)                           |
| `/post/create/`                               | POST   | Create (Create a new post)                          |
| `/post/<int:post_id>/update/`                 | PUT    | Update (Edit an existing post)                      |
| `/posts/`                                     | GET    | Read (Retrieve a list of posts)                     |
| `/posts/<int:pk>/`                            | GET    | Read (Retrieve a specific post by ID)               |
| `/comments/<int:pk>/`                         | GET    | Read (Retrieve a specific comment by ID)            |
| `/comments/<int:post_id>/create/`             | POST   | Create (Create a new comment on a specific post)    |
| `/comments/<int:post_id>/<int:comment_id>/vote/` | POST   | Create (Vote on a specific comment)                 |
| `/comments/<int:post_id>/update/<int:comment_id>/` | PUT    | Update (Edit an existing comment)                   |
| `/comments/<int:post_id>/delete/<int:comment_id>/` | DELETE | Delete (Delete a specific comment)                  |
| `/post/<int:pk>/delete/`                      | DELETE | Delete (Delete a specific post)                     |
| `/profile/<int:pk>`                           | GET    | Read (Retrieve a user's profile by ID)              |
| `/search/`                                    | GET    | Read (Search posts based on query)                  |
| `/admin/`                                     | GET    | (Django admin)                                      |
| `/api/user/register/`                         | POST   | Create (Register a new user)                        |
| `/api/user/<int:pk>/delete/`                  | DELETE | Delete (Delete a specific user by ID)               |
| `/api/user/<int:pk>/edit/`                    | PUT    | Update (Edit a user's information)                  |
| `/api/user/<int:pk>/change-password/`         | POST   | Update (Change a user's password)                   |
| `/api/token/`                                 | POST   | Create (Generate an authentication token)           |
| `/api/csrf-token/`                            | GET    | Read (Retrieve CSRF token)                          |
| `/api/token/refresh/`                         | POST   | Create (Refresh authentication token)               |


## Development

### Technologies Used

#### Languages

The following languages have been used.<br>

- Python

#### Frameworks

The following frameworks have been used.<br>

- Django
- Django Rest Framework
- React

#### Modules, Libraries & Plugins

The following modules, libraries and plugins have been used.<br>

- asgiref                          (ASGI server interface for Django)
- dj-database-url                  (Database URL parser for Django settings)
- Django                           (Web framework for Python)
- django-cors-headers              (CORS handling for Django)
- djangorestframework              (Toolkit for building Web APIs in Django)
- djangorestframework-simplejwt    (JWT authentication for Django REST Framework)
- gunicorn                         (WSGI HTTP Server for Python web applications)
- packaging                        (Utilities for packaging and distributing Python packages)
- pillow                           (Python Imaging Library for image processing)
- psycopg2-binary                  (PostgreSQL adapter for Python)
- PyJWT                            (JWT encoding and decoding library)
- python-dotenv                    (Library to manage environment variables in Python)
- pytz                             (World timezone definitions for Python)
- sqlparse                         (SQL parsing library)
- typing_extensions                (Backport of new type hinting features)
- tzdata                           (Timezone database for Python)
- whitenoise                       (Static file serving for Django applications)


#### Programs & Tools

During the development of this application, the following programs and tools have been used.<br>

- [Heroku Database](https://www.heroku.com) (Used for database hosting)
- [Git](https://git-scm.com/) (Version control)
- [GitHub](https://github.com/) (Used as cloud repository)
- [Heroku](https://www.heroku.com/home) (Deployment of final application)
- [Bruno](https://www.usebruno.com) (For API testing)
- [Visual Studio Code](https://code.visualstudio.com/) (IDE - Integrated Development Environment)
