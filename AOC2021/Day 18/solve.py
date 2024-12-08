import json
from math import floor, ceil, inf
from typing import Self

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

class Num:
    DEPTH_LIMIT = 4 # The max depth where a value should be, before it is in a pair that needs to explode
    VALUE_LIMIT = 9

    # parent, leftChild, rightChild, value, depth
    def __init__(self, value):
        if isinstance(value, list):
            self.parent = None
            self.depth = 0
            self.value = None
            self._setLeftChild(Num(value[0]))
            self._setRightChild(Num(value[1]))
        elif isinstance(value, int):
            self.parent = None
            self.depth = 0
            self.value = value
            self.leftChild = None
            self.rightChild = None
        elif isinstance(value, tuple):
            self.parent = None
            self.depth = 0
            self.value = None
            self._setLeftChild(value[0])
            self._setRightChild(value[1])
        else:
            raise Exception("Unknown value type")
    
    def _setDepth(self, d: int):
        self.depth = d
        if not self._isValue():
            self._getLeftChild()._setDepth(d + 1)
            self._getRightChild()._setDepth(d + 1)

    def _getDepth(self) -> int:
        return self.depth

    def _setParent(self, p: Self):
        self.parent = p
        self._setDepth(p._getDepth() + 1)

    def _getParent(self) -> Self:
        return self.parent

    def _setLeftChild(self, c: Self):
        self.leftChild = c
        if c != None:
            c._setParent(self)

    def _getLeftChild(self) -> Self:
        return self.leftChild

    def _setRightChild(self, c: Self):
        self.rightChild = c
        if c != None:
            c._setParent(self)

    def _getRightChild(self) -> Self:
        return self.rightChild

    def _getLeftLeaf(self) -> Self:
        common_ancestor = self._getParent()
        curr_node = self
        while common_ancestor != None and curr_node == common_ancestor._getLeftChild():
            curr_node = common_ancestor
            common_ancestor = curr_node._getParent()

        if common_ancestor == None: return None

        result = common_ancestor._getLeftChild()
        while not result._isValue():
            result = result._getRightChild()
        return result

    def _getRightLeaf(self) -> Self:
        common_ancestor = self._getParent()
        curr_node = self
        while common_ancestor != None and curr_node == common_ancestor._getRightChild():
            curr_node = common_ancestor
            common_ancestor = curr_node._getParent()

        if common_ancestor == None: return None

        result = common_ancestor._getRightChild()
        while not result._isValue():
            result = result._getLeftChild()
        return result

    def _setValue(self, value: int):
        self.value = value

    def _getValue(self) -> int:
        return self.value

    def _isValue(self) -> bool:
        return self.value != None

    def _shouldExplode(self) -> bool:
        if self._isValue():
            return self._getDepth() > Num.DEPTH_LIMIT
        else:
            return self._getLeftChild()._shouldExplode()  or self._getRightChild()._shouldExplode()

    def _explode(self):
        if not self._isValue():
            if self._getDepth() == Num.DEPTH_LIMIT: # Child Num will exceed limit
                lv = self._getLeftChild()._getValue()
                rv = self._getRightChild()._getValue()
                self._setLeftChild(None)
                self._setRightChild(None)
                self._setValue(0)

                ll = self._getLeftLeaf()
                rl = self._getRightLeaf()
                if ll != None:
                    ll._setValue(ll._getValue() + lv)
                if rl != None:
                    rl._setValue(rl._getValue() + rv)
            else:
                lc = self._getLeftChild()
                if lc._shouldExplode():
                    lc._explode()
                else:
                    rc = self._getRightChild()
                    rc._explode()
        else:
            raise Exception("Exploding a value")

    def _shouldSplit(self) -> bool:
        if self._isValue():
            return self._getValue() > Num.VALUE_LIMIT
        else:
            return self._getLeftChild()._shouldSplit() or self._getRightChild()._shouldSplit()

    def _split(self):
        if self._isValue():
            # Split called on a value, do splitting
            lc = Num(floor(self.value / 2))
            rc = Num(ceil(self.value / 2))
            self._setLeftChild(lc)
            self._setRightChild(rc)
            self._setValue(None)
        else:
            # Split called on a pair, find the number that should split (left-most prioritized)
            lc = self._getLeftChild()
            if lc._shouldSplit():
                lc._split()
            else:
                rc = self._getRightChild()
                rc._split()

    def _reduce(self):
        while True:
            if self._shouldExplode():
                self._explode()
            elif self._shouldSplit():
                self._split()
            else:
                break

    def add(self, num) -> Self:
        new_num = Num((self, num))
        new_num._reduce()
        return new_num

    def getMagnitude(self):
        if self._isValue():
            return self._getValue()
        else:
            return 3 * self._getLeftChild().getMagnitude() + 2 * self._getRightChild().getMagnitude()
        
    def __str__(self):
        if self._isValue():
            return str(self._getValue())
        else:
            return f"[{self._getLeftChild()}, {self._getRightChild()}]"

def solve_part_1():
    numbers = list(map(Num, map(json.loads , read_input_file_data().splitlines())))
    result = numbers.pop(0)
    for num in numbers:
        result = result.add(num)
    return result.getMagnitude()
        
def solve_part_2():
    number_lists = list(map(json.loads , read_input_file_data().splitlines()))
    length = len(number_lists)

    max_magnitude = -inf
    for i in range(length):
        for j in range(length):
            if i == j: # Same number
                continue
            magnitude = Num(number_lists[i]).add(Num(number_lists[j])).getMagnitude()
            max_magnitude = max(max_magnitude, magnitude)
    return max_magnitude
    
print(solve_part_2())
