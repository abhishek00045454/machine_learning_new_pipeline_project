from setuptools import  find_packages,setup
from typing import List

HYPHON_E_DOT="-e ."

def get_requirements(filepath: str)->List[str]:
    requirements=[]
    

    with open(filepath) as  file_obj:
        requirements=file_obj.readlines()
        requirements=[ i.replace("\n","") for i in requirements]
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)   


setup(name="ML_new_pipleline_project",
      version="0.0.1",
      description="Machine Learning project ",
      author="abhishek_saini",
      author_email="abhisheksaini388@gmail.com",
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt"))

