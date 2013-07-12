try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Another Project for ex 45 of LPTHW r2.0',
    'author': 'Some Fine Project',
    'url': 'URL to get it at.',
    'download_url': 'asdfasdfasdfasfd.com',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['somefineproj'],
    'scripts': ['bin/runner.py'],
    'name': 'somefineproj'
}

setup(**config)

