"""
pip install flask==3.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple/
"""
from flask import Flask, request, jsonify, make_response
import uuid

app = Flask(__name__)

# 模拟数据库，存储用户信息、商品信息和订单信息
users = {
    'u001': {'uid': 'u001', 'password': 'p001', 'username': 'user1', 'errorcode': 0, 'info': {'age': 12, 'sex': 'male'},
             'books': [{'a': 1, 'b': 2}, {'a': 11, 'b': 22}, 3, 4]},
    'u002': {'uid': 'u002', 'password': 'p002', 'username': 'user2', 'errorcode': 0,
             'info': {'age': 13, 'sex': 'female'}, 'books': [5, 6, 7, 8]}
}

products = {
    'product1': {'productid': 'product1', 'name': 'Product One', 'price': 10.99, 'errorcode': 0},
    'product2': {'productid': 'product2', 'name': 'Product Two', 'price': 20.99, 'errorcode': 0}
}
print(users)
orders = {
    'u001': [],
    'u002': []
}

order_counter = 1


# 注册接口，JSON入参，返回新用户信息
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    password = data.get('password')
    username = data.get('username')
    age = data.get('age')
    sex = data.get('sex')

    if not all([password, username, age, sex]):
        return jsonify({'message': 'Missing required fields', 'errorcode': -2}), 400

    # 检查用户名是否已经存在
    for user in users.values():
        if user['username'] == username:
            # 用户名已存在
            return jsonify({'message': 'Username already exists', 'errorcode': -1}), 400

    # 生成新的uid
    if users:
        max_id = max(int(user['uid'][1:]) for user in users.values())
        new_uid = 'u{:03d}'.format(max_id + 1)
    else:
        new_uid = 'u001'

    # 创建一个新的用户信息字典
    new_user = {
        'uid': new_uid,
        'password': password,
        'username': username,
        'errorcode': 0,
        'info': {'age': age, 'sex': sex},
        'books': []  # You can customize the initial user data as needed
    }

    users[new_uid] = new_user
    orders[new_uid] = []  # 初始化新用户的订单列表

    response = make_response(jsonify(new_user))
    response.set_cookie('uid', new_uid)  # Set Cookie for the new user
    print(f"注册成功后用户表数据:{users}")
    return response,201


# 登录接口，表单入参，返回Cookie信息
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not all([username, password]):
        return jsonify({'message': 'Missing username or password', 'errorcode': -2}), 400

    for user in users.values():
        if user['username'] == username and user['password'] == password:
            response = make_response(jsonify(user))
            response.set_cookie('uid', user['uid'])  # 设置Cookie
            return response
    return jsonify({'message': 'Invalid credentials', 'errorcode': -1}), 401


# 获取个人信息接口，从Cookie中获取uid
@app.route('/profile', methods=['GET'])
def profile():
    uid = request.cookies.get('uid')  # 从Cookie中获取uid

    if uid in users:
        return jsonify(users[uid])
    else:
        return jsonify({'message': 'User not found'}), 404


# 查询商品信息接口
@app.route('/get_product', methods=['GET'])
def get_product():
    productid = request.args.get('productid')

    if not productid:
        return jsonify({'message': 'Product ID is required', 'errorcode': -1}), 400

    if productid in products:
        return jsonify(products[productid])
    else:
        return jsonify({'message': 'Product not found', 'errorcode': -2}), 404


# 提交订单接口，JSON入参，使用Cookie中的uid
@app.route('/submit_order', methods=['POST'])
def submit_order():
    global order_counter  # 声明使用全局变量
    data = request.json
    uid = request.cookies.get('uid')  # 从Cookie中获取uid
    productid = data.get('productid')

    if not uid:
        return jsonify({'message': 'User not authenticated', 'errorcode': -3}), 401

    if uid not in users:
        return jsonify({'message': 'User not found', 'errorcode': -1}), 404

    if not productid:
        return jsonify({'message': 'Product ID is required', 'errorcode': -2}), 400

    if productid not in products:
        return jsonify({'message': 'Product not found', 'errorcode': -4}), 404

    order_id = 'd{:03d}'.format(order_counter)  # 生成订单 ID (e.g., d001)
    order_counter += 1  # 递增订单计数器

    order = {'order_id': order_id, 'productid': productid, 'uid': uid}
    orders[uid].append(order)
    return jsonify({'message': 'Order submitted successfully', 'order_id': order_id}), 201


# 查询订单接口，从Cookie中获取uid，并可选地通过订单编号查询特定订单
@app.route('/get_orders', methods=['GET'])
def get_orders():
    uid = request.cookies.get('uid')  # 从Cookie中获取uid
    order_id = request.args.get('order_id')  # 获取可选的订单编号

    if not uid:
        return jsonify({'message': 'User not authenticated', 'errorcode': -3}), 401

    if uid not in users:
        return jsonify({'message': 'User not found', 'errorcode': -1}), 404

    if order_id:
        # 如果订单编号存在，查询特定订单
        order = next((order for order in orders[uid] if order['order_id'] == order_id), None)
        if order:
            return jsonify(order)
        else:
            return jsonify({'message': 'Order not found'}), 404
    else:
        # 如果没有订单编号参数，返回所有订单
        return jsonify({'orders': orders[uid]})


# =====================================================================================================
@app.route('/update_user_info', methods=['POST'])
def update_user_info():
    """
    更新用户信息接口：
    - 依赖 Cookie 中的 uid 和请求体中的 username
    """
    # 从 Cookie 中获取用户唯一标识 uid
    uid = request.cookies.get('uid')
    # 获取请求体数据
    data = request.json

    # 如果没有获取到 uid，返回未认证错误
    if not uid:
        return jsonify({'message': 'User not authenticated', 'errorcode': -3}), 401

    # 从请求体中提取用户名和新信息
    username = data.get('username')
    new_info = data.get('info')

    # 检查必要字段是否存在
    if not username or not new_info:
        return jsonify({'message': 'Missing required fields', 'errorcode': -2}), 400

    # 检查 uid 是否在用户数据库中
    if uid not in users:
        return jsonify({'message': 'User not found', 'errorcode': -1}), 404

    # 验证请求中的 username 是否与数据库中的用户名匹配
    if users[uid]['username'] != username:
        return jsonify({'message': 'Permission denied', 'errorcode': -4}), 403

    # 更新用户信息
    users[uid]['info'].update(new_info)
    print(f"更新后数据:{users}")
    # 返回更新成功响应
    return jsonify({'message': 'User information updated successfully', 'errorcode': 0}), 200


# =====================================================================================================

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
