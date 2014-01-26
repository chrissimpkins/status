#!/usr/bin/env python

import unittest
import subprocess

from status.commands.http_request import Get, Post, prepare_url
from Naked.toolshed.shell import run
from requests.exceptions import ConnectionError

class StatusTests(unittest.TestCase):
    def setUp(self):
        self.get_status200 = 'http://httpbin.org/status/200'
        self.get_status301 = 'http://httpbin.org/status/301'
        self.get_status404 = 'http://httpbin.org/status/404'
        self.get_noprotocol = 'httpbin.org/status/200'
        self.get_ssl_protocol = 'https://httpbin.org/status/200'

        self.post_status200 = 'http://httpbin.org/post'
        self.post_noprotocol = 'httpbin.org/post'
        self.post_ssl_protocol = 'https://httpbin.org/post'

        self.bogus_url = 'http://www.thisisabogusurl.io'

        self.string_301 = """
301 : http://httpbin.org/status/301
302 : http://httpbin.org/redirect/1
200 : http://httpbin.org/get
        """
    def tearDown(self):
        pass

    #------------------------------------------------------------------------------
    # GET tests
    #------------------------------------------------------------------------------
    def test_get_status200_with_protocol(self):
        """Test that a status 200 is appropriately returned with GET"""
        response = run("status " + self.get_status200)
        self.assertEqual(response.strip().decode('ascii'), '200 : http://httpbin.org/status/200')

    def test_get_status301_with_protocol(self):
        """Test that a status 301 and bounces are appropriately returned with GET"""
        response = run("status " + self.get_status301)
        self.assertEqual(response.strip().decode('ascii'), self.string_301.strip())

    def test_get_status404_with_protocol(self):
        """Test that a status 404 is appropriately returned with GET"""
        response = run("status " + self.get_status404)
        self.assertEqual(response.strip().decode('ascii'), '404 : http://httpbin.org/status/404')

    def test_get_status200_without_protocol(self):
        """Test that a status 200 is returned appropriately when no protocol included"""
        response = run("status " + self.get_noprotocol)
        self.assertEqual(response.strip().decode('ascii'), '200 : http://httpbin.org/status/200')

    def test_get_status200_ssl_protocol(self):
        """Test that a status 200 is returned appropriately with SSL protocol"""
        response = run("status " + self.get_ssl_protocol)
        self.assertEqual(response.strip().decode('ascii'), '200 : https://httpbin.org/status/200')

    def test_get_status_absent_site(self):
        """Test that absent site raises a CalledProcessError exception"""
        with self.assertRaises(subprocess.CalledProcessError):
            command = "status " + self.bogus_url
            response = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            self.assertEqual(response.strip().decode('ascii'), 'Unable to connect to the URL, http://www.thisisabogusurl.io')

    #------------------------------------------------------------------------------
    # POST tests
    #------------------------------------------------------------------------------
    ## TODO: find URL for non-200 response codes
    def test_post_p_status200_with_protocol(self):
        """Test that a status 200 is appropriately returned with POST using the -p option"""
        response = run("status -p " + self.post_status200)
        self.assertEqual(response.strip().decode('ascii'), '200 : http://httpbin.org/post')

    def test_post_post_status200_with_protocol(self):
        """Test that a status 200 is appropriately returned with POST using the --post option"""
        response = run("status --post " + self.post_status200)
        self.assertEqual(response.strip().decode('ascii'), '200 : http://httpbin.org/post')

    def test_post_p_status200_without_protocol(self):
        """Test that a status 200 is appropriately returned with POST using -p and no protocol"""
        response = run("status -p " + self.post_noprotocol)
        self.assertEqual(response.strip().decode('ascii'), '200 : http://httpbin.org/post')

    def test_post_post_status200_without_protocol(self):
        """Test that a status 200 is appropriately returned with POST using --post and no protocol"""
        response = run("status --post " + self.post_noprotocol)
        self.assertEqual(response.strip().decode('ascii'), '200 : http://httpbin.org/post')

    def test_post_p_status200_ssl(self):
        """Test that a status 200 is appropriately returned with POST using -p and https://"""
        response = run("status -p " + self.post_ssl_protocol)
        self.assertEqual(response.strip().decode('ascii'), '200 : https://httpbin.org/post')

    def test_post_post_status200_ssl(self):
        """Test that a status 200 is appropriately returned with POST using --post and https://"""
        response = run("status --post " + self.post_ssl_protocol)
        self.assertEqual(response.strip().decode('ascii'), '200 : https://httpbin.org/post')

    def test_post_p_status_absent_site(self):
        """Test that absent site raises a CalledProcessError exception with -p"""
        with self.assertRaises(subprocess.CalledProcessError):
            command = "status -p " + self.bogus_url
            response = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            self.assertEqual(response.strip().decode('ascii'), 'Unable to connect to the URL, http://www.thisisabogusurl.io')

    def test_post_post_status_absent_site(self):
        """Test that absent site raises a CalledProcessError exception with --post"""
        with self.assertRaises(subprocess.CalledProcessError):
            command = "status --post " + self.bogus_url
            response = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            self.assertEqual(response.strip().decode('ascii'), 'Unable to connect to the URL, http://www.thisisabogusurl.io')

