import setuptools
from distutils.core import setup

setup(
    name="tbm",
    version="1",
    description="telegram bot manager",
    long_description="use this package to manage your telegram bot projects",
    author="https://github.com/pousay",
    author_email="pouryathesaymon@gmail.com",
    packages=["tbm"],
    entry_points={"console_scripts": ["tbm=tbm.main:main"]},
    requires=["watchdog", "inquirer"],
)
