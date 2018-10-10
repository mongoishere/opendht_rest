from setuptools import setup, find_packages

with open('README.rst') as tmp_file:
    readme = tmp_file.read()

with open('LICENSE') as tmp_file:
    license = tmp_file.read()

setup(
    name='New Python Project',
    version='0.1.0dev',
    description='New Python Project Description',
    long_description='readme',
    author='Trevor Medina',
    url='https://github.com/mongoishere/new_pyproject',
    license=license,
    packages=find_packages(exclude=(
        'docs',
        'tests',
        '.vscode'
    ))
)
