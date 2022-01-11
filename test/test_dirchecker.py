import unittest
import os

from gitmerge.dirchecker import DirectoryChecker

class TestDirectoryChecker(unittest.TestCase):

  def test_git_subdirs(self, relpath=True):
    path = os.path.join(os.path.dirname(__file__), '../..')
    dc = DirectoryChecker(path)

    # test relpath=True
    subdirs = dc.git_subdirs()
    self.assertTrue(subdirs)
    for sd in subdirs:
      self.assertEqual(sd[0], '.')

    # test relpath=False
    subdirs = dc.git_subdirs(relpath=False)
    self.assertTrue(subdirs)
    for sd in subdirs:
      self.assertEqual(sd[0], '/')

    # test false case with no git_dirs
    dc._dir = '.'
    subdirs = dc.git_subdirs()
    self.assertFalse(subdirs)

if __name__ == '__main__':
  unittest.main()
