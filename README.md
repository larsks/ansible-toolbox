This script allows you to run an [Ansible][] role from the command line.

[ansible]: http://ansible.com/

For example, if you have a role `roles/testrole`, you can run it on
localhost like this:

    ansible-role -i localhost, testrole

The following options are unique to the `ansible-role` command:

- `--hosts`, `-h` *hosts*  -- The value of this argument will be applied
  to the `hosts:` line in the generated playbook.  Defaults to `all`.
- `--gather`, `-g` -- Enable fact gathering (this is the default)
- `--no-gather`, `-G` -- Disable fact gathering

The following additional options are simply proxies to the equivalent
`ansible-playbook` options:

- `--verbose`, `-v`
- `--sudo`, `-s`
- `--become`, `-b`
- `--user`, `-u` *user*
- `--inventory`, `-i` *inventory*
- `--extra-vars`, `-e` *vars*
