from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)-> list[str]:
    reqire = []

    with open(file_path) as file_obj:
        reqire = file_obj.readlines()
        reqire = [req.replace("\n","") for req in reqire]

        if "-e ." in reqire:
            reqire.remove("-e .")
    return reqire

setup(
    name="firstmlpoject",
    version="0.0.1",
    author="karan",
    author_email="mewo@example.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),

)
