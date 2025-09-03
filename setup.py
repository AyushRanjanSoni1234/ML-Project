from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    """This function will return the list of requirements"""
    requirement = []
    with open(file_path) as file:
        requirement = file.readlines()
        requirement = [req.replace("\n","") for req in requirement]

        if "-e ." in requirement:
            requirement.remove("-e .")    
            
    return requirement

setup(
    name="MLproject",
    version="0.1.0",
    author="Ayush",
    author_email="ars7408984015@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)