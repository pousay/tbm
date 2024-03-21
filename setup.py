import setuptools
from distutils.core import setup

with open("README.md", "r") as f:
    d = f.read()


setup(
    name="tbm",
    version="1.2.5",
    description="telegram bot manager",
    long_description=d,
    long_description_content_type="text/markdown",
    author="https://github.com/pousay",
    author_email="pouryathesaymon@gmail.com",
    packages=["tbm"],
    entry_points={"console_scripts": ["tbm=tbm.main:main"]},
    install_requires=["watchdog", "inquirer"],
)
