Change Log
==========

0.0.1 (2021-12-27)
------------------

* First release on PyPI.

0.0.2 (2021-12-28)
------------------

* Added command-line interface gitmerge for easy usage of tool.

0.0.3 (2022-01-04)
------------------

* Added --since flag to specifiy time range of commits

0.0.4 (2022-01-09)
------------------

* Extended --since flag with custom config, like e.g. 3m5d
* Added CLI help colors
* Added error handling with custom Exceptions: MissingArgumentException, IncompatibleArgumentsException, InvalidRepositoryException
* Added DirectoryChecker class: can return all git sub directories of a directory
