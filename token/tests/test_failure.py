import brownie
import pytest


def test_failed_assertion(accounts, token):
    balance = token.balanceOf(accounts[0])
    assert balance == 31337


def test_transaction_reverts(accounts, token):
    token.transfer(accounts[2], 10**18, {'from': accounts[1]})


def test_time_travel(accounts, chain):
    tx = accounts[0].transfer(accounts[1], "1 ether")

    # sleep for 1000 seconds
    chain.sleep(1000)

    next_tx = accounts[0].transfer(accounts[1], "1 ether")

    assert next_tx.timestamp >= tx.timestamp + 1000


def test_mine_blocks(accounts, chain):
    tx = accounts[0].transfer(accounts[1], "1 ether")

    # mine 100 blocks
    chain.mine(100)

    assert chain[-1].number == tx.block_number + 100


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    pass


@pytest.mark.xfail
def test_function():
    pass
