from setuptools import setup

setup(
    name='pinglog',
    version='0.1',
    description='Async logging to versatile devices for ML experiments',
    author='Himanshu Gaurav Singh',
    author_email='himanshu_singh@berkeley.edu',
    packages=['pinglog',],
    install_requires=[
        'discord.py',
    ],
)
