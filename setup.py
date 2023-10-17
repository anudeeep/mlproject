from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements 
    ''' 
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n"," ")for req in requirements] #since our packages in req.txt are listed 1 by 1 we will get a /n new line so we are removing it by replacing it with a blank space

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
name = 'mlproject',
version = '0.0.1',
author = 'Anudeep',
#author_email = 'a@gmail.com',
packages = find_packages(),
#install_requires = ['pandas', 'numpy' , 'seaborn'] #we might have 100s of packages needed, not feasible, use a function instead to get the requirements.txt folder
install_requires = get_requirements('requirements.txt')
)