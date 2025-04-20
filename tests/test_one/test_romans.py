# testing collections
# 20/11/2020

import unittest

from pack_one.romans import *

class romansTest(unittest.TestCase):

    def testRomans(self):
        toRoman, fromRoman = romanfunc()

        self.assertEqual('I', toRoman(1))
        self.assertEqual('CI', toRoman(101))

        self.assertEqual(1, fromRoman('I'))
        self.assertEqual(100, fromRoman('C'))









