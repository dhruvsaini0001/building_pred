from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    Docstring for get_requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: List[str]
    '''
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]

        if '-e .' in requirements:
            requirements.remove('-e .')

        
    return requirements


setup(
    name='ml_project',
    version='0.0.1',
    author='Dhruv Saini',
    author_email='dhruvsaini2209@example.com',
    install_requires=get_requirements('requirements.txt'),
    
    )