from setuptools import find_packages,setup 
from typing import List 



def get_requirements(file_path:str)->List[str]:
    """This fun will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n", "")  for req in requirements]

    return requirements
setup(
    name = "ML_Raja",
    version="0.0.1",
    author = "Renga Rajan k",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    )