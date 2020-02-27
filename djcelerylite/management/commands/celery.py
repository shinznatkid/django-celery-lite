from celery.bin import celery

from ...celery_app import app
from ..base import CeleryCommand

base = celery.CeleryCommand(app=app)


class Command(CeleryCommand):
    """The celery command."""
    help = 'celery commands, see celery help'
    options = (
        tuple(CeleryCommand.options) +
        tuple(base.get_options() or ()) +
        tuple(getattr(base, 'preload_options', ()))
    )

    def run_from_argv(self, argv):
        argv = self.handle_default_options(argv)
        base.execute_from_commandline(
            ['{0[0]} {0[1]}'.format(argv)] + argv[2:],
        )
