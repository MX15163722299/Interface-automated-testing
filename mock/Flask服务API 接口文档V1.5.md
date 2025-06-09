## Flask服务API 接口文档V1.5

### 基本信息

- **Base URL**: `http://localhost:5000`
- **Content-Type**: `application/json`（除登录接口外）

### 用户注册接口

- **URL**: `/register`
- **方法**: `POST`
- **描述**: 注册新用户。

#### 请求头

| 参数名         | 值                 |
| -------------- | ------------------ |
| `Content-Type` | `application/json` |

#### 请求参数

| 参数名     | 类型     | 必填 | 描述                             |
| ---------- | -------- | ---- | -------------------------------- |
| `username` | `string` | 是   | 用户名                           |
| `password` | `string` | 是   | 密码                             |
| `age`      | `int`    | 是   | 年龄                             |
| `sex`      | `string` | 是   | 性别（例如：`male` 或 `female`） |

#### 响应示例

- **成功响应** (`200 Created`)

```json
{
    "uid": "u003",
    "password": "your_password",
    "username": "your_username",
    "errorcode": 0,
    "info": {
        "age": 25,
        "sex": "female"
    },
    "books": []
}
```

- **错误响应** (`400 Bad Request`)

```json
{
    "message": "Username already exists",
    "errorcode": -1
}
```

### 用户登录接口

- **URL**: `/login`
- **方法**: `POST`
- **描述**: 用户登录，并返回用户信息和设置 `uid` Cookie。

#### 请求头

| 参数名         | 值                                  |
| -------------- | ----------------------------------- |
| `Content-Type` | `application/x-www-form-urlencoded` |

#### 请求参数

| 参数名     | 类型     | 必填 | 描述   |
| ---------- | -------- | ---- | ------ |
| `username` | `string` | 是   | 用户名 |
| `password` | `string` | 是   | 密码   |

#### 响应示例

- **成功响应** (`200 OK`)

```json
{
    "uid": "u001",
    "password": "your_password",
    "username": "your_username",
    "errorcode": 0,
    "info": {
        "age": 25,
        "sex": "female"
    },
    "books": []
}
```

- **错误响应** (`401 Unauthorized`)

```json
{
    "message": "Invalid credentials",
    "errorcode": -1
}
```

### 获取个人信息接口

- **URL**: `/profile`
- **方法**: `GET`
- **描述**: 获取当前登录用户的个人信息。

#### 请求头

| 参数名         | 值                   |
| -------------- | -------------------- |
| `Content-Type` | `application/json`   |
| `Cookie`       | `uid=your_uid_value` |

#### 响应示例

- **成功响应** (`200 OK`)

```json
{
    "uid": "u001",
    "password": "your_password",
    "username": "your_username",
    "errorcode": 0,
    "info": {
        "age": 25,
        "sex": "female"
    },
    "books": []
}
```

- **错误响应** (`404 Not Found`)

```json
{
    "message": "User not found"
}
```

### 查询商品信息接口

- **URL**: `/get_product`
- **方法**: `GET`
- **描述**: 根据 `productid` 查询商品信息。

#### 请求头

| 参数名         | 值                 |
| -------------- | ------------------ |
| `Content-Type` | `application/json` |

#### 请求参数

| 参数名      | 类型     | 必填 | 描述   |
| ----------- | -------- | ---- | ------ |
| `productid` | `string` | 是   | 商品ID |

#### 响应示例

- **成功响应** (`200 OK`)

```json
{
    "productid": "product1",
    "name": "Product One",
    "price": 10.99
}
```

- **错误响应** (`404 Not Found`)

```json
{
    "message": "Product not found"
}
```

### 提交订单接口

- **URL**: `/submit_order`
- **方法**: `POST`
- **描述**: 用户提交订单。

#### 请求头

| 参数名         | 值                   |
| -------------- | -------------------- |
| `Content-Type` | `application/json`   |
| `Cookie`       | `uid=your_uid_value` |

#### 请求参数

| 参数名      | 类型     | 必填 | 描述   |
| ----------- | -------- | ---- | ------ |
| `productid` | `string` | 是   | 商品ID |

#### 响应示例

- **成功响应** (`201 Created`)

```json
{
    "message": "Order submitted successfully",
    "order_id": "d001"
}
```

- **错误响应** (`404 Not Found`)

```json
{
    "message": "User or product not found",
    "errorcode": -4
}
```

### 查询订单接口

- **URL**: `/get_orders`
- **方法**: `GET`
- **描述**: 查询当前用户的所有订单或指定订单。

#### 请求头

| 参数名         | 值                   |
| -------------- | -------------------- |
| `Content-Type` | `application/json`   |
| `Cookie`       | `uid=your_uid_value` |

#### 请求参数

| 参数名     | 类型     | 必填 | 描述           |
| ---------- | -------- | ---- | -------------- |
| `order_id` | `string` | 否   | （可选）订单ID |

#### 响应示例

- **成功响应** (`200 OK`)

查询所有订单：

```json
{
    "orders": [
        {
            "order_id": "d001",
            "productid": "product1",
            "uid": "u001"
        },
        {
            "order_id": "d002",
            "productid": "product2",
            "uid": "u001"
        }
    ]
}
```

查询特定订单：

```json
{
    "order_id": "d001",
    "productid": "product1",
    "uid": "u001"
}
```

- **错误响应** (`404 Not Found`)

```json
{
    "message": "Order not found"
}
```
### 更新用户信息接口

- **URL**: `/update_user_info`
- **方法**: `POST`
- **描述**: 
  - 此接口用于更新当前登录用户的个人信息。
  - 依赖前置接口 `/login` 返回的 `uid`。

---


#### 请求头

| 参数名         | 必填 | 描述                       |
| -------------- | ---- | -------------------------- |
| `Content-Type` | 是   | 固定值：`application/json` |
| `Cookie`       | 是   | 包含登录用户的 `uid`       |

#### 请求参数

| 参数名     | 类型     | 必填 | 描述                     |
| ---------- | -------- | ---- | ------------------------ |
| `username` | `string` | 是   | 当前登录用户的用户名     |
| `info`     | `object` | 是   | 需要更新的用户信息（键值对形式） |

#### 响应示例

- **成功响应** (`201 Created`):

```json
{
    "message": "User information updated successfully",
    "errorcode": 0
}
```

- **错误响应**

  - 用户未登录或身份验证失败 (`401 Unauthorized`)

    ~~~json
    {
        "message": "User not authenticated",
        "errorcode": -3
    }
    ~~~

  - 用户不存在 (`404 Not Found`)

    ~~~json
    {
        "message": "User not found",
        "errorcode": -1
    }
    ~~~

  - 请求字段缺失 (`400 Bad Request`)

    ~~~json
    {
        "message": "Missing required fields",
        "errorcode": -2
    }
    ~~~

  - 权限不足 (`403 Forbidden`)

    ~~~json
    {
        "message": "Permission denied",
        "errorcode": -4
    }
    ~~~

    

在以上文档中，所有需要 `Cookie` 的接口都加入了 `Cookie` 头的描述。