AUTHOR = 'Sergiy Ryabukha'
SITENAME = 'Personal Page'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'mailto:s.ryabukha@gmail.com', 's.ryabukha@gmail.com'),
        ('github', 'https://github.com/ryabukha', 'github.com/ryabukha'),
        ('telegram', 'https://t.me/serg_ryabukha', 'serg_ryabukha'))

DEFAULT_PAGINATION = False
THEME = "theme"
THEME_STATIC_DIR = 'static'
TEMPLATE_PAGES = {
    'pages/books.html': 'books.html',
    'pages/index.html': 'index.html',
    'pages/cv.html': 'cv.html',
    'pages/contact.html': 'contact.html',
    'pages/error.html': 'error.html',
}

MENUITEMS = (
    ('home', '/'),
    ('cv', '/cv.html'),
    ('books', '/books.html'),
    ('contact', '/contact.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
