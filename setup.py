from setuptools import setup, find_packages

setup(
    name="InstagramFollowersAndUnfollowers",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "setuptools",
        "selenium",
        "undetected-chromedriver",
    ],
)
