#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple basic test for JSON"""

import unittest
import os

from crappyspider.spiders.crappyspider import CrappySpider


class CrappySpiderTestCase(unittest.TestCase):
    """Basic test class with simple test"""

    def test_without_arg(self):
        """Test initialize withtout argument."""
        self.failUnlessRaises(ValueError, CrappySpider)

    def test_with_insufficient_arg(self):
        """Test with insufficient argument."""
        config = None
        output_format = 'json'
        output_filename = 'output'
        start_urls = 'http://test.com'
        self.failUnlessRaises(ValueError, CrappySpider, config, output_format,
                              output_filename, start_urls)

    def test_allowed_domain(self):
        """Test with insufficient argument."""
        config = None
        output_format = 'json'
        output_filename = 'output'
        start_urls = None
        allowed_domains = 'test.com'
        self.failUnlessRaises(ValueError, CrappySpider, config, output_format,
                              output_filename, start_urls, allowed_domains)

    def test_unsupported_format(self):
        """Test with unsupported format"""
        config = None
        output_format = 'format'
        output_filename = 'output'
        start_urls = 'http://test.com'
        allowed_domains = 'test.com'
        self.failUnlessRaises(ValueError, CrappySpider, config, output_format,
                              output_filename, start_urls, allowed_domains)

    def test_output_filename_default(self):
        """Test with insufficient argument."""
        start_urls = 'http://test.com'
        allowed_domains = 'test.com'
        crappyspider = CrappySpider(start_urls=start_urls,
                                    allowed_domains=allowed_domains)
        output_filename = '{current_directory}/output.{ext}'.format(
            current_directory=os.getcwd(), ext='json')

        self.assertEqual(crappyspider.output_filename, output_filename)

    def test_output_filename(self):
        """Test with insufficient argument."""
        start_urls = 'http://test.com'
        allowed_domains = 'test.com'
        output_filename = 'name'
        crappyspider = CrappySpider(output_filename=output_filename,
                                    start_urls=start_urls,
                                    allowed_domains=allowed_domains)

        self.assertEqual(crappyspider.output_filename, 'name')
