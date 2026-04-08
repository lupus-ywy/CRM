#!/usr/bin/env python
"""
CRM API 测试脚本
根据 api_docs.md 编写的完整API测试
"""

import requests
import json
import sys

BASE_URL = "http://127.0.0.1:8000/api/v1"
HEADERS = {"Content-Type": "application/json"}


def print_response(title, response):
    """打印响应信息"""
    print(f"\n{'=' * 50}")
    print(f"{title}")
    print(f"状态码: {response.status_code}")
    print(f"响应: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
    print(f"{'=' * 50}")


def test_lead_api():
    """测试线索API"""
    print("\n### 测试线索API ###")

    # 1. 创建线索
    data = {
        "name": "张三",
        "contact_info": "13800138000",
        "contact_type": "phone",
        "source": "website",
        "notes": "通过官网咨询产品价格"
    }
    response = requests.post(f"{BASE_URL}/leads/", json=data, headers=HEADERS)
    print_response("创建线索", response)
    lead_id = response.json()["data"]["id"]

    # 2. 获取线索列表
    response = requests.get(f"{BASE_URL}/leads/", headers=HEADERS)
    print_response("获取线索列表", response)

    # 3. 获取线索详情
    response = requests.get(f"{BASE_URL}/leads/{lead_id}/", headers=HEADERS)
    print_response("获取线索详情", response)

    # 4. 更新线索
    data = {"status": "contacted", "first_contact_date": "2026-04-08"}
    response = requests.put(f"{BASE_URL}/leads/{lead_id}/", json=data, headers=HEADERS)
    print_response("更新线索", response)

    return lead_id


def test_customer_api():
    """测试客户API"""
    print("\n### 测试客户API ###")

    # 1. 创建客户
    data = {
        "company_name": "某某科技公司",
        "industry": "信息技术",
        "phone": "010-12345678",
        "email": "info@example.com",
        "website": "https://www.example.com",
        "address": "北京市朝阳区xxx路xxx号",
        "customer_type": "enterprise",
        "credit_rating": "A"
    }
    response = requests.post(f"{BASE_URL}/customers/", json=data, headers=HEADERS)
    print_response("创建客户", response)
    customer_id = response.json()["data"]["id"]

    # 2. 获取客户列表
    response = requests.get(f"{BASE_URL}/customers/", headers=HEADERS)
    print_response("获取客户列表", response)

    # 3. 获取客户详情
    response = requests.get(f"{BASE_URL}/customers/{customer_id}/", headers=HEADERS)
    print_response("获取客户详情", response)

    # 4. 更新客户
    data = {"credit_rating": "AAA"}
    response = requests.put(f"{BASE_URL}/customers/{customer_id}/", json=data, headers=HEADERS)
    print_response("更新客户", response)

    return customer_id


def test_contact_api(customer_id):
    """测试联系人API"""
    print("\n### 测试联系人API ###")

    # 1. 创建联系人
    data = {
        "customer": customer_id,
        "first_name": "小明",
        "last_name": "张",
        "position": "采购经理",
        "department": "采购部",
        "phone": "13800138000",
        "email": "zhang@example.com",
        "is_primary": True,
        "role_in_decision": "decision_maker"
    }
    response = requests.post(f"{BASE_URL}/contacts/", json=data, headers=HEADERS)
    print_response("创建联系人", response)
    contact_id = response.json()["data"]["id"]

    # 2. 获取联系人详情
    response = requests.get(f"{BASE_URL}/contacts/{contact_id}/", headers=HEADERS)
    print_response("获取联系人详情", response)

    return contact_id


def test_supplier_api():
    """测试供应商API"""
    print("\n### 测试供应商API ###")

    # 1. 创建供应商
    data = {
        "company_name": "某某供应商公司",
        "contact_person": "李四",
        "phone": "13900139000",
        "email": "li@supplier.com",
        "address": "上海市xxx区xxx路",
        "credit_rating": "优秀",
        "is_preferred": True,
        "active_flag": True,
        "website_url": "https://www.supplier.com"
    }
    response = requests.post(f"{BASE_URL}/suppliers/", json=data, headers=HEADERS)
    print_response("创建供应商", response)
    supplier_id = response.json()["data"]["id"]

    # 2. 获取供应商列表
    response = requests.get(f"{BASE_URL}/suppliers/", headers=HEADERS)
    print_response("获取供应商列表", response)

    return supplier_id


def test_product_api():
    """测试产品API"""
    print("\n### 测试产品API ###")

    # 1. 创建产品
    data = {
        "name": "产品A",
        "description": "产品A的详细描述",
        "category": "电子产品",
        "unit_price": 99.99,
        "stock_quantity": 1000
    }
    response = requests.post(f"{BASE_URL}/products/", json=data, headers=HEADERS)
    print_response("创建产品", response)
    product_id = response.json()["data"]["id"]

    # 2. 获取产品列表
    response = requests.get(f"{BASE_URL}/products/", headers=HEADERS)
    print_response("获取产品列表", response)

    # 3. 更新产品库存
    data = {"stock_quantity": 500}
    response = requests.patch(f"{BASE_URL}/products/{product_id}/stock/", json=data, headers=HEADERS)
    print_response("更新产品库存", response)

    return product_id


def test_opportunity_api(customer_id):
    """测试销售机会API"""
    print("\n### 测试销售机会API ###")

    # 1. 创建销售机会
    data = {
        "title": "某某项目",
        "customer": customer_id,
        "stage": "new_lead",
        "amount": 100000.00,
        "expected_close_date": "2026-06-30"
    }
    response = requests.post(f"{BASE_URL}/opportunities/", json=data, headers=HEADERS)
    print_response("创建销售机会", response)
    opportunity_id = response.json()["data"]["id"]

    # 2. 获取销售机会列表
    response = requests.get(f"{BASE_URL}/opportunities/", headers=HEADERS)
    print_response("获取销售机会列表", response)

    # 3. 更新销售机会
    data = {"stage": "requirement"}
    response = requests.put(f"{BASE_URL}/opportunities/{opportunity_id}/", json=data, headers=HEADERS)
    print_response("更新销售机会", response)

    return opportunity_id


def test_interaction_api(customer_id, contact_id, lead_id):
    """测试互动记录API"""
    print("\n### 测试互动记录API ###")

    # 1. 创建互动记录（关联客户）
    data = {
        "type": "phone",
        "subject": "产品咨询跟进",
        "notes": "客户对产品A很感兴趣，询问了价格和交付时间",
        "interaction_time": "2026-04-08T15:00:00Z",
        "customer": customer_id
    }
    response = requests.post(f"{BASE_URL}/interactions/", json=data, headers=HEADERS)
    print_response("创建互动记录（客户）", response)
    interaction_id = response.json()["data"]["id"]

    # 2. 获取互动记录列表
    response = requests.get(f"{BASE_URL}/interactions/", headers=HEADERS)
    print_response("获取互动记录列表", response)

    return interaction_id


def main():
    """主测试函数"""
    print("=" * 60)
    print("CRM API 测试脚本")
    print("=" * 60)

    try:
        # 测试线索API
        lead_id = test_lead_api()

        # 测试客户API
        customer_id = test_customer_api()

        # 测试联系人API
        contact_id = test_contact_api(customer_id)

        # 测试供应商API
        supplier_id = test_supplier_api()

        # 测试产品API
        product_id = test_product_api()

        # 测试销售机会API
        opportunity_id = test_opportunity_api(customer_id)

        # 测试互动记录API
        interaction_id = test_interaction_api(customer_id, contact_id, lead_id)

        print("\n" + "=" * 60)
        print("✅ 所有测试完成！")
        print("=" * 60)

    except requests.exceptions.ConnectionError:
        print("\n❌ 错误：无法连接到服务器，请确保服务器正在运行！")
        print("启动命令: python manage.py runserver 0.0.0.0:8000")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 测试过程中出现错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()