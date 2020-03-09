#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  26 09:30:09 2020

@author: sachinmcreddy
"""

<<<<<<< Updated upstream
import unittest
=======
import unittest 
from unittest import mock
>>>>>>> Stashed changes

from HW4567 import repo_info


class TestGetInfo(unittest.TestCase):
    def test_normal_response(self):
        expected = ['User: SachinMCReddy',
                    'Repo: test1 Number of commits: 4',
                    'Repo: test2 Number of commits: 2',
                    'Repo: Triangle567 Number of commits: 3']
        self.assertEqual(repo_info(), expected)
<<<<<<< Updated upstream

=======
    @mock.patch("urlib.request.urlopen")
>>>>>>> Stashed changes
    def test_bad_user_name(self):
        self.assertEqual(repo_info('xxxxxxx'), 'not able to fetch repos from user')
        self.assertEqual(repo_info(''), 'not able to fetch repos from user')


if __name__ == '__main__':
    unittest.main()