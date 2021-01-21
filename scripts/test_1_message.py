from airtest.core.api import *
from base.base_poco import *
import pytest
import allure



@allure.feature("个人信息模块")
class TestMessage:

    def setup(self):
        log()
        self.poco = init_poco()

    @allure.story("个人信息")
    @allure.description("验证个人信息界面数据正确")
    @allure.title("验证个人信息存在")
    def test_mymessage(self):
        with allure.step("点击头像"):
            self.poco("img_head@Image").wait_for_appearance()
            self.poco("img_head@Image").click()
            screenshot("存在截图")
        assert  self.poco("img_title").exists() == True

    @pytest.mark.skip(reason="跳过")
    def test_lanzuan(self):
        self.poco("btn_diamond_blue").click()
        assert self.poco("ZSToggle@Toggle").child("bg").child("txt").get_text() == "钻石商店"

    @pytest.mark.skip(reason="跳过")
    def test_shop(self):
        self.poco("btn_shopSpine@SkeletonGraphic").click()
        items = []
        for i in "123456":
            items.append(self.poco("zsitem#" + i + "@").offspring("txt").get_text())
        assert items == ['60蓝钻', '180蓝钻', '300蓝钻', '680蓝钻', '1280蓝钻', '3280蓝钻']

    def teardown(self):
        quit()


