from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->list:
    """This function returns a list of requirements from the given file."""
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()# read all lines
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Priyanshu", 
    author_email="priyanshusakharkar2827@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)