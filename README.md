# GitMerge

As many developers have to use a separate Git account during work, a large amount of their work is not tracked in their personal profile which is often a good reference on resumes etc.
GitMerge solves this problem by importing meta data of your work commits to a dummy repo in your private Git account.

---

## Installation

Easiest way:
```bash
pip install gitmerge
```

Or you can also install it from source.
For development clone the repo and install it with `-e` flag.

```bash
git clone git@github.com:bensch98/git-merge.git
cd git-merge
pip install -e .
```

If you have nice ideas, feel free to open a PR.

---

## Usage

The easiest way to use this package is via its CLI.
```bash
gitmerge merge --author [GIT_NAME] --src [SOURCE_REPO] --dest [DESTINATION_REPO] --company [COMPANY_NAME] --since 2021-12-31 --until 2022-01-10
```

CLI:
```text
$ gitmerge merge --help
Usage: gitmerge merge [OPTIONS]

  Import git commits from one repo to another

Options:
  -a, --author TEXT   Name of the user whose commits of the source repo should
                      be transferred.  [required]
  --src TEXT          Path to source repo where the commits were created.
  --dir TEXT          Path to a directory, where all subfolders with a .git
                      directory are considered. This is a shortcut for
                      multiple single statements if you want to transfer
                      commtis of several source repos into your mock repo.
  -d, --dest TEXT     Path to the destination repo where the commits should be
                      transferred to.  [required]
  --company TEXT      Company name where you worked at for this repo.
  -s, --since TEXT    Consider commits since date, days, month, years ago.
                      Examples: 0y3m1w6d, 3m1w6d, 14d, 1d8w. [DEFAULT = 1w]
  -u, --until TEXT    Consider commits until date, days, month, years ago.
                      Examples: 0y3m1w6d, 3m1w6d, 14d, 1d8w. [DEFAULT = 0d]
  -l, --list          Only list the commits, instead of committing and pushing
                      them to the mock repo. Red highlighted commits have
                      already been transferred in the past to the specified
                      destination and are automatically ignored.
  -c, --columns TEXT  Name column that should be included.
  --help              Show this message and exit.
```


Flags:
- --author: Your Git username which was used for the commits. Only commits of this account will be merged into the destination repo. 
- --src: Relative path to the source repository from which you want to import the commits.
- --dir: Relative path to a directory where all subfolders with a .git directory are taken into account. If all repos are located in one parent folder, their commits can easily be transferred via one command.
- --dest: Relative path to the destination/dummy repository where the commits will be imported into. For each repository a directory and file will be created where meta data of the commits will be stored.
- --company: The name of the company which owns the repository. Can be omitted in the future.
- --since: Specifies from where on the commits should be taken into account. Can be specified as date (2021-09-30, 2021/09/30, 2021-9-1, 2021/9/30, ...) or as a delta value.
- --until: Specifies until which date the commits should be taken into account. Can be specified as date (2021-09-30, 2021/09/30, 2021-9-1, 2021/9/30, ...) or as a delta value.
- --list: Can be used to view the commits which would be committed and pushed without this flag. It does nothing despite printing out the commits to the terminal.
- --columns: Columns that should be considered. Possible columns are **hexsha**, **date**, **message**, **company**, **repository**.

For more help use the *--help* flag of the CLI.

Examples for --since flag:
- 1y: All commits of last year.
- 1y3m: All commits of last 15 months.
- 2w4d: All commits of last 2 weeks and 4 days (18 days).
- 40d1y: All commits of last year and 40 days (405 days).
- 0d: Only todays commits.
 
--since defaults to the last 7 days if nothing was specified.
Each mode (y = year, m = month, w = week, d = days) defaults to 0 if omitted. Therefore 2d == 0y0m0w2d.
--until default to current datetime


The package can also be imported and used like this.
```python
from gitmerge.merge import Merger
m = Merger('USERNAME', '../PATH/TO/SOURCE/REPO', '../PATH/TO/DESTINATION/REPO', 'COMPANY_NAME')
commits = m.get_commits()
m.merge(commits)
m.push
```

## Example

```bash
gitmerge merge \
	--author bensch98
	--dir ..
	--dest ../dest_repo
	--list
	--since 2w
	--until 2022-02-23
	-c hexsha -c date -c message -c company -c repository
```

## TODOs

* Documentation (README / Sphinx ?)
* Unittests
* Github Actions (workflows)
* Command-line interface with click (more configuration options)


Help with these TODOs or good advice is greatly appreciated.
For any questions open an issue.
