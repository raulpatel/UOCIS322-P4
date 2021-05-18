"""
Nose tests for acp_times.py
"""
from acp_times import *

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_zero_distance():
    assert open_time(0, 0, arrow.get('1970-01-01T00:00:00.000Z')).format('YYYY-MM-DDTHH:mm') == '1970-01-01T00:00'
    assert close_time(0, 0, arrow.get('1970-01-01T00:00:00.000Z')).format('YYYY-MM-DDTHH:mm') == '1970-01-01T00:00'



def test_too_far():
    assert open_time(1, 0, arrow.get("1970-01-01T00:00:00.000Z")) == None
    assert close_time(1, 0, arrow.get('1970-01-01T00:00:00.000Z')) == None


def test_small_vocab():
    assert True


def test_from_simulated_file():
    assert True

def test_last():
    assert True
