import os
import shutil
import tempfile
import unittest


class BaseTestCase (unittest.TestCase):
    def setup_method(self, method):
        self.workdir = tempfile.mkdtemp(prefix='test')
        self.origdir = os.path.abspath(os.getcwd())
        os.chdir(self.workdir)

        with open('ansible.cfg', 'w') as fd:
            fd.write('[defaults]\n')
            fd.write('local_tmp = %s/tmp/local\n' % self.workdir)
            fd.write('remote_tmp = %s/tmp/remote\n' % self.workdir)

    def teardown_method(self, method):
        os.chdir(self.origdir)
        shutil.rmtree(self.workdir)
