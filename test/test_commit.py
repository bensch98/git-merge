import unittest
import os
from datetime import datetime

from git import Repo
from gitmerge.merge import Commit

class TestCommit(unittest.TestCase):
  
  def test_init(self):
    path = os.path.join(os.path.dirname(__file__), '..')
    repo = Repo(path)
    self.assertTrue(type(repo) is not None)
    repo_commits = list(repo.iter_commits('--all'))
    self.assertTrue(type(repo_commits) == list)
    
    # init dummy commits
    commits = []
    for c in repo_commits:
      commits.append(Commit(c.hexsha, datetime.now()))

    for c in commits: 
      self.assertTrue(c.hexsha is not None)
      self.assertTrue(c.date is not None)
      self.assertTrue(not c.transferred)

if __name__ == '__main__':
  unittest.main()
