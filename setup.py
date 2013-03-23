try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'perform division using binary search',
    'author': 'Tom Berry',
    'url': '',
    'download_url': '',
    'author_email': 'tom.berry@me.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['division'],
    'scripts': [],
    'name': 'division'
}

setup(**config)