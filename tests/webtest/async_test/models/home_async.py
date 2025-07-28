import re
from playwright.async_api import Page, Locator
from utils.generate_str import *

class PlanListPage:
    def __init__(self, page:Page):
        self.page = page

    async def navigate(self):
        await self.page.goto("http://moka.dmz.sit.caijj.net/bizui/#/activity-list/v2/liufang_test?_shMenuId=tenant_menu_P0224_plan_config_m88761z9")
    
    async def search(self, name:str=None, code:str=None, group:str=None, status:str=None, updated_by:str=None):
        """
        @param name: 计划名称
        @param code: 计划编号
        @param group: 计划组
        @param status: 计划状态
        @param updated_by: 更新人
        @return: 搜索结果
        """
        await self.page.get_by_role("button", name="重 置").click()
        if name:
            await self.page.get_by_role("textbox", name = "计划名称").fill(name)
        if code:
            plan_code_textbox = self.page.locator("div.ant-select-selection__rendered").first
            await plan_code_textbox.click()
            await plan_code_textbox.locator("input.ant-select-search__field").fill(code)
            await self.page.get_by_role("option", name=code).click()
        if group:
            group_code_textbox = self.page.locator("span.ant-select-selection__rendered").first
            await group_code_textbox.click()
            await self.page.get_by_role("textbox", name="filter select").fill(group)
            await self.page.get_by_title(group, exact=True).first.locator("span").click()
        if status:
            await self.page.locator("div.ant-select-selection__rendered").nth(1).click()
            await self.page.get_by_role("option", name=status).click()
        if updated_by:
            updated_by_textbox = self.page.locator("div.ant-select-selection__rendered").nth(2)
            await updated_by_textbox.click()
            await updated_by_textbox.locator("input.ant-select-search__field").fill(updated_by)
            await self.page.get_by_role("option", name=updated_by, exact=True).click()
            
        await self.page.get_by_role("button", name="查 询").click()
        await self.page.wait_for_selector("table", state="visible")
        result_table = self.page.locator("table").filter(has=self.page.locator("thead:has-text('计划名称')"))
        return ResultPage(result_table)

    async def creat_plan(self, name:str, group:str, status:str, description:str, **kwargs) -> dict:
        """
        @param name: 计划名称
        @param group: 业务场景
        @param status: 执行状态: 有状态、无状态
        @param description: 计划描述
        @param kwargs: 其他非必填参数, 如计划编号, 计划重要性, 负责人, 通知人
        @return: 返回新建计划信息
        """
        await self.page.get_by_role("button", name="新建经营计划").click()
        if "code" in kwargs:
            await self.page.locator("span").filter(has_text=re.compile(r"^PF-liufang_test-$")).get_by_role("textbox").fill(kwargs["code"])
            plan_code = f"PF-liufang_test-{kwargs['code']}"
        else:
            random_value = f"{get_current_day()}{get_random_number(8)}"
            plan_code = f"PF-liufang_test-{random_value}"
            await self.page.locator("span").filter(has_text=re.compile(r"^PF-liufang_test-$")).get_by_role("textbox").fill(random_value)
        
        await self.page.get_by_role("textbox", name="请输入经营计划名称").fill(name)
        await self.page.get_by_text("请选择",exact=True).first.click()
        await self.page.get_by_role("textbox", name="filter select").fill(group)
        await self.page.get_by_title(group).first.locator("span").click()
        await self.page.get_by_role("textbox", name="* 计划说明:").fill(description)
        await self.page.get_by_text("请选择计划是否有状态").click()
        await self.page.get_by_role("option", name=status).click()
        await self.page.get_by_role("button", name="确 定").click()
        await self.page.wait_for_timeout(3000)

        return {"biz_key":plan_code, "biz_name":name, "biz_group":group}

class ResultPage:
    """
    搜索结果table
    """
    def __init__(self, locator:Locator):
        self.result_table=locator
        self.result_list=locator.locator("tbody").get_by_role("row")
    
    async def result_count(self) -> int:
        return await self.result_list.count()
    
    async def get_plan_name(self, order:int=0) -> Locator:
        return self.result_list.nth(order).get_by_role("cell").nth(0)
    
    async def get_plan_code(self, order:int=0) -> Locator:
        return self.result_list.nth(order).get_by_role("cell").nth(1)
    
    async def get_plan_group(self, order:int=0) -> Locator:
        return self.result_list.nth(order).get_by_role("cell").nth(2)
    
    async def get_plan_status(self, order:int=0) -> Locator:
        return self.result_list.nth(order).get_by_role("cell").nth(4)

    async def get_updated_by(self, order:int=0) -> Locator:
        return self.result_list.nth(order).get_by_role("cell").nth(6)