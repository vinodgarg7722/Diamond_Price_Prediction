from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

    return requirements

setup(
    name='Diamond_Price_Prediction',
    version='0.0.1',
    author='Vinod Garg',
    author_email='vinodgarg070702@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
