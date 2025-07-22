from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cqdpq1$dvw#)c=yzrxz2y39q1c)pynsr_$62x70&1v%3b5pkby'

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'widget_tweaks',

]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Resume_mng_sys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Resume_mng_sys.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'resume_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/


STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'myapp.CustomUser'
LOGIN_URL = 'login'  # Already present – default login URL
LOGIN_REDIRECT_URL = 'home'  # login नंतर user ला home वर पाठवा
LOGOUT_REDIRECT_URL = 'home'  # logout नंतर user ला home वर पाठवा

# Email configuration using Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # SMTP backend
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'karpemurli3870@gmail.com'
EMAIL_HOST_PASSWORD = 'iqpu fsdc vzsm dvae'  # App Password (Gmail)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Correct assignment

# JAZZMIN_SETTINGS


JAZZMIN_SETTINGS = {

    # ब्राऊझरच्या टॅबमध्ये दिसणारे नाव (जर दिले नसेल तर डिफॉल्ट admin site_title वापरले जाईल)
    "site_title": "Job Portal",

    # लॉगिन स्क्रीनवर दिसणारे शीर्षक (19 अक्षरे मर्यादा)
    "site_header": "JobBoard",

    # डाव्या वरच्या कोपऱ्यात ब्रँड म्हणून दिसणारे नाव
    "site_brand": "JobBoard",

    # वेबसाईटचा लोगो (static फोल्डरमध्ये असावा, वरच्या डाव्या कोपऱ्यात दिसतो)

    "site_logo": "images/M.png",

    # लॉगिन फॉर्मसाठी लोगो (जर दिला नसेल तर वरचा `site_logo` वापरतो)

    "login_logo": "images/M.png",

    # डार्क थीम लॉगिन फॉर्मसाठी लोगो (जर दिला नसेल तर `login_logo` वापरतो)
    "login_logo_dark": None,

    # लोगोला दिले जाणारे CSS वर्ग (class) – इथे 'img-circle' म्हणजे गोल लोगो
    "site_logo_classes": "img-circle",

    # favicon (टॅबमध्ये लहान चिन्ह) – दिलं नसेल तर `site_logo` वापरतो
    "site_icon": "images/M.png",

    # लॉगिन स्क्रीनवर स्वागत संदेश
    "welcome_sign": "Welcome to the JobBoard Admin Panel 👋",

    # पायथ्याशी (footer) दिसणारे कॉपीराइट
    "copyright": "© 2025 MyApp Solutions Pvt. Ltd.",

    # सर्च बारमध्ये शोधता येणारे मॉडेल्स
    "search_model": ["auth.User", "myapp.Job", "myapp.Application"],

    # वरच्या मेनूतील दुवे (top menu)
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},  # मुख्य पानासाठी
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        # बाह्य लिंक
        {"model": "auth.User"},  # User मॉडेल पृष्ठासाठी
        {"app": "books"},  # 'books' app चे सर्व मॉडेल्स
    ],

    # उजव्या कोपऱ्यातील युजर मेनू लिंक
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    # साइडबार (डावी बाजू) दर्शवायचा का?
    # "show_sidebar": True,

    # साइड मेनू आपोआप विस्तारित करायचा का?
    # "navigation_expanded": True,

    # अ‍ॅप्स/मॉडेल्ससाठी खास चिन्हे (Font Awesome icons)
    "icons": {
        "auth": "fas fa-users-cog",  # auth app साठी
        "auth.user": "fa-solid fa-face-smile",  # User मॉडेलसाठी
        "auth.Group": "fas fa-users",  # Group मॉडेलसाठी
    },

    # UI customizer (बाजूला रंग व theme बदलायचा पर्याय) दर्शवायचा का?
    "show_ui_builder": True,

    # Admin फॉर्म कसा दिसेल? 'vertical_tabs' म्हणजे फील्ड टॅब्समध्ये
    "changeform_format": "vertical_tabs",
}

JAZZMIN_UI_TWEAKS = {

    "theme": "cerulean  ",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-light",
    "accent": "accent-navy",
    "navbar": "navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-orange",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "cosmo",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}