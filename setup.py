from setuptools import setup

with open('README.md', 'r') as fh:
  long_description = fh.read()

CLASSIFIERS = [
  'Programming Language :: Python :: 3',
  'License :: OSI Approved :: MIT License'
]

INSTALL_REQUIREMENTS = [
  'GitPython==3.1.24',
  'click',
  'regex'
]

DEV_REQUIREMENTS = [
  'GitPython>=3.1.24',
  'click',
  'regex'
]

setup(name='gitmerge',
      version='0.0.3',
      description='Add your git commits from your corporate account to your private profile with gitmerge.',
      author='Benedikt Scheffler',
      author_email='scheffler.benedikt@gmail.com',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['gitmerge'],
      classifiers=CLASSIFIERS,
      entry_points={
        'console_scripts': ['gitmerge=gitmerge.gitmerge:gitmerge']
      },
      # prod dependencies
      install_requires=INSTALL_REQUIREMENTS,
      # dev dependencies
      extras_require={
        'dev': DEV_REQUIREMENTS
      },
      python_requires='>=3.8')
