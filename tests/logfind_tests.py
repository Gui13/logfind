from nose.tools import *
from bin.logfind import *

def test_pref_file():
    files = read_prefs('./tests/testfiles/test_prefs.logfind')
    assert_equal(files,['./tests/testfiles/logs1'])

def test_pref_glob():
    files = read_prefs('./tests/testfiles/test_prefs_all.logfind')
    assert_equal(files,['./tests/testfiles/subdir1/sub1-2.log', './tests/testfiles/subdir1/sub1.log', './tests/testfiles/subdir2/sub2-2.log', './tests/testfiles/subdir2/sub2.log'])

def test_pref_glob_pattern():
    files = read_prefs('./tests/testfiles/test_prefs_specific.logfind')
    assert_equal(files,['./tests/testfiles/subdir1/sub1-2.log', './tests/testfiles/subdir2/sub2-2.log'])