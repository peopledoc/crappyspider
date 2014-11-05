from distutils.core import setup

setup(
    name="crappyspider",
    packages=["crappyspider"],
    version='0.1.dev0',
    install_requires=['scrapy'],
    description="Test your site.",
    author="Peopledoc",
    author_email="support@people-doc.com",
    url="http://crappyspider.readthedocs.org/en/latest/",
    download_url="",
    keywords=["crawler", "scrapy"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
    long_description="""\
Crappyspider
------------

Crappyspider is a generic crawler. The goal is to test easily your site and see
see if you have error.


This version requires Python 2.7 or later.
"""
)
