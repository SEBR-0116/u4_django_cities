INSTALLED_APPS = [
    #...,
    'cities_app',
    'rest_framework'
]

# Insert btwn Installed_Apps & Middleware
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]

    # use this instead if you're getting 401 or 500 erros:
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.AllowAny',
    # ]
}

# edit existing to look like:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cities_app',
        'USER': 'cityuser',
        'PASSWORD': 'password',
        'HOST': 'localhost'
    }
}

# add when connecting Front End / Cors
#   -> restricts which sites can access this shit
# CORS_ALLOWED_ORIGINS = [
#     "https://example.com",
#     "https://sub.example.com",
#     "http://localhost:5173",
#     "http://127.0.0.1:5555", # but use real ones
# ]

# can use while working w a number of pages/local hosts, & when info doesn't need to be set as secure
#CORS_ALLOW_ALL_ORIGINS = True

# alt if errors w ^ or ^^
# CSRF_TRUSTED_ORIGINS = [
#     "http://localhost:5173" # example
# ]