pragma solidity ^0.6.0;

import "./SafeMath.sol";

contract My_Token {

    using SafeMath for uint256;

    uint256 public total = 0;

    event AddToTotalEvent(uint256 total);

    function addToTotal(uint256 _num) public {
        total.add(_num);
        emit AddToTotalEvent(total);
    }

}
