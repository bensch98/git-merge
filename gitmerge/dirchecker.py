import os

class DirectoryChecker:
  def __init__(self, _dir='.'):
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
  
  def repo_exists(self, repo, dir_name):
    """ Checks whether a src repo already exists from past imports in the dest repo as directory
    :param path: Path of the src repo.
    :param dir_name: Name to check if a matching directory exists. 
    """
    if os.path.isdir(f'{repo.working_dir}/{dir_name}'):
      return True
    return False
