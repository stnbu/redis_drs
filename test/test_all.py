# -*- coding: utf-8 -*-

import redis_drs

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class TestAll(unittest.TestCase):

    def setUp(self):
        self.locker = redis_drs.Locker(resource_signature='myresourcesig')

    def test_all(self):
        self.locker.lock(resource_info={'bob', 'mary'})
        self.locker.get()
        self.locker.update({'7':99})
        self.locker.get()
        self.locker.unlock()

if __name__ == '__main__':
   unittest.main()
