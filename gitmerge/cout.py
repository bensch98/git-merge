import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand

COLUMN_FORMATS = {
  'hexsha': '<42',
  'date': '<27',
  'message': '<20',
  'idx': '<4'
}

class Cout:
  def __init__(self, merger, commits, git_dirs, columns=('hexsha', 'date', 'message'), show_msg=False):
    self.merger = merger
    self.commits = commits
    self.git_dirs = git_dirs
    self.columns = columns
    self.show_msg = show_msg

  def list(self):

    click.echo(click.style(f'Repository: {self.merger.src_name}', fg='blue', bold=True))

    # create header
    header = f' '*4
    for t in self.columns:
      header += f'{t.lower().capitalize():{COLUMN_FORMATS[t.lower()]}}'
    click.echo(click.style(header, fg='green', bold=True))

    for idx, c in enumerate(self.commits):
      if not c.transferred:
        line = f'{idx:{COLUMN_FORMATS["idx"]}}'
        for t in self.columns:
          line += f'{getattr(c, t):{COLUMN_FORMATS[t.lower()]}}'
        click.echo(line)
      else:
        click.echo(click.style(line, fg='red'))

    click.echo(click.style('---------------------------------------------------------', fg='green', bold=True))
    pushable = sum(map(lambda x: not x.transferred, self.commits))
    click.echo(f'{pushable} total changes that can be transferred (red ones will be ignored\n')
    click.echo(f'Total repositorys listed: {len(self.git_dirs)}')
    click.echo('Execute the same statement without --list flag for transferring these commits.')
