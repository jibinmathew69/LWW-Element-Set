'''
This module contains the (Last-Write-Wins)LWW-element-set class
from (Conflict-free Replicated Data Types)CRDT
'''

class Lww:
    '''
    LWW class for CRDTs
    '''
    def __init__(self):
        self.add_set = {}
        self.remove_set = {}

    def add(self, element):
        '''
        This method adds the element into the add_set dictionary
        of the Lww, where key is the element and value is the current unix timestamp
        :param element: Element to be add into LWW
        :return: None
        '''
        pass
