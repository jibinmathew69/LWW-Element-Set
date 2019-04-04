'''
This module contains the (Last-Write-Wins)LWW-element-set class
from (Conflict-free Replicated Data Types)CRDT
'''

import time
from threading import RLock
from config.log_config import LOGGER


class Lww:
    '''
    LWW class for CRDTs
    '''
    def __init__(self):
        self.add_set = {}
        self.remove_set = {}
        self.add_lock = RLock()
        self.remove_lock = RLock()

    def add(self, element):
        '''
        This method adds the element into the add_set dictionary
        of the Lww, where key is the element and value is the current unix timestamp
        :param element: Element to be add into LWW
        :return: None
        '''

        with self.add_lock:
            try:
                if self.add_set.get(element, 0) < time.time():
                    self.add_set[element] = time.time()
            except TypeError as error:
                LOGGER.error(str(error))


    def lookup(self, element):
        '''
        This method check whether a given element is in LWW
        :param element: Element whose presence is the checked in LWW
        :return: Boolean
        '''

        with self.add_lock, self.remove_lock:
            if element not in self.add_set:
                # Element not in add_set
                return False

            if element not in self.remove_set:
                # Element in add_set and not in remove_set
                return True

            if self.remove_set[element] < self.add_set[element]:
                # Element in both add_set and remove_set, but addition is after removal
                return True

            # Element in both add_set and remove_set, but addition is before removal
            return False


    def remove(self, element):
        '''
        This method removes the element from the LWW
        :param element: Element to be removed
        :return: None
        '''

        with self.remove_lock:
            try:
                if self.remove_set.get(element, 0) < time.time():
                    self.remove_set[element] = time.time()
            except TypeError as error:
                LOGGER.error(str(error))




    def compare(self, other):
        '''
        This method checks whether the LWW is subset of the given LWW
        :param other: LWW object to be compared with
        :return: Boolean
        '''

        with self.add_lock, self.remove_lock, other.add_lock, other.remove_lock:

            # Check add_set is subset of other.add_set
            add_subset = set(self.add_set.keys()).issubset(other.add_set.keys())

            # Check remove_set is subset of other.remove_set
            remove_subset = set(self.remove_set.keys()).issubset(other.remove_set.keys())


        return add_subset and remove_subset

    def merge(self, other):
        '''
        This method merge the LWW with the given LWW and returns a new LWW
        without affecting the original LWW
        :param other:
        :return: Lww
        '''

        lww = Lww()

        with self.add_lock, self.remove_lock, other.add_lock, other.remove_lock:

            # Merge add_set
            lww.add_set = {**self.add_set, **other.add_set}

            # Merge remove_set
            lww.remove_set = {**self.remove_set, **other.remove_set}

            # Update lww with latest timestamp in add_set
            for element, timestamp in self.add_set.items():
                lww.add_set[element] = max(lww.add_set[element], timestamp)

            # Update lww with latest timestamp in remove_set
            for element, timestamp in self.remove_set.items():
                lww.remove_set[element] = max(lww.remove_set[element], timestamp)


        return lww
