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


def test_compare():
    '''
    This function test the compare method of Lww
    :return: None
    '''

    lww1 = Lww()
    lww2 = Lww()

    lww1.add(1)
    lww1.add(2)

    lww2.add(1)
    lww2.add(2)
    lww2.add(3)

    lww1.remove(1)
    lww1.remove(2)

    lww2.remove(1)
    lww2.remove(2)
    lww2.remove(3)

    assert lww1.compare(lww2)

    assert not lww2.compare(lww1)


def test_merge():
    '''
    This function test the merge method of Lww
    :return: None
    '''

    lww1 = Lww()
    lww2 = Lww()

    lww1.add(1)
    lww1.add(2)
    lww1.remove(1)

    lww2.add(1)
    lww2.add(3)

    lww1.remove(3)

    lww2.remove(1)

    lww = lww1.merge(lww2)

    assert {1, 2, 3}.issubset(lww.add_set.keys())
    assert {1, 3}.issubset(lww.remove_set.keys())
    assert lww.add_set[1] == lww2.add_set[1]
    assert lww.add_set[1] > lww1.add_set[1]
    assert lww.add_set[3] < lww1.remove_set[3]
    assert lww.remove_set[1] == lww2.remove_set[1]
