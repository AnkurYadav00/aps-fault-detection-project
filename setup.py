from setuptools import setup, find_packages
from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT ="-e ."

def get_requirements()->List[str]:
    """
    Provides libraries names that we require for our project"""

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
    
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="ankur.yadav719@gmail.com",
    packages = find_packages(),
    install_required= get_requirements()
)