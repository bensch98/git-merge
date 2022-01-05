class MissingArgumentException(Exception):
  def __init__(self, missing_args):
    """ Raises an exception that lists all missing arguments.
    :param missing_args: List of argument names, that are missing.
    """
    self.missing_args = missing_args
    self.message = self.__construct_message()
    super(MissingArgumentException, self).__init__(self.message)
  
  def __construct_message(self):
    msg = f'Following argumets are missing: {", ".join(self.missing_args)}'
    return msg
