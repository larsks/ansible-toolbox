from __future__ import absolute_import

import contextlib
import logging
import os
import subprocess
import sys
import tempfile

from ansible_toolbox.base import BaseApp

LOG = logging.getLogger(__name__)


@contextlib.contextmanager
def temporary_file(*args, **kwargs):
    '''Return a temporary filename.

    Generate a temporary filename, return it to the caller, and clean it up
    when done.  Unlike tempfile.NamedTemporaryFile and friends, you only get
    back a filename rather than a file object.
    '''
    name = tempfile.mktemp(*args, **kwargs)
    yield name
    os.unlink(name)


class EvalApp (BaseApp):
    '''Evaluate a Jinja2 template and display the result.'''

    def build_argument_parser(self):
        p = super(EvalApp, self).build_argument_parser()
        p.add_argument('expr')
        return p

    def main(self, args):
        template = self.get_template('eval.yml')

        with tempfile.NamedTemporaryFile(dir='.', suffix='.yml') as tmplfd, \
                temporary_file(dir='.') as output:
            playbook = template.render(
                    expr=args.expr,
                    hosts=args.hosts,
                    gather=args.gather,
                    output=output,
            )

            LOG.debug('playbook: %s', playbook)
            tmplfd.write(playbook.encode('utf-8'))
            tmplfd.flush()

            cmd = ['ansible-playbook', tmplfd.name]
            cmd.extend(self.build_command_line(args))
            LOG.debug('running command: %s', cmd)
            subprocess.check_output(cmd)
            with open(output, 'r') as fd:
                sys.stdout.write(fd.read())
                sys.stdout.write('\n')


app = EvalApp()


def main():
    app.run()
