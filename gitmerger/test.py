import os
from git import Repo

def main():
  p = os.path.abspath('../../configuration')
  repo = Repo(p)
  print(repo.__dict__)

if __name__ == '__main__':
  main()
