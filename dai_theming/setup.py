from setuptools import setup, find_packages
import os

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='dai_theming',
    version='0.1',  # Increment with changes
    packages=find_packages(),  # Find all packages in this directory
    include_package_data=True,  # Include everything in MANIFEST.in if it exists
    install_requires=[
        'django>=3.0',  # Ensure correct Django version is installed
        # List other dependencies if any
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ],
)
