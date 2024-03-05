from setuptools import find_packages,setup
from typing import List

Hypen = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list requirements
    '''

    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if Hypen in requirements:
            requirements.remove(Hypen)
    
    return requirements

setup(
    name='mlproject',
    version = '0.0.1',
    author = 'Sandeep',
    author_email = 'sandeepr2111@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)