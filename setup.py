import io
import os
from pathlib import Path

from setuptools import find_packages, setup


# Metadata of package
NAME = 'prediction_model'
DESCRIPTION = 'Loan Prediction Model'
URL = 'https://github.com/keetrap/Packaging_ml_model'
EMAIL = 'parteekkamboj112@gmail.com'
AUTHOR = 'Prateek Kamboj'
REQUIRES_PYTHON = '>=3.7.0'

pwd = os.path.abspath(os.path.dirname(__file__))

# Get the list of packages to be installed
# def list_reqs(fname='requirements.txt'):
#     with io.open(os.path.join(pwd, fname), encoding='utf-8') as f:
#         return f.read().splitlines()

try:
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# Load the package's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'prediction_model': ['VERSION']},
    install_requires=[
        'colorama==0.4.6',
        'iniconfig==2.0.0',
        'joblib==1.4.2',
        'numpy==1.26.4',
        'packaging==24.0',
        'pandas==2.2.2',
        'pluggy==1.5.0',
        'pytest==8.2.1',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.1',
        'scikit-learn==1.5.0',
        'scipy==1.13.1',
        'six==1.16.0',
        'threadpoolctl==3.5.0',
        'tzdata==2024.1',
        'setuptools==67.8.0',
        'wheel==0.38.4',
    ],
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)