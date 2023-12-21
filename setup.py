from setuptools import setup

setup(
    name='simplai',
    version='0.1.0',
    description='simplai: Simplify OpenAI API integration with Python.',
    author='Ignacio Rigoni',
    packages=['simplai'],
    install_requires=[
        "openai",
    ],
)
