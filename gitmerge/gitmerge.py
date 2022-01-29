#!/usr/bin/env python

import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
import git

from gitmerge.merge import Merger, Commit
from gitmerge.errors import MissingArgumentException, IncompatibleArgumentsException
from gitmerge.dirchecker import DirectoryChecker
from gitmerge.cout import Cout

""" CLI """

@click.group(
  cls=HelpColorsGroup,
  help_headers_color='yellow',
  help_options_color='blue'
)
def gitmerge():
  """ Entry point of CLI """
  pass

@click.command(
  help='Import git commits from one repo to another',
  cls=HelpColorsCommand,
  help_headers_color='yellow',
  help_options_color=None,
  help_options_custom_colors={'--author': 'blue', '--dest': 'blue'}
)
@click.option('--author', '-a', required=True, help='Name of the user whose commits of the source repo should be transferred.')
@click.option('--src', required=False, help='Path to source repo where the commits were created.')
@click.option('--dir', '_dir', required=False, help='Path to a directory, where all subfolders with a .git directory are considered. This is a shortcut for multiple single statements if you want to transfer commtis of several source repos into your mock repo.')
@click.option('--dest', '-d', required=True, help='Path to the destination repo where the commits should be transferred to.')
@click.option('--company', required=False, default='', help='Company name where you worked at for this repo.')
@click.option('--since', '-s', required=False, default='1w', help='Consider commits since date, days, month, years ago. Examples: 0y3m1w6d, 3m1w6d, 14d, 1d8w. [DEFAULT = 1w]')
@click.option('--until', '-u', required=False, default='0d', help='Consider commits until date, days, month, years ago. Examples: 0y3m1w6d, 3m1w6d, 14d, 1d8w. [DEFAULT = 0d]')
@click.option('--list', '-l', '_list', required=False, is_flag=True, help='Only list the commits, instead of committing and pushing them to the mock repo. Red highlighted commits have already been transferred in the past to the specified destination and are automatically ignored.')
@click.option('--columns', '-c', required=False, default=None, multiple=True, help='Name column that should be included.')
def merge(author, src, _dir, dest, company, since, until, _list, columns):
  
  # check if args are missing or incompatible args where specified
  if src is None and _dir is None:
    raise MissingArgumentException(["--src", "--dir"])
  elif src is not None and _dir is not None:
    raise IncompatibleArgumentsException(["--src", "--dir"])

  # get all .git sub directories of _dir
  git_dirs = []
  if _dir is not None:
    dc = DirectoryChecker(_dir)
    git_dirs = dc.git_subdirs()

  # append src if no _dir mode was selected to iterate over list of length = 1
  if src:
    git_dirs.append(src)

  pushable = 0
  for gd in git_dirs:
    # init Merger and get commits of repo in time range
    m = Merger(author, gd, dest, company)
    commits = m.get_commits(since, until)

    if not _list:
      m.merge(commits)
      m.push()
    else:
      cout = Cout(m, commits, git_dirs, columns)
      pushable += cout.list()
  cout.summary(pushable)


# add all above listed commands to CLI
# if necessary, commands can be disabled by commenting them out here (only for test purposes)
gitmerge.add_command(merge)


if __name__ == '__main__':
  gitmerge()
