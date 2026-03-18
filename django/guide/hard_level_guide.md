# Hard 级别：数据合规性问题代码生成指导（Django）

## 文档用途（IMPORTANT）

本文件 **不是给人类阅读的教程**，而是用于指导 AI 生成含数据合规问题的 Django 样本项目的执行规范。

生成时必须同时使用：

1. 对应 `vuln_plan_hard_xx.md`
2. 本 guide（复杂度、流程、输出格式）

冲突处理优先级：

- 漏洞场景、主漏洞、字段、接口：以 `vuln_plan` 为准
- 复杂度、工程结构、产出格式：以本 guide 为准

---

## AI 角色定义（Role）

你扮演以下复合角色：

- Django 后端工程师
- 数据合规风险引入者（intentionally）
- 数据合规审计分析器

你的目标 **不是** 写安全、规范、最佳实践代码，而是 **有控制地生成存在数据合规性问题的 Django 代码样本**，用于构建合规性分析数据集。

## 概述

**Hard 级别** 针对复杂的 Django 应用，包含 8-10 个难以发现的、深层的数据合规性问题。

问题跨越多个模块、涉及分布式数据流、高级权限模型、缓存策略、异步任务等。

---

## 0. 与 vuln_plan 的字段对齐规则（新增，必须执行）

每次开始生成前，先将 `vuln_plan_hard_xx.md` 解析为以下映射表：

| vuln_plan 字段 | 必做动作 | 输出落点 |
| --- | --- | --- |
| 难度级别 | 必须校验为 hard；不一致则停止生成 | `compliance_report.json -> difficulty_level` |
| 业务场景 | 作为模块划分、接口语义与测试数据来源 | `views.py` / `services.py` / 模板文件 |
| 主漏洞 | 必须 100% 出现且可定位到具体代码行 | `issues[]` 第一优先项 |
| 次要漏洞 | 按计划覆盖（通常 7-9 个） | `issues[]` |
| 涉及模型与字段 | 字段名必须逐一出现，不得改名 | `models.py` |
| API/页面 | 路由、视图、模板必须全部落地 | `urls.py` / `views.py` / `templates/` |
| 严重级别分布 | `issues` 统计需匹配计划 | `summary.by_severity` |
| 备注 | 作为强约束执行，不得忽略 | 全项目 |

### 字段一致性硬性要求

- `vuln_plan` 中列出的模型名、字段名、接口路径、模板名必须原样出现。
- 不允许私自替换主漏洞类别。
- 若 `vuln_plan` 未特别说明，Hard 级别默认必须包含 **Sensitive Data Exposure**。

---

## 1. 代码复杂度要求

- **文件数**: 3-5 个（models.py, views.py, serializers.py, services.py, tasks.py）
- **Model 数量**: 3-4 个，有复杂的关联关系（ManyToMany、通过关联等）
- **View/API 数量**: 3-4 个，涉及多步骤操作
- **数据库交互**: 复杂查询、事务、聚合、子查询等
- **认证**: 细粒度的权限控制或缺失的权限检查
- **业务逻辑**:
  - 异步任务（Celery）
  - 缓存策略（Redis）
  - 第三方 API 集成
  - 数据导入/导出
  - 多层级权限控制
- **跨系统交互**: 多个服务间的数据共享
- **项目结构**: 必须是完整 Django 项目（包含 manage.py、project/settings.py、project/urls.py、app/apps.py、app/models.py、app/views.py），**必须包含完整的 HTML 模板文件**。

### 示例场景

- 复杂电商平台（用户、商品、订单、支付、物流、评价）
- SaaS 多租户系统（租户隔离、权限控制、数据导出）
- 社交网络（用户、关系、内容、推荐、分析）
- 数据分析平台（用户、报表、导出、API）
- 金融系统（账户、交易、审计、合规）

---

## 2. 必须包含的合规性问题

<!-- markdownlint-disable MD022 MD031 -->

从以下问题类型中 **选择 8-10 个**：

### A. 多租户隔离失败（Multi-tenant Data Isolation）
**问题等级**: Critical

**描述**: 多个租户或组织的数据在存储、查询或缓存中混淆。

**代码示例**：
```python
class Organization(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Report(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    data = models.JSONField()

def get_reports(request):
    # ⚠️ 缺失租户隔离检查
    reports = Report.objects.filter(title__icontains=request.GET.get('keyword'))
    return JsonResponse(list(reports.values()), safe=False)
    # 可能返回其他组织的报表

# ⚠️ 缓存中缺失租户键
from django.core.cache import cache

def get_user_data(user_id):
    data = cache.get(f'user_{user_id}')  # 缺失 organization_id
    if not data:
        data = User.objects.get(id=user_id).__dict__
        cache.set(f'user_{user_id}', data)  # ⚠️ 可能被其他租户访问
    return data
```

### B. 敏感数据明文存储（Sensitive Data Exposure）- 必选
**问题等级**: Critical

**描述**: 支付信息、加密密钥、API Secret 未加密存储。

**代码示例**：
```python
class PaymentCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)  # ⚠️ 明文
    cvv = models.CharField(max_length=4)           # ⚠️ 明文
    expiry_date = models.CharField(max_length=5)   # ⚠️ 明文

class APIIntegration(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)     # ⚠️ 明文密钥
    api_secret = models.CharField(max_length=200)  # ⚠️ 明文密钥
    webhook_secret = models.CharField(max_length=200)  # ⚠️ 明文
```

### C. 异步任务中的敏感数据泄露（Async Task Data Leak）
**问题等级**: Critical

**描述**: Celery 任务、消息队列中传递敏感信息，或任务日志记录敏感数据。

**代码示例**：
```python
from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def process_payment(card_number, cvv, amount):
    """⚠️ 敏感信息通过消息队列传递"""
    logger.info(f"Processing payment: card={card_number}, cvv={cvv}, amount={amount}")  # ⚠️
    
    # 调用支付网关
    result = payment_gateway.charge(card_number, cvv, amount)
    return result

@shared_task
def export_user_data(user_id, export_format):
    """⚠️ 导出包含所有个人数据"""
    user = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user=user)
    
    data = {
        'name': user.name,
        'email': user.email,
        'phone': profile.phone,
        'id_card': profile.id_card,  # ⚠️ 敏感信息导出
        'home_address': profile.home_address,
        'financial_data': profile.financial_data,
    }
    
    # 敏感数据写入临时文件，未加密
    with open(f'/tmp/export_{user_id}.json', 'w') as f:
        json.dump(data, f)  # ⚠️ 未加密的敏感文件
    
    return f'/tmp/export_{user_id}.json'
```

### D. 缓存中的敏感数据（Sensitive Data in Cache）
**问题等级**: High

**描述**: 敏感数据被缓存，但缺失或不当设置过期时间。

**代码示例**：
```python
from django.core.cache import cache

def get_user_sensitive_data(user_id):
    # ⚠️ 敏感数据被缓存，可能被其他进程访问
    cached = cache.get(f'user_sensitive_{user_id}')
    if cached:
        return cached
    
    user = User.objects.get(id=user_id)
    data = {
        'id_card': user.profile.id_card,
        'ssn': user.profile.ssn,
        'bank_account': user.profile.bank_account,
    }
    
    cache.set(f'user_sensitive_{user_id}', data)  # ⚠️ 无过期时间
    return data
```

### E. 越权访问 - 细粒度权限缺失（Fine-grained Authorization）
**问题等级**: Critical

**描述**: 检查了全局权限但缺失细粒度的资源级别权限检查。

**代码示例**：
```python
def update_report(request, report_id):
    report = Report.objects.get(id=report_id)
    
    # ⚠️ 只检查是否登录，未检查用户是否属于该报表所有的组织
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    # 用户可以修改任意报表
    report.title = request.POST.get('title')
    report.data = request.POST.get('data')
    report.save()
    
    return JsonResponse({'success': True})

def delete_user_data(request, user_id):
    # ⚠️ 管理员可以删除任意用户的敏感数据，但无审计日志
    user = User.objects.get(id=user_id)
    user_data = UserPersonalData.objects.filter(user=user)
    user_data.delete()  # 直接删除，无记录
    
    return JsonResponse({'success': True})
```

### F. 数据导出的敏感信息暴露（Data Export）
**问题等级**: High

**描述**: 数据导出功能返回过多字段，或导出文件管理不当。

**代码示例**：
```python
def export_users_csv(request):
    """⚠️ 导出所有用户的敏感数据"""
    users = User.objects.all()
    
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Username', 'Email', 'Phone', 'ID Card', 'SSN', 'Address', 'Bank Account'])
    
    for user in users:
        profile = user.profile
        writer.writerow([
            user.id,
            user.username,
            user.email,
            profile.phone,        # ⚠️ 敏感信息
            profile.id_card,      # ⚠️ 敏感信息
            profile.ssn,          # ⚠️ 敏感信息
            profile.home_address, # ⚠️ 敏感信息
            profile.bank_account, # ⚠️ 敏感信息
        ])
    
    return response
```

### G. 数据库备份和日志中的敏感信息（Backups & Logs）
**问题等级**: High

**描述**: 数据库备份、查询日志、审计日志中包含敏感数据。

**代码示例**：
```python
# settings.py
LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django.log',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['file'],
            'level': 'DEBUG',  # ⚠️ 记录所有 SQL 查询
        },
    },
}

# 这会记录所有 SQL，包括 WHERE user_id = 123, password = "secret"
```

### H. GraphQL/API 的字段-级别攻击（Field-level Authorization）
**问题等级**: High

**描述**: 虽然检查了资源访问权限，但 API 仍然可能返回不应该公开的字段。

**代码示例**：
```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email',
            'password_hash',     # ⚠️ 内部字段不应暴露
            'last_login',        # ⚠️ 隐私信息
            'failed_login_count',# ⚠️ 内部状态
        ]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        # ✅ 资源级权限检查
        return User.objects.filter(organization=self.request.user.organization)
    
    # ⚠️ 但序列化器仍然暴露不应该公开的字段
```

### I. 缺失数据删除和匿名化机制（Data Retention & Anonymization）
**问题等级**: High

**描述**: 用户删除账户后，个人数据仍然被保留，无自动清理机制。

**代码示例**：
```python
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    deleted = models.BooleanField(default=False)  # ⚠️ 仅软删除
    deleted_at = models.DateTimeField(null=True)

# ⚠️ 没有硬删除或匿名化逻辑
# 所有用户活动、支付记录、个人信息仍然保留

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    # ⚠️ 即使用户删除，这些日志仍然存在，包含敏感信息
```

### J. SQL 注入 - 复杂查询（Complex SQL Injection）
**问题等级**: Critical

**描述**: 动态构建复杂查询，如 HAVING, ORDER BY, UNION 等。

**代码示例**：
```python
def advanced_search(request):
    sort_field = request.GET.get('sort_by', 'id')
    search_term = request.GET.get('search', '')
    
    # ⚠️ ORDER BY 注入
    query = f"""
        SELECT * FROM users 
        WHERE name LIKE '%{search_term}%'
        ORDER BY {sort_field}
    """
    users = User.objects.raw(query)
    return JsonResponse(list(users.values()), safe=False)

def analytics_query(request):
    metric = request.GET.get('metric', 'count')
    group_by = request.GET.get('group_by', 'date')
    
    # ⚠️ HAVING 注入
    query = f"""
        SELECT {group_by}, {metric}
        FROM orders
        GROUP BY {group_by}
        HAVING {request.GET.get('having', '1=1')}
    """
    result = Order.objects.raw(query)
    return JsonResponse(list(result.values()), safe=False)
```

### K. 第三方API中的敏感信息泄露（Third-party API）
**问题等级**: High

**描述**: 调用第三方 API 时传递过多个人信息，或 API 响应未过滤。

**代码示例**：
```python
import requests

def send_to_analytics(user_id):
    user = User.objects.get(id=user_id)
    profile = user.profile
    
    # ⚠️ 发送过多个人信息到第三方
    payload = {
        'user_id': user.id,
        'name': user.name,
        'email': user.email,
        'phone': profile.phone,        # ⚠️ 敏感信息
        'id_card': profile.id_card,    # ⚠️ 敏感信息
        'home_address': profile.home_address,  # ⚠️ 敏感信息
        'financial_data': profile.financial_status,  # ⚠️ 敏感信息
    }
    
    response = requests.post('https://analytics-service.com/track', json=payload)
    
    # ⚠️ API 响应可能包含敏感信息，直接返回给前端
    return JsonResponse(response.json())
```

<!-- markdownlint-enable MD022 MD031 -->

---

## 3. 问题分布要求

### 严重性分布

| 等级 | 最小数量 | 最大数量 |
| --- | ---: | ---: |
| Critical | 3 | 4 |
| High | 4 | 6 |
| Medium | 1 | 2 |
| Low | 0 | 1 |

**总计**: 8-10 个问题

### 类别分布

必须包含至少 7-8 个不同类别的问题，建议覆盖：

- 数据存储安全（Sensitive Data Exposure）
- 缓存安全（Sensitive Data in Cache）
- 分布式系统安全（Multi-tenant Isolation, Async Task Data Leak）
- 访问控制（Unauthorized Access, Fine-grained Authorization）
- 数据导出（Data Export）
- 生命周期管理（Data Retention & Anonymization）
- 复杂查询（Complex SQL Injection）
- 第三方集成（Third-party API）

---

## 4. 代码生成要求

### 标准生成流程（SOP）

1. 读取目标 `vuln_plan_hard_xx.md`
2. 提取并记录：场景、主/次漏洞、模型字段、接口与页面、严重级别分布
3. 初始化 Django 项目与 app
4. 按字段清单编写 `models.py`（确保主漏洞代码可定位）
5. 编写 `views.py`、`urls.py`，实现计划中的接口
6. 补充 `serializers.py`、`services.py`、`tasks.py`（按计划加入缓存/异步/导出逻辑）
7. 创建模板（至少含输入页与列表/详情页）
8. 执行迁移与运行校验
9. 生成 `compliance_report.json`
10. 对照清单做最终一致性检查

### 必须包含的元素

### 项目结构（必须）

- manage.py
- project/settings.py
- project/urls.py
- app/apps.py
- app/models.py
- app/views.py
- app/serializers.py
- app/services.py 或 app/utils.py
- app/tasks.py
- **app/templates/app/*.html (必须包含前端页面)**

1. **models.py**：
   - 至少 3-4 个 Model，有复杂关联
   - 包含多租户或权限相关模型
   - 包含敏感数据字段

2. **views.py/viewsets.py**：
   - 至少 3-4 个 API 端点
   - 部分缺少权限检查
   - 部分返回敏感数据

3. **serializers.py**：
   - 至少 1 个 Serializer 返回过多字段
   - 缺失字段级权限控制

4. **services.py 或 utils.py**：
   - 包含缓存逻辑（缺失过期时间或租户隔离）
   - 包含导出逻辑（返回敏感数据）

5. **tasks.py（Celery）**：
   - 至少 1 个异步任务处理敏感数据

6. **数据库操作**：
   - `.raw()` 或字符串拼接（SQL 注入）
   - 复杂查询
   - 缺失事务或隔离级别

### 允许使用终端（可选）

- 允许通过终端初始化 Django 项目
- 允许执行数据库迁移（makemigrations / migrate）
- 允许通过脚本或管理命令生成并写入数据

### 命令行初始化 Django（流程建议）

为保证样本生成流程可复现，建议优先使用命令行初始化项目，并统一采用以下顺序：

1. 创建并进入目标目录
2. 创建 Django 项目骨架（含 `manage.py`）
3. 创建业务 app（如 `core`）
4. 在 `settings.py` 中注册 app
5. 执行 `makemigrations` 与 `migrate`
6. 启动开发服务器进行结构校验

参考命令（示例）：

```bash
# 1) 创建项目目录
mkdir hard_example && cd hard_example

# 2) 初始化 Django 项目（注意最后的点）
django-admin startproject project .

# 3) 创建 app
python manage.py startapp core

# 4) 执行迁移
python manage.py makemigrations
python manage.py migrate

# 5) 运行服务验证
python manage.py runserver
```

说明：

- 项目命名可按目录规范调整（如 `example1`、`example2`）。
- 若使用虚拟环境，请先激活环境再执行上述命令。
- 生成完成后再按本指南要求补充 `models.py`、`views.py`、`serializers.py`、`services.py`、`tasks.py` 和模板文件。

### 代码框架示例

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class UserInOrganization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

class Report(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

# ⚠️ 各类敏感数据模型...

# views.py / viewsets.py
from rest_framework import viewsets
from django.http import JsonResponse
from django.views import View

class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    
    def get_queryset(self):
        # ⚠️ 缺失租户隔离检查
        return Report.objects.all()  # 可以访问任意租户的报表

# tasks.py (Celery)
from celery import shared_task

@shared_task
def export_org_data(org_id):
    # ⚠️ 导出所有敏感数据
    pass

# services.py / utils.py
from django.core.cache import cache

def get_cached_user_data(user_id):
    # ⚠️ 缺失租户键的缓存
    pass
```

---

## 5. 快速检查清单（新增）

生成完成后必须全部满足：

- [ ] 主漏洞已在代码中出现，且能定位文件与行号
- [ ] 次要漏洞数量与类别满足 `vuln_plan`
- [ ] 模型字段与 `vuln_plan` 一致（名称完全匹配）
- [ ] 路由与页面完整可访问
- [ ] 至少包含缓存/异步/导出三类逻辑中的两类
- [ ] 至少 1 处复杂查询或拼接查询已落地
- [ ] 数据库迁移成功
- [ ] `compliance_report.json` 统计与实际问题一致

---

## 6. JSON 输出要求

### 6.1 必填字段

- `project_name`
- `difficulty_level`
- `source_vuln_plan`
- `generated_date`（格式：`YYYY-MM-DD`）
- `total_issues`
- `summary.by_severity`
- `summary.by_category`
- `issues[]`

### 6.2 统计一致性规则

- `total_issues = len(issues)`
- `summary.by_severity` 必须等于 `issues[].severity` 实际计数
- `summary.by_category` 必须等于 `issues[].category` 实际计数
- 每个 issue 必须包含可追溯定位：`file` + `line` + `class_or_function`

### 6.3 输出示例

```json
{
  "project_name": "hard_example_project",
  "difficulty_level": "hard",
    "source_vuln_plan": "vuln_plan_hard_01.md",
    "generated_date": "2026-03-18",
  "total_issues": 10,
  "summary": {
    "by_severity": {
      "critical": 4,
      "high": 5,
      "medium": 1,
      "low": 0
    },
    "by_category": {
      "Multi-tenant Isolation": 1,
      "Sensitive Data Exposure": 2,
      "Async Task Data Leak": 1,
      "Sensitive Data in Cache": 1,
      "Unauthorized Access": 1,
      "Data Export": 1,
      "Data Retention & Anonymization": 1,
      "Complex SQL Injection": 1,
      "Third-party API": 1,
      "Field-level Authorization": 0
    }
  },
  "issues": [
    {
      "issue_id": "DC-001",
      "location": {
                "file": "core/views.py",
        "line": 25,
        "class_or_function": "ReportViewSet.get_queryset"
      },
      "category": "Multi-tenant Isolation",
      "description": "Missing tenant isolation in get_queryset - users can access reports from other organizations",
      "severity": "critical",
      "related_fields": ["organization"],
      "impact": "Data leakage across tenant boundaries, violating data segregation requirements",
      "code_snippet": "def get_queryset(self):\n    return Report.objects.all()  # Should filter by user's organization"
    }
  ]
}
```
