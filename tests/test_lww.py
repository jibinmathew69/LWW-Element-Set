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


def test_remove():
    '''
    This function test the successful removal of the element
    from the LWW
    :return: None
    '''

    lww = Lww()

    lww.remove(1)
    assert not lww.lookup(1)

    lww.add(1)
    assert lww.lookup(1)
