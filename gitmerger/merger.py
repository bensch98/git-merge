""" Github Merger:
CLI to synchronize meta data of git activities of one account to another.
"""

import os
from datetime import datetime, timedelta
from github import Github
from gitmerger.tokens import *
from git import Repo 

class Commit:
  
  def __init__(self, date, message, hexsha):
    """ Git commit with relevant information for merge.
    :param date: Commit date as datetime object.
    :commit chash: Commit hash as identifier for commit to avoid duplicate commits.
    """
    self.date = date
    self.chash = hexsha
    

class Merger:

  __g = None
  __access_token = None 
  __dest_repos = []

  def __init__(self, access_token, author, repo_path):
    self.__access_token = access_token
    self.__g = Github(access_token)

    # destination repo
    self.__dest_repos = self.__g.get_user().get_repos()
    self.dest_repo = None

    # source repo
    self.repo_path = os.path.abspath(repo_path)
    self.src_repo = Repo(self.repo_path)
    self.author = author


  @property
  def dest_repo(self):
    print(f'Getter: {self._dest_repo}')
    return self._dest_repo

  @dest_repo.setter
  def dest_repo(self, repo):
    """ Set repo to either None or a valid repo name for the specified account. """

    # allow setting equal to None
    if repo == None:
      self._dest_repo = None
      return

    # if possible set to a destination repo
    for r in self.__dest_repos:
      if r.name == repo or r.full_name == repo:
        self._dest_repo = r
        return


  def get_commits(self, since='14.days.ago'):
    """ Get all commits in specified range """
    
    # get list of commits
    commits = list(self.src_repo.iter_commits('--all'))

    # filter for name of author
    commits_filtered = []
    for c in commits:
      # convert unix timestamp to datetime object
      converted_date = datetime.fromtimestamp(int(c.committed_date))
      # calc date x days ago and check if commit date is newer
      is_new = converted_date > datetime.now()-timedelta(days=14)

      # filter commits based on author and if commits were committed in last x period
      if c.author.name == self.author and is_new:
        c = Commit(converted_date, c.hexsha)
        commits_filtered.append(c)
        
    return commits_filtered


  def print_props(self):
    print(self.__g)
    print(self.__access_token)
    return


  def merge(self, src_repo, dest_repo):
    """ Submit dummy commits in destination repo with meta data from source repo. """
    pass

