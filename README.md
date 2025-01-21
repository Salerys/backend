# Definitely Not Reddit (DNR) Backend 

This documentation covers the backend part of the project built with Django,  Django Rest Framework and React.<br>

[The Frontend can be found here:](https://github.com/Salerys/frontend)

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
- [dbdiagram.io](https://dbdiagram.io/) (Creating database visualization)
- [Heroku](https://www.heroku.com) (Deployment of final application)
- [Bruno](https://www.usebruno.com) (For API testing)
- [Visual Studio Code](https://code.visualstudio.com/) (IDE - Integrated Development Environment)

### Deployment

#### Version Control

This application was developed using Visual Studio Code as the IDE and GitHub for hosting the repository.<br>
<br>
Git was used for version control by using the following comments:<br>
<br>

- git add filename - Select the files that should be uploaded and updated to the GitHub repository.
- git commit -m "commit message" - Commenting the commit to better understand the changes in this specific commit.
- git push - Upload the commit to GitHub.

#### Database Deployment

The database for this project was deployed with the help of the [Heroku Database](https://heroku.com).

#### Heroku Deployment

**Step 0: Create requirements.txt**

- Create the requirements.txt (pip freeze > requirements.txt)
- Make sure it contains all needed modules and libraries.
- Modify settings.py
  - Add Heroku to ALLOWED_HOSTS
  - Add Frontend adsress to CORS_ALLOWED_ORIGINS
  - Set DEBUG to "False"
- Create Procfile in root directory with the following content: web: gunicorn sessionminds.wsgi --log-file -
- Use python manage.py collectstatic in the local IDE terminal to collect all static files

**Step 1: Use Account**

- Create a Heroku account
- Log into the Heroku account

**Step 2: Create New App**

- On the dashboard, click "New" in the upper right corner.
- Select "Create new app"
- Select a name for the application - the name should only contain lowercase letters, numbers, and dashes.
- Choose a region. (Europe as we are in Europe)

**Step 3: Define Deployment Method**

- Select GitHub as deployment method
- Connect GitHub account to Heroku
- Select account and search for repository
- Connect to found repository

**Step 4: Settings**

- Switch to the settings page (Menu in the top)
- Click on "Reveal Config Vars"
- Fill in the required Key/Value pairs 
- In the next section, click on "Add buildpack"
- If not already selected, add Python.

**Step 5: Deploy Application**

- Switch to the deploy page (Menu in the top)
- Look under manual deployment
- Select a branch to deploy (Main in my case)
- Click "Deploy Branch"

**Step 6: Use App**

- Heroku will then set up the virtual environment with all packages, modules and libraries needed. (This can take some time)
- When Heroku is done with the deployment, click "View" and start to use the
- Use app
  <br>

  ### Database Diagram
![Definitely Not Reddit diagram](/documentation/images/ppt5dia.png/)

 ### Known Unfixed Bugs

- profile pictures aren't shown, as Heroku Database can't work with them. Outer tool such as Cloudinary is to be implemented
- refresh user profile after voting (voting on own posts shown in user Profile changes the vote counter, but the User has to refresh for it to be shown on the Profile)
- sorting by "most popular" doesn't work as intended, sorting doesn't happen
- lack of interface notifications by user actions, such as post edit/delete/ or profile edit/deletion
- refresh token works, but doesn't get called automatically. once the token expires, and the user navigates to "website root address", the token is refreshed. otherwise an error is shown.
- security aspects directly in the settings file, they should be  hidden in the environment variable

### Extra Mention

Regarding the Github repository, there is a "contributor". The contributor is also me, as there was a bit of a mix-up while I was traveling and used the laptop of my sister, who also uses github.
For the project itself it makes no difference, however for the sake of assessing the project, Code Institute Student Care has been informed of the details, please refer to those.


## Credits

### Resources

- All content was written and created by me.<br>
The project was inspired by ideas of my real life friends, and my Code Institute classmates (shown during weekly calls), as well as the famous platform Reddit, although personalized/customized greatly.<br>
- A huge amount of Google searches were done along other sources like Stack , Reddit, Discord and the different documentations for Django, Bootstrap and React were used.<br>


### Acknowledgements

- Thanks to [Dennis Schenkel](https://github.com/DennisSchenkel) for answering my questions and his general layout of the ReadME file.
- Thanks to Kay for they effort as a facilitator of the Code Institute team.
- My great real life friends Thomas and Matthew.
