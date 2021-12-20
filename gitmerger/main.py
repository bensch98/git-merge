""" Github Merger:
CLI to synchronize meta data of git activities of one account to another.
"""

from github import Github

class GitMerger:
  
  def __init__(self, access_token):
    self.access_token = access_token
