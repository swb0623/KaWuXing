from base.base_poco import *
import pytest
import allure
@allure.feature("优惠码模块")
class TestYouHuiMa:
    def setup(self):
        log()
        self.poco = init_poco()

    def teardown(self):
        quit()

    @allure.story("优惠码不存在")
    @allure.description("验证未填写优惠码时界面数据正确")
    @allure.title("验证优惠码未填写")
    @pytest.mark.skip()
    def test_not_youhuima(self):
        with allure.step("点击优惠码"):
            self.poco("btn_agent").wait_for_appearance()
            self.poco("btn_agent").click()
            screenshot("存在截图")
        assert self.poco("btn_bangding@").exists() == True

    @allure.story("优惠码错误")
    @allure.description("输入优惠码：123456,45678，优惠码写错误优惠码时界面数据正确")
    @allure.title("填写错误优惠码")
    @pytest.mark.parametrize("args",analyze_file("../data/2_youhuima_data.yaml","test_youhuima"))
    def test_youhuima(self,args):
        with allure.step("点击优惠码"):
            self.poco("btn_agent").wait_for_appearance()
            self.poco("btn_agent").click()
        with allure.step("点击输入框"):
            self.poco(text="请输入优惠码").click()
        with allure.step("输入优惠码"):
            text(args["yhm"])
            self.poco(text="请输入优惠码").click()
        with allure.step("点击立即绑定"):
            self.poco("btn_bangding@").click()
            screenshot("优惠码错误截图")
        assert self.poco("txt_err@Text").exists() == True