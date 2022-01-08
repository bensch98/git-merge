#!/usr/bin/env python

import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
import git
from gitmerge.merge import Merger, Commit
from gitmerge.errors import MissingArgumentException, IncompatibleArgumentsException
from gitmerge.dirchecker import DirectoryChecker

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
@click.option('--company', '-c', required=False, default='', help='Company name where you worked at for this repo.')
@click.option('--since', '-s', required=False, default='1w', help='Consider commits since date, days, month, years ago. Examples: 0y3m1w6d, 3m1w6d, 14d, 1d8w.')
@click.option('--list', '-l', '_list', required=False, is_flag=True, help='Only list the commits, instead of committing and pushing them to the mock repo.')
def merge(author, src, _dir, dest, company, since, _list):
  
  # check if args are missing or incompatible args where specified
  if src is None and _dir is None:
    raise MissingArgumentException(["--src", "--dir"])
  elif src is not None and _dir is not None:
    raise IncompatibleArgumentsException(["--src", "--dir"])

  # get all .git sub directories of _dir
  dc = DirectoryChecker(_dir)
  git_dirs = dc.git_subdirs()

  # append src if no _dir mode was selected to iterate over list of length = 1
  if src:
    git_dirs.append(src)

  for gd in git_dirs:
    # init Merger and get commits of repo in time range
    m = Merger(author, gd, dest, company)
    commits = m.get_commits(since)

    if not _list:
      m.merge(commits)
      m.push()
    else:
      # prints basic preview of changes that would've been committed and pushed
      click.echo(click.style(f'Repository: {m.src_name}',  fg='blue', bold=True))
      click.echo(click.style('\tHash\t\t\t\t\t   Date', fg='green', bold=True))
      idx = 0
      for idx, c in enumerate(commits):
        click.echo(f'{idx}\t{c.hexsha} | {c.date[:-6]}')
      click.echo(click.style('----------------------------------------------------------------------------', fg='green', bold=True))
      click.echo(f'{idx} total changes that can be committed / pushed\n\n')

    if not _list:
      click.echo('Print the same statement without --list flag for committing and pushing it.')

  click.echo(f'\nTotal repositorys listed: {len(git_dirs)}')

# add all above listed commands to CLI
# if necessary, commands can be disabled by commenting them out here (only for test purposes)
gitmerge.add_command(merge)


if __name__ == '__main__':
  gitmerge()
