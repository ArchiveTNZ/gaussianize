from setuptools import setup

setup(
    name='gaussianize',
    version='1.0-SNAPSHOT',
    packages=[''],
    url='https://github.com/Cognevo/gaussianize',
    license='MIT',
    author='Abram Spamers',
    author_email='abram.spamers@team.telstra.com',
    install_requires=[
        'numpy', 
        'scipy', 
        'sklearn'
    ],
    description='A fork of the versteeg gaussianize library'
)