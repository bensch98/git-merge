""" Github Merger:
CLI to synchronize meta data of git activities of one account to another.
"""

import os
from datetime import datetime, timedelta
import time
import hashlib

from git import Repo 

class Commit:
  
  def __init__(self, date, hexsha):
    """ Git commit with relevant information for merge.
    :param date: Commit date as datetime object.
    :commit chash: Commit hash as identifier for commit to avoid duplicate commits.
    """
    self.date = date
    self.hexsha = hexsha
    

class Merger:

  def __init__(self, author, src_path, dest_path, company):
    # repos
    self.src_repo = Repo(os.path.abspath(src_path))
    src_name = self.src_repo.remotes.origin.url.split('.git')[0].split('/')[-1]
    self.hashed_repo_name = hashlib.sha512(src_name.encode('utf-8')).hexdigest()[:20]
    
    self.dest_repo = Repo(os.path.abspath(dest_path))

    # name of commiter in src path
    self.author = author
    # company name where commits are imported from
    self.company = company

    # list of all filtered commits
    self.commits = None

  def get_commits(self, days_ago=14):
    """ Get all commits in specified range """
    
    # get list of commits
    commits = list(self.src_repo.iter_commits('--all'))

    # filter for name of author
    commits_filtered = []
    for c in commits:
      # convert unix timestamp to datetime object
      converted_date = datetime.fromtimestamp(int(c.committed_date))
      #convert to iso date
      iso_date = time.strftime("%Y-%m-%d %H:%M:%S +0000", time.gmtime(c.committed_date))
      
      # calc date x days ago and check if commit date is newer
      is_new = converted_date > datetime.now()-timedelta(days=days_ago)

      # filter commits based on author and if commits were committed in last x period
      if c.author.name == self.author and is_new:
        commit = Commit(iso_date, c.hexsha)
        commits_filtered.append(commit)
      
      self.commits = commits_filtered

    return commits_filtered

  def preview(self, commits):
    """ Print out a review of the commits. """ 
    print('\tHash\tDate') 
    max = len(commits)
    for idx, c in enumerate(commits):
      print(f'{idx} - {c.hexsha} | {c.date}') 
    print('------------------------------------------------------------------')
    print(f'{idx} total changes that can be committed / pushed')
    print(f'Print the same statement without --list flag for committing and pushing it')

  def __create_directory(self):
    """ Creates directory in destination repo with hashed name and one file with headers. """
    # inspect directory structure
    tree = self.dest_repo._working_tree_dir
    directories = [f for f in os.listdir(tree) if os.path.isdir(f'{tree}/{f}')]

    # create new directory if not already present
    if self.hashed_repo_name not in directories:
      # create new directory
      os.mkdir(f'{tree}/{self.hashed_repo_name}')

    # init new file
    file_name = f'{tree}/{self.hashed_repo_name}/test.txt'
    with open(file_name, 'w') as f:
      f.write('Company Name\t\tDate\t\tCommit Hex Sha\n') 

    return file_name
          
  def merge(self, commits=None):
    """ Submit dummy commits in destination repo with meta data from source repo. """
    # if not list of commits is provieded use the list of commits available from class
    # this way someone can retrieve the commits and filter them additionally as they like
    if commits == None:
      commits = self.commits
    
    file_name = self.__create_directory()
    for c in commits:
      with open(file_name, 'a') as f:
        f.write(f'{self.company}\t\t{c.date}\t\t\t\t\t\t\t{c.hexsha}\n')
      os.environ['GIT_AUTHOR_DATE'] = c.date
      os.environ['GIT_COMMITTER_DATE'] = c.date
      try:
        self.dest_repo.git.add('.')
        self.dest_repo.git.commit('-m', 'test', '--allow-empty')
      except git.exc.GitError as e:
        print(f'Error in commit: {e}') 

  def push(self):
    """ Push changes after merging one repo into another. """
    try:
      origin = self.dest_repo.remote(name='origin')
      origin.push()
    except:
      print('Some error occurred while pushing the code.')
