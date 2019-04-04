# LWW-Element-Set
LWW Element Set is an algorithm under Conflict-free replicated data type(CRDT) , here is the Python implementation.

###<b>LWW-Element-Set (Last-Write-Wins-Element-Set)</b><br />

LWW-Element-Set is similar to 2P-Set in that it consists of an "add set" and a "remove set", with a timestamp for each element. Elements are added to an LWW-Element-Set by inserting the element into the add set, with a timestamp. Elements are removed from the LWW-Element-Set by being added to the remove set, again with a timestamp. An element is a member of the LWW-Element-Set if it is in the add set, and either not in the remove set, or in the remove set but with an earlier timestamp than the latest timestamp in the add set. Merging two replicas of the LWW-Element-Set consists of taking the union of the add sets and the union of the remove sets. When timestamps are equal, the "bias" of the LWW-Element-Set comes into play. A LWW-Element-Set can be biased towards adds or removals. The advantage of LWW-Element-Set over 2P-Set is that, unlike 2P-Set, LWW-Element-Set allows an element to be reinserted after having been removed.

#### Methods
* `add` : Add a new element to LWW
* `remove` : Remove element from LWW
* `lookup` : Checks for the presence of an element in LWW
* `compare` : Checks if the given Lww is subset of another LWW
* `merge` : Merges 2 LWW and returns a new LWW

#### Installation

Run the following command before using the code: <br />
`pip install -r requirements.txt`

#### Running Test
Run the following code from the Project root: <br />
`pytest`<br />

For test coverage run from the Project root: <br />
`pytest --cov=LWW tests/`

`100%` Test coverage achieved.

#### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

#### Note : 
The code exploits the internal GIL available for built-in datatypes in Python and achieves,
further sychronization using `RLock()` in Python. 

 #### Future Improvements
 The bias factor, for preference between add and remove is not implemented, and needs to be done.