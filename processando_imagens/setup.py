from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processando_imagens",
    version="0.0.3",
    author="Edi",    
    description="Processamento de imagens com Python", 
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edhioliver/Processamento-de-imagens-em-Python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)