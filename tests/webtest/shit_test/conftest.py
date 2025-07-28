import pytest
import asyncio
@pytest.fixture(scope="module")
async def first_fixture():
    await asyncio.sleep(1)
    return "data"

@pytest.fixture(scope="module")
async def second_fixture(first_fixture):
    await asyncio.sleep(1)
    yield first_fixture
@pytest.fixture(scope="function")
async def third_fixture(second_fixture):
    await asyncio.sleep(1)
    yield second_fixture