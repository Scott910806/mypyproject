import pytest
from playwright.sync_api import expect, Page
from models.home import PlanListPage
from utils.generate_str import get_specified_prefix_str

@pytest.mark.skip
def test_create_plan(authed_page:Page):
    plan_list_page = PlanListPage(authed_page)
    plan_list_page.navigate()
    new_plan = plan_list_page.creat_plan(
        get_specified_prefix_str('webtest'),'AI','有状态','UIAUTO测试计划',
        code = get_specified_prefix_str('yxma')
    )
    print(new_plan)

def test_plan_search(authed_page:Page):
    plan_list_page = PlanListPage(authed_page)
    plan_list_page.navigate()
    result_page = plan_list_page.search()

    assert result_page.result_count() > 0

def test_search_by_name(authed_page:Page):
    plan_list_page = PlanListPage(authed_page)
    plan_list_page.navigate()
    result_page = plan_list_page.search(name='webtest')

    assert result_page.result_count() > 0
    expect(result_page.get_plan_name()).to_contain_text('webtest')

def test_search_by_code(authed_page:Page):
    plan_list_page = PlanListPage(authed_page)
    plan_list_page.navigate()
    result_page = plan_list_page.search(code='PF-liufang_test-2025-05-2186126324')

    assert result_page.result_count() > 0
    expect(result_page.get_plan_code()).to_contain_text('PF-liufang_test-2025-05-2186126324')

def test_search_by_multiple_fields(authed_page:Page):
    plan_list_page = PlanListPage(authed_page)
    plan_list_page.navigate()
    result_page = plan_list_page.search(group="AI", status="上线", updated_by="马云翔")

    assert result_page.result_count() > 0
    expect(result_page.get_plan_group()).to_contain_text("AI")
    expect(result_page.get_plan_status()).to_contain_text("上线")
    expect(result_page.get_updated_by()).to_contain_text("马云翔")