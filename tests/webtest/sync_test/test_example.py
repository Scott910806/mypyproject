import re
from playwright.sync_api import Page, expect
from utils.generate_str import *

def test_create_plan(authed_page:Page):
    page = authed_page
    # 进入经营计划平台
    url = "http://moka.dmz.sit.caijj.net/bizui/#/activity-list/v2/liufang_test?_shMenuId=tenant_menu_P0224_plan_config_m88761z9"
    page.goto(url)

    # 新建计划
    # 记录新生成的planName
    plan_name = get_specified_prefix_str("webtest")
    # 记录新生成的bizKey
    biz_key_random_value = f"{get_current_day()}{get_random_number(8)}"
    biz_key = f"PF-liufang_test-{biz_key_random_value}"
    page.get_by_role("button", name="新建经营计划").click()
    page.locator("span").filter(has_text=re.compile(r"^PF-liufang_test-$")).get_by_role("textbox").fill(biz_key_random_value)
    page.get_by_role("textbox", name="请输入经营计划名称").fill(plan_name)
    page.get_by_text("请选择").first.click()
    page.get_by_role("treeitem", name="图标: caret-down 业务场景").locator("svg").click()
    page.get_by_role("treeitem", name="图标: caret-down 技术").locator("svg").click()
    page.get_by_title("AI", exact=True).click()
    page.get_by_role("textbox", name="* 计划说明:").fill("test")
    page.get_by_text("请选择计划是否有状态").click()
    page.get_by_role("option", name="有状态").click()
    page.get_by_role("button", name="确 定").click()
    page.get_by_role("button", name="查 询").click()
    page.wait_for_timeout(2000)

    # 检查新建计划数据
    expect(page.locator(".ant-table-fixed tr:first-child > td:first-child > a:first-of-type")).to_have_text(plan_name)
    expect(page.locator(".ant-table-fixed tr:first-child > td:nth-child(2) > span")).to_contain_text(biz_key)
    expect(page.locator(".ant-table-fixed tr:first-child > td:nth-child(3) > div > div > span")).to_contain_text("AI")
    expect(page.locator(".ant-table-fixed tr:first-child > td:nth-child(5) > span > .ant-badge-status-text")).to_contain_text("下线")
    expect(page.locator(".ant-table-fixed tr:first-child > td:nth-child(7) > span")).to_contain_text("马云翔008")
def test_modify_plan_base(authed_page:Page):
    page = authed_page
    # 进入经营计划平台
    url = "http://moka.dmz.sit.caijj.net/bizui/#/activity-list/v2/liufang_test?_shMenuId=tenant_menu_P0224_plan_config_m88761z9"
    page.goto(url)
    
    page.get_by_role("textbox", name="计划名称").fill("webtest_Dro4vWZD")
    page.get_by_role("button", name = "查 询").click()
    page.get_by_role("cell", name="webtest_Dro4vWZD").locator("a").click()
    page.get_by_role("tab", name="基础信息").click()
    page.get_by_role("button", name="编 辑").click()
    plan_desc = get_specified_prefix_str("plan_desc")
    page.get_by_role("textbox", name="* 计划说明:").fill(plan_desc)
    page.get_by_role("button", name="确 定").click()
    page.get_by_role("button", name="返回").click()
    page.wait_for_timeout(2000)

    updated_plan = page.get_by_role("row").filter(has=page.get_by_role("cell", name="webtest_Dro4vWZD"))
    expect(updated_plan.get_by_role("cell").nth(5)).to_contain_text(get_current_day())

def test_query_plan_bpm_records(authed_page: Page):
    page = authed_page
    # 进入经营计划平台
    url = "http://moka.dmz.sit.caijj.net/bizui/#/activity-list/v2/liufang_test?_shMenuId=tenant_menu_P0224_plan_config_m88761z9"
    page.goto(url)
    
    page.get_by_role("textbox", name="计划名称").fill("webtest_Dro4vWZD")
    page.get_by_role("button", name = "查 询").click()
    page.get_by_role("cell", name="webtest_Dro4vWZD").locator("a").click()
    page.get_by_role("tab", name="工单记录").click()

    expect(page.locator("tbody tr")).not_to_have_count(0)

def test_create_version_from_previous_version(authed_page: Page):
    page = authed_page
    # 进入经营计划平台
    url = "http://moka.dmz.sit.caijj.net/bizui/#/activity-list/v2/liufang_test?_shMenuId=tenant_menu_P0224_plan_config_m88761z9"
    page.goto(url)

    page.get_by_role("textbox", name="计划名称").fill("webtest_Dro4vWZD")
    page.get_by_role("button", name = "查 询").click()
    page.get_by_role("cell", name="webtest_Dro4vWZD").locator("a").click()
    page.get_by_role("button", name="新建版本").hover()
    page.get_by_text("从历史版本复制").click()
    page.get_by_role("textbox", name="版本描述:").click()
    page.get_by_role("textbox", name="版本描述:").fill("copy from history version")
    page.get_by_role("button", name="下一步").click()
    page.get_by_role("button", name="···").click()
    page.get_by_role("button", name="保存并退出").click()

    page.wait_for_selector("table", state="visible")
    version_table = page.locator("table").filter(has=page.locator("thead:has-text('版本号')"))
    new_version_row = version_table.locator("tbody tr").first
    print(new_version_row.text_content())
    expect(new_version_row.get_by_role("cell").nth(2)).to_contain_text("初始化")
    expect(new_version_row.get_by_role("cell").nth(4)).to_contain_text("copy from history version")

def test_create_version_from_other_plan(authed_page: Page):
    page = authed_page
    # 进入经营计划平台
    url = "http://moka.dmz.sit.caijj.net/bizui/#/activity-list/v2/liufang_test?_shMenuId=tenant_menu_P0224_plan_config_m88761z9"
    page.goto(url)

    page.get_by_role("textbox", name="计划名称").fill("webtest_Dro4vWZD")
    page.get_by_role("button", name = "查 询").click()
    page.get_by_role("cell", name="webtest_Dro4vWZD").locator("a").click()
    page.get_by_role("button", name="新建版本").hover()
    page.get_by_text("从其他计划复制").click()
    plan_selector = page.locator("div.ant-modal-content").locator("div.ant-select-selection__rendered").first
    plan_selector.click()
    plan_selector.locator("input").fill("血缘查询")
    origin_plan = page.get_by_text("PF-liufang_test-2025-06-051749090994588")
    origin_plan.wait_for(state="visible")
    origin_plan.click()
    page.get_by_role("textbox", name="版本描述:").click()
    page.get_by_role("textbox", name="版本描述:").fill("copy from other plan version")
    page.get_by_role("button", name="下一步").click()
    page.get_by_role("button", name="···").click()
    page.get_by_role("button", name="保存并退出").click()

    page.wait_for_selector("table", state="visible")
    version_table = page.locator("table").filter(has=page.locator("thead:has-text('版本号')"))
    new_version_row = version_table.locator("tbody tr").first
    print(new_version_row.text_content())
    expect(new_version_row.get_by_role("cell").nth(2)).to_contain_text("初始化")
    expect(new_version_row.get_by_role("cell").nth(4)).to_contain_text("copy from other plan version")

