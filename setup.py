from setuptools import setup, find_packages
import pathlib

from gitmerge import __version__


readme = pathlib.Path(__file__).parent / 'README.md'
reqs = pathlib.Path(__file__).parent / 'requirements.txt'
reqs_dev = pathlib.Path(__file__).parent / 'requirements_dev.txt'

with open(readme, 'r') as fh:
  long_description = fh.read()

CLASSIFIERS = [
  'Programming Language :: Python :: 3',
  'License :: OSI Approved :: MIT License',
]

with open(reqs, 'r') as f:
  install_requirements = f.read().splitlines()

with open(reqs_dev, 'r') as f:
  dev_requirements = f.read().splitlines()

setup(name='gitmerge',
      version=__version__,
      description='Add your git commits from your corporate account to your private profile with gitmerge.',
      author='Benedikt Scheffler',
      author_email='scheffler.benedikt@gmail.com',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=find_packages(),
      classifiers=CLASSIFIERS,
      entry_points={
        'console_scripts': ['gitmerge=gitmerge.gitmerge:gitmerge']
      },
      # prod dependencies
      install_requires=install_requirements,
      # dev dependencies
      extras_require={
        'dev': dev_requirements
      },
      python_requires='>=3.8')
