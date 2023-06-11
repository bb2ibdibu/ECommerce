from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),

]
# 这是一个 Django 项目中的 urls.py 文件，其中定义了四个 URL 路由规则，分别对应着购物车页面、添加商品到购物车、从购物车中删除商品和删除购物车中的某一项。
# Desc:
# 该代码片段是 Django 框架中用于处理 URL 映射关系的 urlpatterns 列表。其中每个 path() 函数表示一个路由规则，包括路径（第一个参数）、视图函数（第二个参数）和名称（name 参数）。具体来说：
# 	•	第一个路由规则 ‘’ 表示访问网站根目录时会调用 views.cart 视图函数展示用户的购物车页面。
# 	•	第二个路由规则 ‘add_cart/int:product_id/’ 表示当用户在浏览商品详情页时点击“加入购物车”按钮后会将该商品添加到其购物车，并跳转回原来的页面。其中 int:product_id 是动态路径参数，表示要添加到购物车里面的商品 ID。
# 	•	第三个路由规则 ‘remove_cart/int:product_id/int:cart_item_id/’ 表示当用户在查看自己已经加入到购物车里面的所有商品列表时可以选择删除某件特定的商品。其中 int:product_id 和 int:cart_item_id 都是动态路径参数，分别代表要删除哪种产品以及它在当前用户所属订单内部唯一标识符。
# 	•	最后一个路由规则 ‘remove_cart_item/int:product_id/int:cart_item_id/’ 表示当用户在购物车页面中删除某一项商品时，会调用 views.remove_cart_item 视图函数来处理。其中 int:product_id 和 int:cart_item_id 都是动态路径参数，分别代表要删除哪种产品以及它在当前用户所属订单内部唯一标识符。
