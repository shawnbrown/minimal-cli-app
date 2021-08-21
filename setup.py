"""A package to demonstrate "scripts" and "data_files" installation."""
from distutils.core import setup


setup(
    name='my-app',
    version='0.1',
    description='A package to demo "scripts" and "data_files" installation.',
    packages=['my_app'],
    scripts=['bin/my-app'],
    data_files=[
        ('share/applications', ['data/my-app.desktop']),
    ],
    author='Shawn Brown',
    author_email='shawnbrown@users.noreply.github.com',
)
