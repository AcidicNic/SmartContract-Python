import brownie
import pytest
from brownie.test import given, strategy


def test_transfer_adjusts_sender_balance(accounts, token):
    balance = token.balanceOf(accounts[0])
    token.transfer(accounts[1], 10**18, {'from': accounts[0]})

    assert token.balanceOf(accounts[0]) == balance - 10**18


@given(amount=strategy('uint256', max_value=10**18))
def test_transfer_adjusts_receiver_balance(accounts, token, amount):
    balance = token.balanceOf(accounts[1])
    token.transfer(accounts[1], amount, {'from': accounts[0]})

    assert token.balanceOf(accounts[1]) == balance + amount


def test_transfer_fails_from_insufficient_balance(accounts, token):
    with brownie.reverts("Insufficient balance"):
        token.transfer(accounts[2], 10**18, {'from': accounts[1]})
