import allure


class Test001:
    @allure.step("我是测试步骤")
    def test01(self):
        """测试步骤"""
        allure.attach("附件内容","附件名字")

    @allure.severity(allure.severity_level.BLOCKER)
    def test02(self):
        """测试步骤"""
        allure.attach("附件内容","附件名字")

    @allure.severity(allure.severity_level.CRITICAL)
    def test03(self):
        """测试步骤"""
        allure.attach("附件内容","附件名字")

    @allure.severity(allure.severity_level.NORMAL)
    def test04(self):
        """测试步骤"""
        allure.attach("附件内容","附件名字")
