from setuptools import setup, find_packages
from AnimeThemes.__vars__ import __version__, __author__, __email__


setup(
    name='animethemes',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/TaprisSugarbell/AnimeThemes',
    author=__author__,
    author_email=__email__,
    description='Unofficial https://staging.animethemes.moe Package',
    long_description=open("./README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "beautifulsoup4",
        "cloudscraper"
    ],
    project_urls={
        "Issue tracker": "https://github.com/TaprisSugarbell/AnimeThemes/issues"
    }
)


