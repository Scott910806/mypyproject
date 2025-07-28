import pytest
from playwright.async_api import Page, expect
from tests.webtest.async_test.models.home_async import PlanListPage

@pytest.mark.asyncio
async def test_plan_search(authed_page:Page):
    plan_list_page = PlanListPage(authed_page)
    await plan_list_page.navigate()
    result_page = await plan_list_page.search()

    assert await result_page.result_count() > 0

@pytest.mark.asyncio    
async def test_search_by_name(authed_page:Page):
    plan_list_page = PlanListPage(authed_page)
    await plan_list_page.navigate()
    result_page = await plan_list_page.search(name='webtest')

    assert await result_page.result_count() > 0
    await expect(await result_page.get_plan_name()).to_contain_text('webtest')

@pytest.mark.asyncio
async def test_search_by_code(authed_page:Page):
    plan_list_page = PlanListPage(authed_page)
    await plan_list_page.navigate()
    result_page = await plan_list_page.search(code='PF-liufang_test-2025-05-2186126324')

    assert await result_page.result_count() > 0
    await expect(await result_page.get_plan_code()).to_contain_text('PF-liufang_test-2025-05-2186126324')

@pytest.mark.asyncio
async def test_search_by_multiple_fields(authed_page:Page):
    plan_list_page = PlanListPage(authed_page)
    await plan_list_page.navigate()
    result_page = await plan_list_page.search(group="AI", status="上线", updated_by="马云翔")

    assert await result_page.result_count() > 0
    await expect(await result_page.get_plan_group()).to_contain_text("AI")
    await expect(await result_page.get_plan_status()).to_contain_text("上线")
    await expect(await result_page.get_updated_by()).to_contain_text("马云翔")