This script allows you to run an [Ansible][] role from the command line.

[ansible]: http://ansible.com/

For example, if you have a role `roles/testrole`, you can run it on
localhost like this:

    ansible-role -i localhost, testrole

The `ansible-role` script accepts the following options:

- `--inventory`, `-i` *inventory* -- Like the corresponding `ansible`
  option
- `--extra-vars, `-e` *vars* -- Like the corresponding `ansible` option
- `--hosts`, `-h` *hosts*  -- The value of this argument will be applied
  to the `hosts:` line in the generated playbook.  Defaults to `all`.
- `--gather`, `-g` -- Enable fact gathering (this is the default)
- `--no-gather`, `-G` -- Disable fact gathering
