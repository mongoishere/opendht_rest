from setuptools import setup, find_packages

with open('README.rst') as tmp_file:
    readme = tmp_file.read()

with open('LICENSE') as tmp_file:
    license = tmp_file.read()

setup(
    name='OpenDHT REST',
    version='0.1.0dev',
    description='A REST API for OpenDHT',
    long_description='readme',
    author='Trevor Medina',
    url='https://github.com/mongoishere/opendht_rest.git',
    license=license,
    packages=find_packages(exclude=(
        'docs',
        'tests',
        '.vscode'
    ))
)
