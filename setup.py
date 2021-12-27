from setuptools import setup

with open('README.md', 'r') as fh:
  long_description = fh.read()

CLASSIFIERS = [
  'Programming Language :: Python :: 3',
  'License :: OSI Approved :: MIT License'
]

setup(name='gitmerge',
      version='0.0.1',
      description='Adding git commits from von repo to another.',
      author='Benedikt Scheffler',
      author_email='scheffler.benedikt@gmail.com',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['gitmerge'],
      classifiers=CLASSIFIERS,
      # prod dependencies
      install_requires=[
        'GitPython==3.1.24'
      ],
      # dev dependencies
      extras_require={
        'dev': [
          'GitPython>=3.1.24'
        ]
      },
      python_requires='>=3.8')
