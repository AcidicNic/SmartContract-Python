# @version ^0.2.4

event AddToTotalEvent:
    total: uint256

total: public(uint256)

@external
def addToTotal(_num: uint256):
    log AddToTotalEvent(self.total + _num)
