from setuptools import setup

setup(
    name='somopai',
    version='0.1.0',
    description='SimoPAI: Simplify OpenAI API integration with Python.',
    author='Nachokhan',
    author_email='ignacio.rigoni@gmail.com',
    packages=['simoPAI'],
    install_requires=[
        "openai",
    ],
)
