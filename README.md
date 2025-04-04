# Django + Vue (Vite) Boilerplate for Heroku

## Introduction
This is a full-stack boilerplate designed for deployment on Heroku. The frontend is built using Vue 3 with Vite, while the backend is implemented with Django Rest Framework. Supabase is used for database. This setup provides a solid foundation for developing and deploying full-stack applications efficiently.

The site already includes a user registration and login system.

## Getting Started

### Setting Up the Environment
1. Clone the repository
   
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install backend dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Install frontend dependencies:
   ```sh
   cd front
   npm install
   ```

### Default Development Configuration
- The project is initially set up for development.
- The `.env` file starts with `DJANGO_ENV=development`.
- The API endpoints start empty.
- `DEBUG` is set to `True`.

## Running in Development Mode

### Running the Backend
1. Navigate to the backend directory:
   ```sh
   cd ../back
   ```
2. Apply migrations and run the server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

### Running the Frontend
1. Navigate to the frontend directory:
   ```sh
   cd ../front
   ```
2. Start the development server:
   ```sh
   npm run dev
   ```

The Vue app should now be running on `http://localhost:5173` (default Vite port), and the Django API should be available on `http://127.0.0.1:8000`. To develop you must use `http://127.0.0.1:8000`

## Switching Between Development and Production

If you need to switch between development and production, make sure you update your database connection settings in `settings.py`.

### Default SQLite for Local Development:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Connect to Supabase (Production Database):
Uncomment the following block and replace the placeholders with your Supabase credentials:

```python
# DATABASES = {
#     'default': {  
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': '<your-db-user>',
#         'PASSWORD': '<your-db-password>',
#         'HOST': '<your-db-host>',
#         'PORT': '5432',  
#         'OPTIONS': {
#             'gssencmode': 'disable',
#             'sslmode': 'require',  # Use SSL for the connection
#             'options': '-c statement_timeout=30000 -c krbsrvname=postgres',
#         },
#     }
# }
```

Make sure to comment out the SQLite block and uncomment the PostgreSQL block when switching to production.

## Deploying to Production on Heroku

### Preparing for Deployment
1. Login to Heroku:
   ```sh
   heroku login
   ```
2. Create a new Heroku app:
   ```sh
   heroku create your-app-name
   ```
3. Add the required buildpacks:
   ```sh
   heroku buildpacks:add heroku/python
   ```
4. Set up the `.env` file for production:
   - Change `DJANGO_ENV=development` to `DJANGO_ENV=production`.
   - SET `DEBUG=False` in  `settings.py`.
   - Specify the Python version in `runtime.txt`:
     ```sh
     echo "python-3.x.x" > runtime.txt
     ```
5. Build the front end
    ```sh
    cd front
    npm run build
    ```
### Deploying
1. Commit all changes:
   ```sh
   git add .
   git commit -m "Deploying to Heroku"
   ```
2. Push to Heroku:
   ```sh
   git push heroku main
   ```
3. Important: Initially, the application will not work because the base API endpoint is not set correctly.
    Set the base API endpoints to match the Heroku app URL.
    The endpoints file is located in `front/common/endpoints.js`
    After updating the endpoint, commit the changes and push again:
    ```sh
    git add .  
    git commit -m "Updated API base endpoint"  
    git push heroku main  
     ```

## Switching Between Production and Development

### From Production to Development
- Update the `.env` file and change `DJANGO_ENV=production` to `DJANGO_ENV=development`.
- Set `DEBUG` to `True`.
- Set `baseEndpoint = ""`in `front/common/endpoints.js`
- Restart the Django server if it is running

### From Development to Production
- Ensure all features work locally.
- Update the `.env` file and change `DJANGO_ENV=development` to `DJANGO_ENV=production`.
- Set `DEBUG` to `False`.
- Set the base API endpoints to match the Heroku app URL.
- Build the front end
- Commit the changes and push again on git.



## Additional Notes
- Whenever you want to change something in the front-end, if you apply these changes in development mode you have to rebuild the Vue project:
    ```sh
    cd front
    npm run build
    ```
- Ensure Heroku Dynos are correctly allocated.
- Use `heroku logs --tail` for debugging deployment issues.
- It's already present a user to login in the platform: `username = admin, password = admin`, you can manage users by goint to `/admin` route.

Enjoy building with Django and Vue on Heroku!

