from setuptools import setup, find_packages


setup(
    name='pyhangouts',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'selenium==2.47.3',
        'xvfbwrapper==0.2.5',
    ],
    author='Aji Liu',
    author_email='amigcamel@gmail.com',
    description="A selenium-based client for Google Hangouts",
)
