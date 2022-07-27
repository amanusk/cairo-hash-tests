from starkware.starknet.testing.starknet import Starknet
from starkware.starknet.compiler.compile import compile_starknet_files
import pytest
import pytest_asyncio
import os
import asyncio


@pytest_asyncio.fixture(scope="module")
def event_loop():
    return asyncio.new_event_loop()


@pytest_asyncio.fixture(scope="module")
async def starknet_factory():
    starknet = await Starknet.empty()
    return starknet


# The path to the contract source code.
HASH_CONTRACT_FILE = os.path.join("contracts", "keccak_hash.cairo")
HASH_TO_FP_CONTRACT_FILE = os.path.join("contracts", "expand_msg_SHA_XMD.cairo")


@pytest_asyncio.fixture(scope="module")
async def hash_factory(starknet_factory):
    # Create a new Starknet class that simulates the StarkNet
    # system.
    starknet =  starknet_factory

    # Deploy the contract.

    # contract_def = compile_starknet_files(
    #     files=[HASH_CONTRACT_FILE], disable_hint_validation=True
    # )

    contract = await starknet.deploy(
        source=HASH_CONTRACT_FILE, disable_hint_validation=True
    )

    return contract


@pytest_asyncio.fixture(scope="module")
async def hash_to_fp_factory(starknet_factory):
    # Create a new Starknet class that simulates the StarkNet
    # system.
    starknet = starknet_factory

    # Deploy the contract.

    # contract_def = compile_starknet_files(
    #     files=[HASH_TO_FP_CONTRACT_FILE], disable_hint_validation=True
    # )
    
    contract = await starknet.deploy(
        source=HASH_TO_FP_CONTRACT_FILE, disable_hint_validation=True
    )

    return contract
    
