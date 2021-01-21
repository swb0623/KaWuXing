from base.base_poco import *
import pytest
import allure
@allure.feature("违法举报模块")
class TestJuBao:
    def setup(self):
        log()
        self.poco = init_poco()
    def teardown(self):
        quit()
    @allure.story("未实名举报")
    @allure.description("未实名时，验证举报界面数据正确")
    @allure.title("未实名")
    def test_not_jubao(self):
        with allure.step("点击违法举报"):
            self.poco("btn_jubao").wait_for_appearance()
            self.poco("btn_jubao").click()
            screenshot("未实名截图")
        assert "尚未实名认证" in self.poco("txt_content@Text").get_text()