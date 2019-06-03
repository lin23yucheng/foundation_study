# allure 装饰器
import allure
# pytest 单元测试框架
# @allure.feature("测试功能一") 加在类上面
@allure.feature('商品模块')
class Test_order:
    # @allure.story("测试小功能1")加在方法上面
    @allure.story('新建商品')
    def test_order_add(self):
        # 假设发了请求
        # 假设获取响应
        assert '成功' in '操作成功'

    @allure.story('查询商品')
    def test_order_to_wh(self):
        # 假设发了请求
        # 假设获取响应
        assert '成功' in '操作成功'