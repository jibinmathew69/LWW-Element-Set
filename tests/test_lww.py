'''
This file contains tests for Lww class from LWW.lww module
'''

from LWW.lww import Lww

def test_add():
    '''
    This functions test the successful addition of the element
    into the LWW
    :return: None
    '''

    lww = Lww()

    lww.add(1)

    assert lww.lookup(1)
