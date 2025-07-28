import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        username = "mayunxiang008" 
        password = "Webtest2025"
        await page.goto("http://moka.dmz.sit.caijj.net/idaasui/#/account-login")
        await page.get_by_role("textbox", name="请输入您 SIT环境的账号").fill(username)
        await page.get_by_role("textbox", name="请输入您 SIT环境的密码").fill(password)
        await page.get_by_role("button", name="登 录 SIT").click()
        await page.close()
        await browser.close()