from setuptools import find_packages, setup

setup(
    name="igmapper-api",
    version="1.0.1",
    description="Collect public data from Instagram",
    author="lucaslealll",
    author_email="-",
    long_description=("README.md"),
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    package_data={"": ["assets/*", "docs/*"]},
    packages=find_packages(),
    install_requires=["requests", "selenium", "setuptools", "undetected-chromedriver"],
    classifiers=["Programming Language :: Python :: 3.10"],
)
