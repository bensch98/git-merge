# Git Merger

As many developers have to use a separate git account during work, a large amount of their work is not tracked in their personal profile which is often a good reference on resumes etc.
GitMerger solves this problem by importing meta data of your work commits to a dummy repo in your private Git account.


## Installation

Easiest way:
```bash
pip install gitmerge
```

Or you can also install it from source.

If you have nice ideas, feel free to open a PR.


## Usage

So far this package has to be used in code like this:
```python
from gitmerge.merge import Merger
m = Merger('USERNAME', '../PATH/TO/SOURCE/REPO', '../PATH/TO/DESTINATION/REPO', 'COMPANY_NAME')
commits = m.get_commits()
m.merge(commits)
m.push
```

However, a CLI is already in work to simplify the whole process.

## TODOs

* Documentation (README / Sphinx ?)
* Unittests
* Github Actions (workflows)
* Command-line interface with click
* more configuration options
