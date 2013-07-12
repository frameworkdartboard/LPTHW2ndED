try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Enhanced version of my game from Exercise 43',
    'author': 'Eric Kramer',
    'url': 'http://127.0.0.1/',
    'download_url': 'http://127.0.0.1/download',
    'author_email': 'eric.kramer@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47ec3'],
    'scripts': ['bin/ex47ec3runner.py'],
    'name': 'Ex47EC3'
}

setup(**config)

