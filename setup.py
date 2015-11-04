from setuptools import setup, find_packages

with open('requirements.txt') as fd:
    setup(name='ansible-toolbox',
          author='Lars Kellogg-Stedman',
          author_email='lars@redhat.com',
          url='https://github.com/larsks/ansible-role',
          version='1.0',
          install_requires=fd.readlines(),
          packages=find_packages(),
          package_data={'ansible_toolbox': [
              'ansible_toolbox/templates/*'
          ]},
          entry_points={'console_scripts': [
              'ansible-role = ansible_toolbox.cmd.role:main',
              'ansible-task = ansible_toolbox.cmd.task:main',
              'ansible-eval = ansible_toolbox.cmd.eval:main',
          ]},
          )
