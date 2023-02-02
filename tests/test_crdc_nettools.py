#!/usr/bin/env python

"""Tests for `crdc_nettools` package."""


import unittest

from crdc_nettools import crdc_nettools


class TestCrdc_nettools(unittest.TestCase):
    """Tests for `crdc_nettools` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_dummy(self):
        """Test dummuy"""
        test = crdc_nettools.DummyTest()
        assert test.test()
