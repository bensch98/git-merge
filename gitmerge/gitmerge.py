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
def merge(author, src, dest, company):
  m = Merger(author, src, dest, company)
  commits = m.get_commits()
  m.merge(commits)
  m.push()

gitmerge.add_command(merge)

if __name__ == '__main__':
  gitmerge()
