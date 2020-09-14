#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implements a test fixture for the echo.py module

Students MUST EDIT this module, to add more tests to run
against the 'echo.py' program.
"""

__author__ = """Greg Spurgeon with help from JT(facilitator)"""

import sys
import importlib
import argparse
import unittest
import subprocess

# devs: change this to 'soln.echo' to run this suite against the solution
PKG_NAME = 'echo'

# suppress __pycache__ and .pyc files
sys.dont_write_bytecode = True


# Students should use this function in their tests
def run_capture(pyfile, args=()):
    """
    Runs a python program in a separate process,
    returns the output lines as a list.
    """
    cmd = ["python", pyfile]
    cmd.extend(args)
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True
        )
        output = result.stdout.decode()
    except subprocess.CalledProcessError as err:
        output = err.stdout.decode()
    assert output, "Nothing was printed!"
    return output.splitlines()


# Students: complete this TestEcho class so that all tests run and pass.
class TestEcho(unittest.TestCase):
    """Main test fixture for 'echo' module"""
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested (the student's echo.py)
        cls.module = importlib.import_module(PKG_NAME)

    def test_parser(self):
        """Check if create_parser() returns a parser object"""
        result = self.module.create_parser()
        self.assertIsInstance(
            result, argparse.ArgumentParser,
            "create_parser() function is not returning a parser object")

    def test_parser_namespace(self):
        """Check if parser creates correct namespace"""
        p = self.module.create_parser()
        ns = p.parse_args(["-l", "hello"])
        self.assertTrue(ns.lower)
        self.assertFalse(ns.upper)
        self.assertFalse(ns.title)
        self.assertEqual(ns.text, "hello")

    def test_echo(self):
        """Check if main() function prints anything at all"""
        module_to_test = self.module.__file__
        run_capture(module_to_test)

    def test_simple_echo(self):
        """Check if main actually echoes an input string"""
        args = ['Was soll die ganze Aufregung?']
        output = run_capture(self.module.__file__, args)
        self.assertEqual(
            output[0], args[0],
            "The program is not performing simple echo"
            )

    def test_lower_short(self):
        """Check if short option '-l' performs lowercasing"""
        args = ["-l", "HELLO WORLD"]
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "hello world")

    def test_lower_long(self):
        """Check if short option '--lower' performs lowercasing"""
        args = ['--lower', 'HELLO WORLD']
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "hello world")

    def test_upper_short(self):
        """Check if short option '-u' performs uppercasing"""
        args = ['-u', 'hello world']
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "HELLO WORLD")

    def test_upper_long(self):
        """Check if short option '--upper' performs uppercasing"""
        args = ['--upper', 'hello world']
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "HELLO WORLD")

    def test_title_short(self):
        """Check if short option '-t' performs  titel casing"""
        args = ['-t', 'hello world']
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "Hello World")

    def test_title_long(self):
        """Check if short option '--title' performs  titel casing"""
        args = ['--title', 'hello world']
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "Hello World")

    def test_multiple_options(self):
        """"Checks to see if options are applied in order of usage"""
        args = ['-ult', 'hello world']
        output = run_capture(self.module.__file__, args)
        self.assertEqual(output[0], "Hello World")

    def test_help_message(self):
        """If -h is passed, show usage"""
        args = ['-h']
        output = run_capture(self.module.__file__, args)
        with open("./USAGE", "r") as f:
            usage = f.read().splitlines()

        self.assertListEqual(output, usage)

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)

    def test_author(self):
        """Checking for author string"""
        self.assertIsNotNone(self.module.__author__)
        self.assertNotEqual(
            self.module.__author__, "???",
            "Author string is not completed"
            )


if __name__ == '__main__':
    unittest.main()
