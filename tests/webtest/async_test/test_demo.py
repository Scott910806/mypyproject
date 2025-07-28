from playwright.async_api import Page, expect
import pytest, asyncio
@pytest.mark.asyncio
async def test_async_demo(authed_page:Page):
    print("event_loop:", asyncio.get_event_loop())
    await authed_page.goto("http://moka.dmz.sit.caijj.net/bizui/#/activity-list/v2/liufang_test?planTabKey=plan")
    await expect(authed_page).to_have_title("计划配置")
    await authed_page.close()