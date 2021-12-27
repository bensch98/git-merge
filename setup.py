from setuptools import setup

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
      install_requires=[
        'GitPython'
      ],
      python_requires='>=3.8')
