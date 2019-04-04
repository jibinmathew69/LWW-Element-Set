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
    lww.add("test_element")

    assert lww.lookup(1)
    assert lww.lookup("test_element")
    assert not lww.lookup("test")


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

def test_add_exception(caplog):
    '''
    This function test the exception handling of the add
    :param caplog: pytest fixture
    :return: None
    '''

    lww = Lww()
    lww.add([1, 2, 3])

    assert "unhashable type: 'list'" in caplog.text


def test_remove_exception(caplog):
    '''
    This function test the exception handling of the add
    :param caplog: pytest fixture
    :return: None
    '''

    lww = Lww()
    lww.remove({})

    assert "unhashable type: 'dict'" in caplog.text


def test_key_internal():
    '''
    This function validates the state of the elements in Lww
    :return: None
    '''
    lww = Lww()

    lww.add(1)
    lww.add(2)
    lww.add(3)
    lww.remove(4)
    lww.remove(2)

    assert {1, 2, 3}.issubset(lww.add_set.keys())
    assert {2, 4}.issubset(lww.remove_set.keys())

    assert 4 not in lww.add_set.keys()
    assert 1 not in lww.remove_set.keys()
    assert 3 not in lww.remove_set.keys()


def test_value_internal():
    lww = Lww()

    lww.add(1)
    lww.add(2)
    lww.add(3)
    lww.remove(4)
    lww.remove(2)

    assert lww.remove_set[2] > lww.add_set[2]
    assert lww.add_set[3] > lww.add_set[2]
    assert lww.remove_set[4] > lww.add_set[3]
    assert lww.remove_set[2] > lww.remove_set[4]
