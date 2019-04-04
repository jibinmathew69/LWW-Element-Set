'''
This module contains the (Last-Write-Wins)LWW-element-set class
from (Conflict-free Replicated Data Types)CRDT
'''

import time
from threading import RLock

class Lww:
    '''
    LWW class for CRDTs
    '''
    def __init__(self):
        self.add_set = {}
        self.remove_set = {}
        self.lock = RLock()

    def add(self, element):
        '''
        This method adds the element into the add_set dictionary
        of the Lww, where key is the element and value is the current unix timestamp
        :param element: Element to be add into LWW
        :return: None
        '''
        self.lock.acquire()
        if self.add_set.get(element, 0) < time.time():
            self.add_set[element] = time.time()
        self.lock.release()

    def lookup(self, element):
        '''
        This method check whether a given element is in LWW
        :param element: Element whose presence is the checked in LWW
        :return: Boolean
        '''

        return element in self.add_set

    def remove(self, element):
        '''
        This method removes the element from the LWW
        :param element: Element to be removed
        :return: None
        '''

        self.lock.acquire()
        if self.remove_set.get(element, 0) < time.time():
            self.remove_set[element] = time.time()
        self.lock.release()
