#!/usr/bin/env python

import click
import git
from gitmerge.merge import Merger, Commit

""" CLI """

@click.group()
def gitmerge():
  """ Entry point of CLI """
  pass

@click.command(help='Import git commits from one repo to another')
@click.option('--author', '-a', required=True, help='Name of user which commits of the source repo should be transferred.')
@click.option('--src', '-s', required=True, help='Path to source repo which the contributions were committed.')
@click.option('--dest', '-d', required=True, help='Path to destination repo which the contributions should be transferred to.')
@click.option('--company', '-c', required=True, help='Company name where you at for this repo.')
@click.option('--list', '-l', '_list', required=False, is_flag=True, help='Only list the commits, instead of committing and pushing them to the mock repo.')
def merge(author, src, dest, company, _list):
  m = Merger(author, src, dest, company)
  commits = m.get_commits()
  
  if not _list:
    m.merge(commits)
    m.push()
  else:
    m.preview(commits)   


gitmerge.add_command(merge)

if __name__ == '__main__':
  gitmerge()
