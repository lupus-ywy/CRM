# CRM 系统 API 接口文档

本文档描述CRM系统的RESTful API接口设计，涵盖线索、客户、联系人、供应商、产品、销售机会和互动记录的管理。

## 基础信息

- **基础URL**: `/api/v1/`
- **数据格式**: JSON
- **认证方式**: Token / Session

## 通用响应格式

### 成功响应
```json
{
    "code": 200,
    "message": "success",
    "data": {}
}
```

### 错误响应
```json
{
    "code": 400,
    "message": "error message",
    "data": null
}
```

---

## 1. 线索管理 (Lead)

### 1.1 创建线索
**请求**: `POST /api/v1/leads/`

**请求体**:
```json
{
    "name": "张三",
    "contact_info": "13800138000",
    "contact_type": "phone",
    "source": "website",
    "notes": "通过官网咨询产品价格"
}
```

**响应**:
```json
{
    "code": 201,
    "message": "创建成功",
    "data": {
        "id": 1,
        "name": "张三",
        "contact_info": "13800138000",
        "contact_type": "phone",
        "source": "website",
        "status": "pending",
        "notes": "通过官网咨询产品价格",
        "created_at": "2026-04-08T14:00:00Z"
    }
}
```

### 1.2 获取线索列表
**请求**: `GET /api/v1/leads/`

**查询参数**:
- `status`: 筛选状态
- `source`: 筛选来源
- `page`: 页码
- `page_size`: 每页数量

**响应**:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "count": 10,
        "next": "/api/v1/leads/?page=2",
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "张三",
                "contact_info": "13800138000",
                "contact_type": "phone",
                "source": "website",
                "status": "pending",
                "first_contact_date": null,
                "last_contact_date": null,
                "notes": "",
                "created_at": "2026-04-08T14:00:00Z",
                "updated_at": "2026-04-08T14:00:00Z"
            }
        ]
    }
}
```

### 1.3 获取线索详情
**请求**: `GET /api/v1/leads/{id}/`

**响应**:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "id": 1,
        "name": "张三",
        "contact_info": "13800138000",
        "contact_type": "phone",
        "source": "website",
        "status": "pending",
        "first_contact_date": null,
        "last_contact_date": null,
        "notes": "",
        "created_at": "2026-04-08T14:00:00Z",
        "updated_at": "2026-04-08T14:00:00Z"
    }
}
```

### 1.4 更新线索
**请求**: `PUT /api/v1/leads/{id}/`

**请求体**:
```json
{
    "status": "contacted",
    "first_contact_date": "2026-04-08"
}
```

### 1.5 删除线索
**请求**: `DELETE /api/v1/leads/{id}/`

### 1.6 线索转化为客户
**请求**: `POST /api/v1/leads/{id}/convert/`

**请求体**:
```json
{
    "company_name": "某某科技公司"
}
```

---

## 2. 客户管理 (Customer)

### 2.1 创建客户
**请求**: `POST /api/v1/customers/`

**请求体**:
```json
{
    "company_name": "某某科技公司",
    "industry": "信息技术",
    "phone": "010-12345678",
    "email": "info@example.com",
    "website": "https://www.example.com",
    "address": "北京市朝阳区xxx路xxx号",
    "customer_type": "enterprise",
    "credit_rating": "A",
    "owner": 1
}
```

### 2.2 获取客户列表
**请求**: `GET /api/v1/customers/`

**查询参数**:
- `customer_type`: 客户类型
- `owner`: 负责人ID
- `keyword`: 搜索关键词

### 2.3 获取客户详情
**请求**: `GET /api/v1/customers/{id}/`

### 2.4 更新客户
**请求**: `PUT /api/v1/customers/{id}/`

### 2.5 删除客户
**请求**: `DELETE /api/v1/customers/{id}/`

---

## 3. 联系人管理 (Contact)

### 3.1 创建联系人
**请求**: `POST /api/v1/contacts/`

**请求体**:
```json
{
    "customer": 1,
    "first_name": "小明",
    "last_name": "张",
    "position": "采购经理",
    "department": "采购部",
    "phone": "13800138000",
    "email": "zhang@example.com",
    "is_primary": true,
    "role_in_decision": "decision_maker"
}
```

### 3.2 获取客户联系人列表
**请求**: `GET /api/v1/customers/{customer_id}/contacts/`

### 3.3 获取联系人详情
**请求**: `GET /api/v1/contacts/{id}/`

### 3.4 更新联系人
**请求**: `PUT /api/v1/contacts/{id}/`

### 3.5 删除联系人
**请求**: `DELETE /api/v1/contacts/{id}/`

---

## 4. 供应商管理 (Supplier)

### 4.1 创建供应商
**请求**: `POST /api/v1/suppliers/`

**请求体**:
```json
{
    "company_name": "某某供应商公司",
    "contact_person": "李四",
    "phone": "13900139000",
    "email": "li@supplier.com",
    "address": "上海市xxx区xxx路",
    "credit_rating": "优秀",
    "is_preferred": true,
    "active_flag": true,
    "website_url": "https://www.supplier.com"
}
```

### 4.2 获取供应商列表
**请求**: `GET /api/v1/suppliers/`

**查询参数**:
- `is_preferred`: 是否首选
- `active_flag`: 是否合作中

### 4.3 获取供应商详情
**请求**: `GET /api/v1/suppliers/{id}/`

### 4.4 更新供应商
**请求**: `PUT /api/v1/suppliers/{id}/`

### 4.5 删除供应商
**请求**: `DELETE /api/v1/suppliers/{id}/`

---

## 5. 产品管理 (Product)

### 5.1 创建产品
**请求**: `POST /api/v1/products/`

**请求体**:
```json
{
    "name": "产品A",
    "description": "产品A的详细描述",
    "category": "电子产品",
    "unit_price": 99.99,
    "stock_quantity": 1000
}
```

### 5.2 获取产品列表
**请求**: `GET /api/v1/products/`

**查询参数**:
- `category`: 产品类别
- `in_stock`: 是否有库存

### 5.3 获取产品详情
**请求**: `GET /api/v1/products/{id}/`

### 5.4 更新产品
**请求**: `PUT /api/v1/products/{id}/`

### 5.5 更新产品库存
**请求**: `PATCH /api/v1/products/{id}/stock/`

**请求体**:
```json
{
    "stock_quantity": 500
}
```

### 5.6 删除产品
**请求**: `DELETE /api/v1/products/{id}/`

---

## 6. 销售机会管理 (Opportunity)

### 6.1 创建销售机会
**请求**: `POST /api/v1/opportunities/`

**请求体**:
```json
{
    "title": "某某项目",
    "customer": 1,
    "stage": "new_lead",
    "amount": 100000.00,
    "expected_close_date": "2026-06-30",
    "assigned_to": 1
}
```

### 6.2 获取销售机会列表
**请求**: `GET /api/v1/opportunities/`

**查询参数**:
- `stage`: 销售阶段
- `customer`: 客户ID
- `assigned_to`: 负责人ID

### 6.3 获取销售机会详情
**请求**: `GET /api/v1/opportunities/{id}/`

### 6.4 更新销售机会
**请求**: `PUT /api/v1/opportunities/{id}/`

### 6.5 删除销售机会
**请求**: `DELETE /api/v1/opportunities/{id}/`

---

## 7. 互动记录管理 (Interaction)

### 7.1 创建互动记录
**请求**: `POST /api/v1/interactions/`

**请求体**:
```json
{
    "type": "phone",
    "subject": "产品咨询跟进",
    "notes": "客户对产品A很感兴趣，询问了价格和交付时间",
    "interaction_time": "2026-04-08T15:00:00Z",
    "customer": 1,
    "contact": null,
    "lead": null,
    "user": 1
}
```

### 7.2 获取互动记录列表
**请求**: `GET /api/v1/interactions/`

**查询参数**:
- `customer`: 客户ID
- `lead`: 线索ID
- `type`: 互动类型
- `user`: 跟进人ID

### 7.3 获取互动记录详情
**请求**: `GET /api/v1/interactions/{id}/`

### 7.4 更新互动记录
**请求**: `PUT /api/v1/interactions/{id}/`

### 7.5 删除互动记录
**请求**: `DELETE /api/v1/interactions/{id}/`

---

## 8. 统计接口

### 8.1 获取销售统计
**请求**: `GET /api/v1/statistics/sales/`

**查询参数**:
- `start_date`: 开始日期
- `end_date`: 结束日期

**响应**:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "total_opportunities": 50,
        "won_opportunities": 10,
        "total_amount": 500000.00,
        "won_amount": 100000.00,
        "conversion_rate": 0.2
    }
}
```

### 8.2 获取客户统计
**请求**: `GET /api/v1/statistics/customers/`

**响应**:
```json
{
    "code": 200,
    "message": "success",
    "data": {
        "total_customers": 100,
        "new_customers_this_month": 10,
        "customers_by_type": {
            "enterprise": 80,
            "individual": 20
        }
    }
}
```

---

## 错误码说明

| 错误码 | 说明 |
|--------|------|
| 200 | 请求成功 |
| 201 | 创建成功 |
| 400 | 请求参数错误 |
| 401 | 未授权 |
| 403 | 禁止访问 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

## 数据字典

### 线索状态 (Lead Status)
| 值 | 说明 |
|----|------|
| pending | 待联系 |
| contacted | 已联系 |
| converted | 已转化 |
| invalid | 无效 |

### 销售阶段 (Opportunity Stage)
| 值 | 说明 |
|----|------|
| new_lead | 新线索 |
| requirement | 需求确认 |
| proposal | 方案报价 |
| negotiation | 谈判中 |
| closed_won | 已成交 |
| closed_lost | 已丢失 |

### 互动类型 (Interaction Type)
| 值 | 说明 |
|----|------|
| phone | 电话 |
| email | 邮件 |
| meeting | 会议 |
| visit | 拜访 |
| wechat | 微信 |
| sms | 短信 |
| other | 其他 |

### 决策角色 (Role in Decision)
| 值 | 说明 |
|----|------|
| decision_maker | 决策者 |
| influencer | 影响者 |
| user | 使用者 |
| evaluator | 评估者 |
| gatekeeper | 守门人 |
| other | 其他 |