"""描述餐馆的类"""
class Restaurant():
    """描述餐馆的类"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化餐厅属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + "类型是:" + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + "正在营业中，欢迎来就餐！")
