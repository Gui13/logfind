try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'logfind is an implementation of http://projectsthehardway.com/2015/06/16/project-1-logfind-2/',
    'author': 'Guillaume BIENKOWSKI',
    'url': 'https://github.com/Gui13/logfind',
    'download_url': 'https://github.com/Gui13/logfind',
    'author_email': 'guitreize@ the one from google',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'scripts': [],
    'name': 'logfind'
}

setup(**config)