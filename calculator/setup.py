from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.readlines()

long_description = "A simple command line utility calculator."

setup(
    name="pythoncalculator",
    version="1.0.0",
    author="William Stella",
    author_email="william.a.stella@gmail.com",
    url="https://github.com/cestella/software_engineering_curriculum/tree/master/calculator",
    description="Command line calculator using python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="APACHE",
    packages=find_packages(),
    entry_points={"console_scripts": ["calc = src.cli:main"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ),
    keywords="calculator python package williamstella",
    install_requires=requirements,
    zip_safe=False,
)
