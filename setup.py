from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    function returns list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements.txt]

    '''
    or simply;
    
    with open('requirements.txt')
    '''
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
        requirements = [req.replace("\n", "") for req in requirements]

return requirements        
       
        






setup(
name= 'ML_25',
version = '0.0.1',  #flexibility incase I update
author = 'Mwadz',
author_email = 'mghoimwadime@gmail.com',
packages = find_packages(), #looks to see in how many folders the __init__.py exists then conciders the folders packages as well



all_requires = get_requirements('requirements.txt')
)

"""

install_requires= ['pandas','numpy', 'seaborn']
we won't be needing this since we made requirements.txt file


"""