import argparse
import jinja2
import jinja2.loaders

class BaseApp (object):
    def __init__(self):
        self._env = jinja2.Environment(
            loader=jinja2.loaders.PackageLoader('ansible_toolbox', 'templates'))

    def get_template(self, template):
        return self._env.get_template(template)

    def build_argument_parser(self):
        p = argparse.ArgumentParser()
        p.add_argument('--verbose', '-v',
                       action='count',
                       default=0)

        p.add_argument('--gather', '-g',
                       action='store_true')
        p.add_argument('--no-gather', '-G',
                       action='store_false',
                       dest='gather')
        p.add_argument('--extra-vars', '-e',
                       action='append',
                       default=[])
        p.add_argument('--connection', '-c')

        g = p.add_argument_group('Inventory')
        g.add_argument('-i', '--inventory')
        g.add_argument('--hosts', '-H',
                       default='localhost')

        g = p.add_argument_group('Identity')
        g.add_argument('--sudo', '-s',
                       action='store_true',
                       dest='become')
        g.add_argument('--become', '-b',
                       action='store_true')
        g.add_argument('--user', '-u')
        g.add_argument('--ask-become-pass', '-K',
                       action='store_true')

        p.set_defaults(gather=True)
        return p

    def parse_args(self):
        p = self.build_argument_parser()
        return p.parse_args()

    def build_command_line(self, args):
        cmd = []

        ap_args = [('-e', x) for x in args.extra_vars]
        if args.inventory:
            cmd.extend(('-i', args.inventory))

        if args.become:
            cmd.append('-b')
            
        if args.ask_become_pass:
            cmd.append('-K')

        if args.user:
            cmd.extend(('-u', args.user))

        if args.connection:
            cmd.extend(('-c', args.connection))

        for i in range(args.verbose):
            cmd.append('-v')

        for arg in ap_args:
            cmd.extend(arg)

        return cmd

