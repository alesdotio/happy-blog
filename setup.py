from setuptools import setup, find_packages
from happy_blog import __version__ as version

setup(
    name = 'happy-blog',
    version = version,
    description = 'A simple django blog app that uses django-hvad for translations.',
    author = 'Ales Kocjancic',
    author_email = 'ales.kocjancic@divio.ch',
    url = 'https://github.com/neo64bit/happy-blog',
    packages = find_packages(),
    zip_safe=False,
    include_package_data = True,
    install_requires=[
        'Django>=1.2',
        'django-cms>=2.0',
        'django-hvad',
        'django-tinymce',
        'django-simplegallery-hvad',
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ]
)