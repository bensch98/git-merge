import os

class DirectoryChecker:
  def __init__(self, _dir):
    self._dir = _dir

  def git_subdirs(self, relpath=True):
    """ Checks all subdirectories of _dir whether there is a .git folder and returns them as a list.
    :param relpath: Specify return type as list of absolute or relative paths.
    """
    # list of subdirectories
    git_dirs = next(os.walk(self._dir))[1]

    # filter dirs out which don't have a .git subdirectory
    for i in range(len(git_dirs)-1, -1, -1):
      subdirs = next(os.walk(f'{self._dir}/{git_dirs[i]}'))[1]
      if '.git' not in subdirs:
        git_dirs.pop(i)

    if relpath:
      git_dirs = [os.path.relpath(f'{self._dir}/{gd}') for gd in git_dirs]
    else:
      git_dirs = [os.path.abspath(f'{self._dir}/{gd}') for gd in git_dirs]
        
    return git_dirs
