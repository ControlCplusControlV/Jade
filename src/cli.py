import click
from jade import *

@click.command()
@click.option('--path', default="./", help='The path to the directory containing the contracts to mutate.')
def main(path):
    project = Project(path, ['forge', 'test'])
    project.run_tests()

if __name__ == '__main__':
    main()