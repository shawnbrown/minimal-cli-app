Command Line and Desktop Entry Launcher Demo
============================================


Project Structure
-----------------

This demo uses the following directory structure:

    my-app-demo/
    ├── bin/
    │   └── my-app
    ├── data/
    │   └── my-app.desktop
    ├── my_app/
    │   ├── __init__.py
    │   └── submodule.py
    ├── setup.cfg
    └── setup.py

Each file in the above structure serves a specific function:

**`bin/my-app`:** Terminal command that gets installed (the file's `#!python`
is replaced with the appropriate shebang on install). Users can run this
command simply by typing "my-app" at the command line.

**`data/my-app.desktop`:** Desktop entry file provides a clickable icon for
Linux desktop environments (GNOME, KDE, etc.).

**`my-app/__init__.py`:** Standard Python package init file defines the
importable package objects.

**`my-app/submodule.py`:** Sub-module containing package code that implements
application logic.

**`setup.cfg`:** Setup configuration file.

**`setup.py`:** Setup script.


The setup.py File
-----------------

```python
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
)
```

In this demo, we use the `scripts` argument (above) instead of `entry_points`.
We do this so it's easier to install the app on systems that may not have easy
access to `pip` and `setuptools`.


Installing and Removing
-----------------------

Install with `pip`:

    pip install ./my-app-demo

Install with `pip` from live GitHub repo:

    pip install --upgrade https://github.com/shawnbrown/my-app-demo/archive/main.zip

To install without `pip` (harder to uninstall):

    cd my-app-demo
    python setup.py install --user --prefix=;

If you used `pip` to install `my_app`, you can easily remove it with `pip`:

    pip uninstall my_app

If you need to uninstall `my_app` but you didn't install it using `pip`, you
can delete its individual files manually (a list of these files was saved in
`install-log.txt` during installation).

Another way to remove `my_app` is to overwrite the non-pip installation
with a `pip` installation, and then remove it using `pip`:

    pip install --ignore-installed --force-reinstall ./my-app-demo
    pip uninstall my_app
