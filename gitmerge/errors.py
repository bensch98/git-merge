import os

class MissingArgumentException(Exception):
  def __init__(self, missing_args):
    """ Raises an exception that lists all missing arguments.
    :param missing_args: List of argument names, that are missing.
    """
    self.missing_args = missing_args
    self.msg = self.__construct_message()
    super(MissingArgumentException, self).__init__(self.msg)
  
  def __construct_message(self):
    msg = f'Following argumets are missing: {", ".join(self.missing_args)}'
    return msg

class IncompatibleArgumentsException(Exception):
  def __init__(self, args):
    """ Raises an exception that lists all arguments, that cannot be used together.
    :param args: All flags that are incompatible. Will be printed out to the user.
    """
    self.args = args
    self.msg = self.__construct_message()
    super(IncompatibleArgumentsException, self).__init__(self.msg)

  def __construct_message(self):
    msg = f'Too many arguments specified. One of the following arguments has to be omitted {", ".join(self.args)}'
    return msg

class InvalidRepositoryException(Exception):
  def __init__(self, dest):
    """ Informs user of invalid path to destination directory due to missing .git directory.
    :param dest: Path to the specified git repository/destination.
    """
    self.dest = os.path.abspath(dest)
    self.msg = self.__construct_message()
    super(InvalidRepositoryException, self).__init__(self.msg)

  def __construct_message(self):
    msg = f'The specified path is no valid git repository. No .git dircectory found inside {self.dest}'
    return msg
