import pytest
import asyncio

@pytest.mark.asyncio
async def test_nested_fixture_01(first_fixture):
    assert first_fixture == "data"
    print(asyncio.get_event_loop())

@pytest.mark.asyncio
async def test_nested_fixture_02(second_fixture):
    assert second_fixture == "data"
    print(asyncio.get_event_loop())

@pytest.mark.asyncio
async def test_nested_fixture_03(third_fixture):
    assert third_fixture == "data"
    print(asyncio.get_event_loop())