from setuptools import setup

setup(
    name='gaussianize',
    version='0.1',
    packages=['numpy, scipy, sklearn'],
    url='https://github.com/Cognevo/gaussianize',
    license='MIT',
    author='Abram Spamers',
    author_email='aspamers@gmail.com',
    install_requires=[
        'keras', 'numpy',
    ],
    description='A fork of the versteeg gaussianize library'
)