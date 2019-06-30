#!/usr/bin/env python3

import time
import unittest
from selenium import webdriver


class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
        self.browser.save_screenshot('google_scr.png')


class ConsulTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://demo.consul.io/ui/dc1/services')
        time.sleep(2)
        self.assertIn('Consul', self.browser.title)
        self.browser.save_screenshot('consul_services.png')
        self.browser.get('https://demo.consul.io/ui/dc1/nodes')
        time.sleep(2)
        self.browser.save_screenshot('consul_nodes.png')


if __name__ == '__main__':
    unittest.main(verbosity=2)
