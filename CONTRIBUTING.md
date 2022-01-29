# Table of Contents

<!-- toc -->

- [Contributing to gitmerge](#contributing-to-gitmerge)
- [Unit testing](#unit-testing)

<!-- toc -->

## Contributing to gitmerge

Thank you for your interest in contributing to gitmerge!
Before you begin writing code, it is important that you share your intention 
to contribute with the team, based on the type of contribution:

1. You want to propose a new feature and implement it.
  - Post about your intended feature in [issue](https://github.com/bensch98/git-merge/issues),
  and we shall discuss the design and implementation. Once we agree that the plan looks good,
  go ahead and implement it.
2. You want to implement a feature or bug-fix for an outstanding issue.
- Search for your issue in the [gitmerge issue list](https://github.com/bensch98/git-merge/issues).
- Pick an issue and comment that you'd like to work on the feature or bug-fix.
- If you need more context on a particular issue, please ask and we shall provide.

Once you implement and test your feature or bug-fix, please submit a Pull Request to
https://github.com/bensch98/git-merge.

## Unit testing

All gitmerge test suites are located in `test` folder and start with `test_`.
For testing this repo uses the python unittest module.
You can run all unittests with:

```bash
python -m unittest -v
```

To run just a single test run:

```bash
python -m unittest -v test/[FILE]
```

The CI pipeline runs in GitHub Actions and executes all unittests after committing and opening PRs.
