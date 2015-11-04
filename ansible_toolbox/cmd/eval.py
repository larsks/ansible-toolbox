from __future__ import absolute_import

import sys
import logging
import tempfile
import subprocess

from ansible_toolbox.base import BaseApp

LOG = logging.getLogger(__name__)


class App (BaseApp):
    def build_argument_parser(self):
        p = super(App, self).build_argument_parser()
        p.add_argument('expr')
        return p

    def main(self):
        args = self.parse_args()
        template = self.get_template('eval.yml')

        with tempfile.NamedTemporaryFile(dir='.') as tmplfd:
            tmplfd.write(template.render(
                expr=args.expr,
                hosts=args.hosts,
                gather=args.gather,
            ))

            tmplfd.flush()

            cmd = ['ansible-playbook', tmplfd.name]
            cmd.extend(self.build_command_line(args))
            subprocess.check_call(cmd)


def main():
    App().main()
