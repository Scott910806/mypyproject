import pytest, asyncio
from playwright.async_api import BrowserContext, async_playwright
# import nest_asyncio
# nest_asyncio.apply()

@pytest.fixture(scope="module")
async def login_context():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        # 登录o系统
        username = "mayunxiang008"
        password = "Webtest2025"
        await page.goto("http://moka.dmz.sit.caijj.net/idaasui/#/account-login")
        await page.get_by_role("textbox", name="请输入您 SIT环境的账号").fill(username)
        await page.get_by_role("textbox", name="请输入您 SIT环境的密码").fill(password)
        await page.get_by_role("button", name="登 录 SIT").click()
        await page.wait_for_timeout(2000)

        # 存储登录信息
        storage = await context.storage_state()
        new_context = await browser.new_context(storage_state=storage)
        yield new_context
        await context.close()
        await browser.close()

# @pytest.fixture(scope="module")
# async def login_context(browser: Browser):
#     print("event_loop:", asyncio.get_event_loop())
#     browser_context = await browser.new_context()
#     page = await browser_context.new_page()
#     # 登录o系统
#     username = "mayunxiang008"
#     password = "Webtest2025"
#     await page.goto("http://moka.dmz.sit.caijj.net/idaasui/#/account-login")
#     await page.get_by_role("textbox", name="请输入您 SIT环境的账号").fill(username)
#     await page.get_by_role("textbox", name="请输入您 SIT环境的密码").fill(password)
#     await page.get_by_role("button", name="登 录 SIT").click()
#     await page.wait_for_timeout(2000)
#     # 存储登录信息
#     storage = await browser_context.storage_state()
#     context = await browser.new_context(storage_state=storage)
#     yield context
#     await context.close()
#     await browser_context.close()

@pytest.fixture(scope="function")
async def authed_page(login_context:BrowserContext):
    print("event_loop:", asyncio.get_event_loop())
    page = await login_context.new_page()
    yield page
    await page.close()