# GitMerge

As many developers have to use a separate Git account during work, a large amount of their work is not tracked in their personal profile which is often a good reference on resumes etc.
GitMerge solves this problem by importing meta data of your work commits to a dummy repo in your private Git account.


## Installation

Easiest way:
```bash
pip install gitmerge
```

Or you can also install it from source.

If you have nice ideas, feel free to open a PR.


## Usage

The easiest way to use this package is via its CLI.
```bash
gitmerge merge --author [GIT_NAME] --src [SOURCE_REPO] --dest [DESTINATION_REPO] --company [COMPANY_NAME] --since 2021-12-31
```

Flags:
- --author: Your Git username which was used for the commits. Only commits of this account will be merged into the destination repo. 
- --src: Relative path to the source repository from which you want to import the commits.
- --dest: Relative path to the destination/dummy repository where the commits will be imported into. For each repository a directory and file will be created where meta data of the commits will be stored.
- --company: The name of the company which owns the repository. Can be omitted in the future.
- --since: Specifies from where on the commits should be taken into account. Can be specified as date (2021-09-30, 2021/09/30, 2021-9-1, 2021/9/30, ...) or as a delta value.
- --list: Can be used to view the commits which would be committed and pushed without this flag. It does nothing despite printing out the commits to the terminal.

For more help use the *--help* flag of the CLI.

Examples for --since flag:
- 1y: All commits of last year.
- 1y3m: All commits of last 15 months.
- 2w4d: All commits of last 2 weeks and 4 days (18 days).
- 40d1y: All commits of last year and 40 days (405 days).
- 0d: Only todays commits.
 
--since defaults to the last 7 days if nothing was specified.
Each mode (y = year, m = month, w = week, d = days) defaults to 0 if omitted. Therefore 2d == 0y0m0w2d.


The package can also be imported and used like this.
```python
from gitmerge.merge import Merger
m = Merger('USERNAME', '../PATH/TO/SOURCE/REPO', '../PATH/TO/DESTINATION/REPO', 'COMPANY_NAME')
commits = m.get_commits()
m.merge(commits)
m.push
```

## TODOs

* Documentation (README / Sphinx ?)
* Unittests
* Github Actions (workflows)
* Command-line interface with click (more configuration options)


Help with these TODOs or good advice is greatly appreciated.
For any questions open an issue.
I check these almost every day.
For collaboration we can communicate via Discord if needed.
