import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand

COLUMN_FORMATS = {
  'hexsha': '<42',
  'date': '<21',
  'message': '<40',
  'idx': '<4',
  'repository': '<20',
  'company': '<20'
}

class Cout:
  def __init__(self, merger, commits, git_dirs, columns=('hexsha', 'date', 'message'), show_msg=False):
    self.merger = merger
    self.commits = commits
    self.git_dirs = git_dirs
    self.columns = columns
    self.show_msg = show_msg

    # format commits
    for c in self.commits:
      c.date = c.date[:-6]
      if len(c.message) > 38:
        c.message = c.message[:35]+'...'
      else:
        # cut off line break \n in commit message
        c.message = c.message[:-1]

  def list(self):

    click.echo(click.style(f'Repository: {self.merger.src_name}', fg='blue', bold=True))

    # header
    header = f' '*4
    for t in self.columns:
      header += f'{t.lower().capitalize():{COLUMN_FORMATS[t.lower()]}}'
    click.echo(click.style(header, fg='green', bold=True))
    
    # data
    for idx, c in enumerate(self.commits):
      if not c.transferred:
        line = f'{idx:{COLUMN_FORMATS["idx"]}}'
        for t in self.columns:
          line += f'{getattr(c, t):{COLUMN_FORMATS[t.lower()]}}'
        click.echo(line)
      else:
        click.echo(click.style(line, fg='red'))

    # footer
    click.echo(click.style('-'*68, fg='green', bold=True))
    pushable = sum(map(lambda x: not x.transferred, self.commits))
    click.echo(f'{pushable} total changes that can be transferred (red ones will be ignored)\n')
    return pushable

  def summary(self, pushable):
    # total summary
    click.echo(click.style('-'*68, fg='green', bold=True))
    click.echo('Summary:')
    click.echo(f'- Total repositorys listed: {len(self.git_dirs)}')
    click.echo(f'- {pushable} total changes that can be transferred (red ones will be ignored)')
    click.echo('Execute the same statement without --list flag for transferring these commits.')
