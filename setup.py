from setuptools import setup

with open('README.md', 'r') as fh:
  long_description = fh.read()

setup(name='gitmerger',
      version='0.0.1',
      description='Adding git commits from von repo to another.',
      author='Benedikt Scheffler',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['gitmerger'],
      classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
      ],
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
