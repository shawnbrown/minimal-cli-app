"""A package to demonstrate "scripts" and "data_files" installation."""
try:
    from distutils.core import setup
except ModuleNotFoundError as error:
    error.msg = f"""{error.msg}

    Your system does not appear to have the full `distutils` package.
    Distutils is part of the Python Standard Library but some Linux
    distributions are shipped with a minimal install of Python. You
    may have to install `distutils` using your system's package manager.

    For Debian or Debian-based distributions (like Ubuntu, Mint, etc.):

        sudo apt install python3-distutils
    """
    raise error


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
