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
SOCIAL = (('email', 's.ryabukha@gmail.com'),
        ('github', 'https://github.com/ryabukha'),
        ('telegram', '@serg.ryabukha'))

DEFAULT_PAGINATION = False
THEME = "theme"
TEMPLATE_PAGES = {
    'pages/books.html': 'books.html',
    'pages/index.html': 'index.html',
    'pages/cv.html': 'cv.html',
    'pages/contact.html': 'contact.html',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
