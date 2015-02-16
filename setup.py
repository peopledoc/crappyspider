try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="crappyspider",
    packages=["crappyspider"],
    version='0.3',
    install_requires=['scrapy'],
    description="Test your site.",
    author="Peopledoc",
    author_email="hobbestigrou@erakis.eu",
    url="http://crappyspider.readthedocs.org/en/latest/",
    download_url="",
    keywords=["crawler", "scrapy"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description="""\
Crappyspider
------------

Crappyspider is a generic crawler. The goal is to easily test your site for
HTTP errors and more.


This version requires Python 2.7 or later.
"""
)
