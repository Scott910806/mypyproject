import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from typing import Generator

@pytest.fixture(scope="module")
def login_context(browser: Browser):
    browser_context = browser.new_context()
    page = browser_context.new_page()
    # 登录o系统
    username = "mayunxiang008"
    password = "Webtest2025"
    page.goto("http://moka.dmz.sit.caijj.net/idaasui/#/account-login")
    page.get_by_role("textbox", name="请输入您 SIT环境的账号").fill(username)
    page.get_by_role("textbox", name="请输入您 SIT环境的密码").fill(password)
    page.get_by_role("button", name="登 录 SIT").click()
    page.wait_for_timeout(2000)
    # 存储（登录信息）
    storage = browser_context.storage_state()
    context = browser.new_context(storage_state=storage)
    yield context
    context.close()

@pytest.fixture(scope="function")
def authed_page(login_context:BrowserContext)->Generator[Page,None,None]:
    page = login_context.new_page()
    yield page
    page.close()