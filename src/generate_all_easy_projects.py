from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent

BASE = Path(r"c:\Users\29281\Desktop\毕设\project\django\easy")
TODAY = "2026-03-18"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


MANAGE_PY = dedent(
    """\
    #!/usr/bin/env python
    import os
    import sys


    def main():
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)


    if __name__ == "__main__":
        main()
    """
)

ASGI = dedent(
    """\
    import os
    from django.core.asgi import get_asgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    application = get_asgi_application()
    """
)

WSGI = dedent(
    """\
    import os
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    application = get_wsgi_application()
    """
)


def settings_py(secret: str) -> str:
    return dedent(
        f"""\
        from pathlib import Path

        BASE_DIR = Path(__file__).resolve().parent.parent
        SECRET_KEY = {secret!r}
        DEBUG = True
        ALLOWED_HOSTS = []

        INSTALLED_APPS = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "core",
        ]

        MIDDLEWARE = [
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ]

        ROOT_URLCONF = "project.urls"
        TEMPLATES = [
            {{
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [BASE_DIR / "templates"],
                "APP_DIRS": True,
                "OPTIONS": {{
                    "context_processors": [
                        "django.template.context_processors.request",
                        "django.contrib.auth.context_processors.auth",
                        "django.contrib.messages.context_processors.messages",
                    ],
                }},
            }}
        ]

        WSGI_APPLICATION = "project.wsgi.application"

        DATABASES = {{
            "default": {{
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }}
        }}

        AUTH_PASSWORD_VALIDATORS = []

        LANGUAGE_CODE = "zh-hans"
        TIME_ZONE = "Asia/Shanghai"
        USE_I18N = True
        USE_TZ = True

        STATIC_URL = "static/"
        DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
        """
    )


ROOT_URLS = dedent(
    """\
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("", include("core.urls")),
    ]
    """
)

APPS = dedent(
    """\
    from django.apps import AppConfig


    class CoreConfig(AppConfig):
        default_auto_field = "django.db.models.BigAutoField"
        name = "core"
    """
)

PROJECTS = {
    "example02": {
        "model": dedent(
            """\
            from django.db import models


            class CandidateProfile(models.Model):
                name = models.CharField(max_length=100)
                email = models.EmailField()
                id_card = models.CharField(max_length=20)  # 明文敏感信息
                phone = models.CharField(max_length=20)
                marital_status = models.CharField(max_length=30)  # 不必要收集
                religion = models.CharField(max_length=50)  # 不必要收集
                medical_history = models.TextField(blank=True)  # 不必要收集
                created_at = models.DateTimeField(auto_now_add=True)
            """
        ),
        "views": dedent(
            """\
            from django.shortcuts import redirect, render
            from .models import CandidateProfile


            def submit_resume(request):
                if request.method == "POST":
                    CandidateProfile.objects.create(
                        name=request.POST.get("name", ""),
                        email=request.POST.get("email", ""),
                        id_card=request.POST.get("id_card", ""),
                        phone=request.POST.get("phone", ""),
                        marital_status=request.POST.get("marital_status", ""),
                        religion=request.POST.get("religion", ""),
                        medical_history=request.POST.get("medical_history", ""),
                    )
                    return redirect("resume_list")
                return render(request, "submit.html")


            def resume_list(request):
                resumes = CandidateProfile.objects.all().order_by("-id")
                return render(request, "resume_list.html", {"resumes": resumes})
            """
        ),
        "urls": dedent(
            """\
            from django.urls import path
            from .views import resume_list, submit_resume

            urlpatterns = [
                path("resume/submit/", submit_resume, name="submit_resume"),
                path("resumes/", resume_list, name="resume_list"),
            ]
            """
        ),
        "templates": {
            "submit.html": "<h1>简历提交</h1><form method='post'>{% csrf_token %}<input name='name' placeholder='姓名'><input name='email' placeholder='邮箱'><input name='id_card' placeholder='身份证'><input name='phone' placeholder='手机号'><input name='marital_status' placeholder='婚姻状况'><input name='religion' placeholder='宗教'><textarea name='medical_history' placeholder='病史'></textarea><button type='submit'>提交</button></form><a href='/resumes/'>查看简历列表</a>",
            "resume_list.html": "<h1>简历列表</h1><table border='1'><tr><th>姓名</th><th>邮箱</th><th>身份证</th><th>手机号</th><th>婚姻状况</th><th>宗教</th><th>病史</th></tr>{% for r in resumes %}<tr><td>{{ r.name }}</td><td>{{ r.email }}</td><td>{{ r.id_card }}</td><td>{{ r.phone }}</td><td>{{ r.marital_status }}</td><td>{{ r.religion }}</td><td>{{ r.medical_history }}</td></tr>{% endfor %}</table>",
        },
        "report": {
            "project_name": "easy_02",
            "difficulty_level": "easy",
            "source_vuln_plan": "vuln_plan_easy_02.md",
            "generated_date": TODAY,
            "total_issues": 3,
            "summary": {
                "by_severity": {"critical": 1, "high": 2, "medium": 0, "low": 0},
                "by_category": {
                    "Sensitive Data Exposure": 1,
                    "Data Minimization": 1,
                    "Data Over-exposure": 1,
                    "Missing Consent": 0,
                    "Unauthorized Access": 0,
                    "Data Lifecycle": 0,
                    "SQL Injection": 0,
                    "XSS": 0,
                    "Sensitive Logging": 0,
                    "Hardcoded Secrets": 0,
                },
            },
            "issues": [
                {"issue_id": "DC-001", "location": {"file": "core/models.py", "line": 7, "class_or_function": "CandidateProfile"}, "category": "Data Minimization", "description": "Collects marital status, religion and medical history irrelevant to resume submission.", "severity": "high", "related_fields": ["marital_status", "religion", "medical_history"], "impact": "Excessive collection increases compliance risk.", "code_snippet": "marital_status = models.CharField(max_length=30)"},
                {"issue_id": "DC-002", "location": {"file": "core/models.py", "line": 6, "class_or_function": "CandidateProfile"}, "category": "Sensitive Data Exposure", "description": "ID card stored in plaintext.", "severity": "critical", "related_fields": ["id_card"], "impact": "Identity data leak risk.", "code_snippet": "id_card = models.CharField(max_length=20)"},
                {"issue_id": "DC-003", "location": {"file": "core/views.py", "line": 20, "class_or_function": "resume_list"}, "category": "Data Over-exposure", "description": "Resume list page exposes all fields including sensitive attributes.", "severity": "high", "related_fields": ["id_card", "medical_history"], "impact": "Sensitive resume data exposed to broad viewers.", "code_snippet": "resumes = CandidateProfile.objects.all()"},
            ],
        },
    },
    "example03": {
        "model": dedent(
            """\
            from django.db import models


            class StudentProfile(models.Model):
                name = models.CharField(max_length=100)
                id_card = models.CharField(max_length=20)
                phone = models.CharField(max_length=20)
                address = models.CharField(max_length=200)
                gpa = models.FloatField(default=0)
                family_income = models.CharField(max_length=50)
                created_at = models.DateTimeField(auto_now_add=True)
            """
        ),
        "views": dedent(
            """\
            from django.shortcuts import get_object_or_404, render
            from .models import StudentProfile


            def search_students(request):
                students = StudentProfile.objects.all().order_by("-id")
                return render(request, "search.html", {"students": students})


            def student_detail(request, student_id):
                student = get_object_or_404(StudentProfile, pk=student_id)
                return render(request, "detail.html", {"student": student})
            """
        ),
        "urls": dedent(
            """\
            from django.urls import path
            from .views import search_students, student_detail

            urlpatterns = [
                path("students/", search_students, name="students"),
                path("students/<int:student_id>/", student_detail, name="student_detail"),
            ]
            """
        ),
        "templates": {
            "search.html": "<h1>学生查询</h1><ul>{% for s in students %}<li><a href='/students/{{ s.id }}/'>{{ s.name }} - {{ s.id_card }} - {{ s.family_income }}</a></li>{% endfor %}</ul>",
            "detail.html": "<h1>学生详情</h1><p>姓名: {{ student.name }}</p><p>身份证: {{ student.id_card }}</p><p>电话: {{ student.phone }}</p><p>地址: {{ student.address }}</p><p>GPA: {{ student.gpa }}</p><p>家庭收入: {{ student.family_income }}</p>",
        },
        "report": {
            "project_name": "easy_03",
            "difficulty_level": "easy",
            "source_vuln_plan": "vuln_plan_easy_03.md",
            "generated_date": TODAY,
            "total_issues": 3,
            "summary": {
                "by_severity": {"critical": 1, "high": 2, "medium": 0, "low": 0},
                "by_category": {"Sensitive Data Exposure": 1, "Data Minimization": 0, "Data Over-exposure": 1, "Missing Consent": 1, "Unauthorized Access": 0, "Data Lifecycle": 0, "SQL Injection": 0, "XSS": 0, "Sensitive Logging": 0, "Hardcoded Secrets": 0},
            },
            "issues": [
                {"issue_id": "DC-001", "location": {"file": "core/views.py", "line": 6, "class_or_function": "search_students"}, "category": "Data Over-exposure", "description": "Student query returns all fields including id_card and family_income.", "severity": "high", "related_fields": ["id_card", "family_income"], "impact": "Sensitive student data exposed.", "code_snippet": "students = StudentProfile.objects.all()"},
                {"issue_id": "DC-002", "location": {"file": "core/models.py", "line": 6, "class_or_function": "StudentProfile"}, "category": "Sensitive Data Exposure", "description": "Sensitive fields are plaintext in database.", "severity": "critical", "related_fields": ["id_card", "family_income"], "impact": "Sensitive data leakage risk.", "code_snippet": "id_card = models.CharField(max_length=20)"},
                {"issue_id": "DC-003", "location": {"file": "core/models.py", "line": 4, "class_or_function": "StudentProfile"}, "category": "Missing Consent", "description": "No consent flag for student data query/sharing.", "severity": "high", "related_fields": [], "impact": "Cannot prove lawful processing basis.", "code_snippet": "class StudentProfile(models.Model):"},
            ],
        },
    },
    "example04": {
        "model": dedent(
            """\
            from django.db import models


            class Subscriber(models.Model):
                name = models.CharField(max_length=100)
                email = models.EmailField()
                phone = models.CharField(max_length=20)
                birth_date = models.DateField(null=True, blank=True)
                address = models.CharField(max_length=200, blank=True)
                created_at = models.DateTimeField(auto_now_add=True)
            """
        ),
        "views": dedent(
            """\
            from django.shortcuts import redirect, render
            from .models import Subscriber


            def subscribe(request):
                if request.method == "POST":
                    Subscriber.objects.create(
                        name=request.POST.get("name", ""),
                        email=request.POST.get("email", ""),
                        phone=request.POST.get("phone", ""),
                        birth_date=request.POST.get("birth_date") or None,
                        address=request.POST.get("address", ""),
                    )
                    return redirect("subscriber_list")
                return render(request, "subscribe.html")


            def subscriber_list(request):
                data = Subscriber.objects.all().order_by("-id")
                return render(request, "subscriber_list.html", {"subs": data})
            """
        ),
        "urls": dedent(
            """\
            from django.urls import path
            from .views import subscribe, subscriber_list

            urlpatterns = [
                path("subscribe/", subscribe, name="subscribe"),
                path("subscribers/", subscriber_list, name="subscriber_list"),
            ]
            """
        ),
        "templates": {
            "subscribe.html": "<h1>订阅</h1><form method='post'>{% csrf_token %}<input name='name' placeholder='姓名'><input name='email' placeholder='邮箱'><input name='phone' placeholder='手机号'><input name='birth_date' placeholder='出生日期'><input name='address' placeholder='地址'><button type='submit'>提交</button></form>",
            "subscriber_list.html": "<h1>订阅者</h1><table border='1'><tr><th>姓名</th><th>邮箱</th><th>电话</th><th>生日</th><th>地址</th></tr>{% for s in subs %}<tr><td>{{ s.name }}</td><td>{{ s.email }}</td><td>{{ s.phone }}</td><td>{{ s.birth_date }}</td><td>{{ s.address }}</td></tr>{% endfor %}</table>",
        },
        "report": {
            "project_name": "easy_04",
            "difficulty_level": "easy",
            "source_vuln_plan": "vuln_plan_easy_04.md",
            "generated_date": TODAY,
            "total_issues": 3,
            "summary": {
                "by_severity": {"critical": 1, "high": 2, "medium": 0, "low": 0},
                "by_category": {"Sensitive Data Exposure": 1, "Data Minimization": 1, "Data Over-exposure": 0, "Missing Consent": 1, "Unauthorized Access": 0, "Data Lifecycle": 0, "SQL Injection": 0, "XSS": 0, "Sensitive Logging": 0, "Hardcoded Secrets": 0},
            },
            "issues": [
                {"issue_id": "DC-001", "location": {"file": "core/models.py", "line": 4, "class_or_function": "Subscriber"}, "category": "Missing Consent", "description": "No consent/audit fields for subscription collection.", "severity": "high", "related_fields": [], "impact": "Unable to track authorization.", "code_snippet": "class Subscriber(models.Model):"},
                {"issue_id": "DC-002", "location": {"file": "core/models.py", "line": 7, "class_or_function": "Subscriber"}, "category": "Sensitive Data Exposure", "description": "Phone stored in plaintext.", "severity": "critical", "related_fields": ["phone"], "impact": "Contact data leakage risk.", "code_snippet": "phone = models.CharField(max_length=20)"},
                {"issue_id": "DC-003", "location": {"file": "core/models.py", "line": 8, "class_or_function": "Subscriber"}, "category": "Data Minimization", "description": "Birth date and address collected for newsletter subscription.", "severity": "high", "related_fields": ["birth_date", "address"], "impact": "Unnecessary personal data processing.", "code_snippet": "birth_date = models.DateField(null=True, blank=True)"},
            ],
        },
    },
    "example05": {
        "model": dedent(
            """\
            from django.db import models


            class ParcelRecord(models.Model):
                name = models.CharField(max_length=100)
                phone = models.CharField(max_length=20)
                id_card = models.CharField(max_length=20)
                address = models.CharField(max_length=200)
                parcel_no = models.CharField(max_length=50)
                status = models.CharField(max_length=30, default="pending")
                created_at = models.DateTimeField(auto_now_add=True)
            """
        ),
        "views": dedent(
            """\
            from django.shortcuts import get_object_or_404, redirect, render
            from .models import ParcelRecord


            def create_parcel(request):
                if request.method == "POST":
                    rec = ParcelRecord.objects.create(
                        name=request.POST.get("name", ""),
                        phone=request.POST.get("phone", ""),
                        id_card=request.POST.get("id_card", ""),
                        address=request.POST.get("address", ""),
                        parcel_no=request.POST.get("parcel_no", ""),
                        status=request.POST.get("status", "pending"),
                    )
                    return redirect("parcel_detail", rec.id)
                return render(request, "register.html")


            def parcel_detail(request, record_id):
                # 未做对象级权限校验
                record = get_object_or_404(ParcelRecord, pk=record_id)
                return render(request, "detail.html", {"record": record})
            """
        ),
        "urls": dedent(
            """\
            from django.urls import path
            from .views import create_parcel, parcel_detail

            urlpatterns = [
                path("parcel/create/", create_parcel, name="create_parcel"),
                path("parcel/<int:record_id>/", parcel_detail, name="parcel_detail"),
            ]
            """
        ),
        "templates": {
            "register.html": "<h1>取件登记</h1><form method='post'>{% csrf_token %}<input name='name' placeholder='姓名'><input name='phone' placeholder='手机号'><input name='id_card' placeholder='身份证'><input name='address' placeholder='地址'><input name='parcel_no' placeholder='快递单号'><button type='submit'>登记</button></form>",
            "detail.html": "<h1>取件详情</h1><p>{{ record.name }}</p><p>{{ record.phone }}</p><p>{{ record.id_card }}</p><p>{{ record.address }}</p><p>{{ record.parcel_no }}</p><p>{{ record.status }}</p>",
        },
        "report": {
            "project_name": "easy_05",
            "difficulty_level": "easy",
            "source_vuln_plan": "vuln_plan_easy_05.md",
            "generated_date": TODAY,
            "total_issues": 3,
            "summary": {
                "by_severity": {"critical": 2, "high": 1, "medium": 0, "low": 0},
                "by_category": {"Sensitive Data Exposure": 1, "Data Minimization": 0, "Data Over-exposure": 1, "Missing Consent": 0, "Unauthorized Access": 1, "Data Lifecycle": 0, "SQL Injection": 0, "XSS": 0, "Sensitive Logging": 0, "Hardcoded Secrets": 0},
            },
            "issues": [
                {"issue_id": "DC-001", "location": {"file": "core/views.py", "line": 20, "class_or_function": "parcel_detail"}, "category": "Unauthorized Access", "description": "Direct object access by id without permission checks (IDOR).", "severity": "critical", "related_fields": ["record_id"], "impact": "Any user can read others' parcel records.", "code_snippet": "record = get_object_or_404(ParcelRecord, pk=record_id)"},
                {"issue_id": "DC-002", "location": {"file": "core/models.py", "line": 6, "class_or_function": "ParcelRecord"}, "category": "Sensitive Data Exposure", "description": "Phone, id card and address stored in plaintext.", "severity": "critical", "related_fields": ["phone", "id_card", "address"], "impact": "Private contact data exposed on DB compromise.", "code_snippet": "id_card = models.CharField(max_length=20)"},
                {"issue_id": "DC-003", "location": {"file": "core/views.py", "line": 21, "class_or_function": "parcel_detail"}, "category": "Data Over-exposure", "description": "Detail page displays full personal fields.", "severity": "high", "related_fields": ["phone", "id_card", "address"], "impact": "Excessive data exposure in UI.", "code_snippet": "return render(request, 'detail.html', {'record': record})"},
            ],
        },
    },
    "example06": {
        "model": dedent(
            """\
            from django.db import models


            class BorrowRecord(models.Model):
                name = models.CharField(max_length=100)
                id_card = models.CharField(max_length=20)
                phone = models.CharField(max_length=20)
                book_title = models.CharField(max_length=200)
                borrow_date = models.DateField(null=True, blank=True)
                return_date = models.DateField(null=True, blank=True)
                created_at = models.DateTimeField(auto_now_add=True)
            """
        ),
        "views": dedent(
            """\
            from django.db import connection
            from django.shortcuts import redirect, render
            from .models import BorrowRecord


            def search(request):
                keyword = request.GET.get("keyword", "")
                query = f"SELECT id,name,id_card,phone,book_title,borrow_date,return_date,created_at FROM core_borrowrecord WHERE book_title LIKE '%{keyword}%'"
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    rows = cursor.fetchall()
                return render(request, "search.html", {"rows": rows})


            def borrow(request):
                if request.method == "POST":
                    BorrowRecord.objects.create(
                        name=request.POST.get("name", ""),
                        id_card=request.POST.get("id_card", ""),
                        phone=request.POST.get("phone", ""),
                        book_title=request.POST.get("book_title", ""),
                        borrow_date=request.POST.get("borrow_date") or None,
                        return_date=request.POST.get("return_date") or None,
                    )
                    return redirect("search")
                return render(request, "borrow.html")
            """
        ),
        "urls": dedent(
            """\
            from django.urls import path
            from .views import borrow, search

            urlpatterns = [
                path("search/", search, name="search"),
                path("borrow/", borrow, name="borrow"),
            ]
            """
        ),
        "templates": {
            "search.html": "<h1>借阅搜索</h1><form method='get'><input name='keyword' placeholder='书名关键字'><button type='submit'>搜索</button></form><table border='1'><tr><th>姓名</th><th>身份证</th><th>电话</th><th>书名</th></tr>{% for r in rows %}<tr><td>{{ r.1 }}</td><td>{{ r.2 }}</td><td>{{ r.3 }}</td><td>{{ r.4 }}</td></tr>{% endfor %}</table><a href='/borrow/'>登记借阅</a>",
            "borrow.html": "<h1>借阅登记</h1><form method='post'>{% csrf_token %}<input name='name' placeholder='姓名'><input name='id_card' placeholder='身份证'><input name='phone' placeholder='电话'><input name='book_title' placeholder='书名'><input name='borrow_date' placeholder='借阅日期'><input name='return_date' placeholder='归还日期'><button type='submit'>提交</button></form>",
        },
        "report": {
            "project_name": "easy_06",
            "difficulty_level": "easy",
            "source_vuln_plan": "vuln_plan_easy_06.md",
            "generated_date": TODAY,
            "total_issues": 3,
            "summary": {
                "by_severity": {"critical": 2, "high": 1, "medium": 0, "low": 0},
                "by_category": {"Sensitive Data Exposure": 1, "Data Minimization": 0, "Data Over-exposure": 1, "Missing Consent": 0, "Unauthorized Access": 0, "Data Lifecycle": 0, "SQL Injection": 1, "XSS": 0, "Sensitive Logging": 0, "Hardcoded Secrets": 0},
            },
            "issues": [
                {"issue_id": "DC-001", "location": {"file": "core/views.py", "line": 8, "class_or_function": "search"}, "category": "SQL Injection", "description": "Search query concatenates user input directly into SQL.", "severity": "critical", "related_fields": ["keyword"], "impact": "Attacker can inject SQL clauses.", "code_snippet": "query = f\"SELECT ... LIKE '%{keyword}%'\""},
                {"issue_id": "DC-002", "location": {"file": "core/models.py", "line": 6, "class_or_function": "BorrowRecord"}, "category": "Sensitive Data Exposure", "description": "Borrower id_card stored in plaintext.", "severity": "critical", "related_fields": ["id_card"], "impact": "Identity exposure risk.", "code_snippet": "id_card = models.CharField(max_length=20)"},
                {"issue_id": "DC-003", "location": {"file": "templates/search.html", "line": 1, "class_or_function": "search page"}, "category": "Data Over-exposure", "description": "Search result page displays full id card and phone fields.", "severity": "high", "related_fields": ["id_card", "phone"], "impact": "Sensitive borrowing data exposed.", "code_snippet": "<td>{{ r.2 }}</td><td>{{ r.3 }}</td>"},
            ],
        },
    },
    "example07": {
        "model": dedent(
            """\
            from django.db import models


            class Feedback(models.Model):
                name = models.CharField(max_length=100)
                email = models.EmailField()
                phone = models.CharField(max_length=20)
                feedback_content = models.TextField()
                created_at = models.DateTimeField(auto_now_add=True)
            """
        ),
        "views": dedent(
            """\
            from django.shortcuts import redirect, render
            from .models import Feedback


            def feedback(request):
                if request.method == "POST":
                    Feedback.objects.create(
                        name=request.POST.get("name", ""),
                        email=request.POST.get("email", ""),
                        phone=request.POST.get("phone", ""),
                        feedback_content=request.POST.get("feedback_content", ""),
                    )
                    return redirect("feedback_list")
                return render(request, "feedback.html")


            def feedback_list(request):
                items = Feedback.objects.all().order_by("-id")
                return render(request, "feedback_list.html", {"items": items})
            """
        ),
        "urls": dedent(
            """\
            from django.urls import path
            from .views import feedback, feedback_list

            urlpatterns = [
                path("feedback/", feedback, name="feedback"),
                path("feedbacks/", feedback_list, name="feedback_list"),
            ]
            """
        ),
        "templates": {
            "feedback.html": "<h1>反馈提交</h1><form method='post'>{% csrf_token %}<input name='name' placeholder='姓名'><input name='email' placeholder='邮箱'><input name='phone' placeholder='手机号'><textarea name='feedback_content' placeholder='反馈内容'></textarea><button type='submit'>提交</button></form>",
            "feedback_list.html": "{% load static %}<h1>反馈列表</h1><ul>{% for i in items %}<li><b>{{ i.name }}</b> {{ i.phone }} {{ i.email }}<div>{{ i.feedback_content|safe }}</div></li>{% endfor %}</ul>",
        },
        "report": {
            "project_name": "easy_07",
            "difficulty_level": "easy",
            "source_vuln_plan": "vuln_plan_easy_07.md",
            "generated_date": TODAY,
            "total_issues": 3,
            "summary": {
                "by_severity": {"critical": 1, "high": 2, "medium": 0, "low": 0},
                "by_category": {"Sensitive Data Exposure": 1, "Data Minimization": 0, "Data Over-exposure": 0, "Missing Consent": 1, "Unauthorized Access": 0, "Data Lifecycle": 0, "SQL Injection": 0, "XSS": 1, "Sensitive Logging": 0, "Hardcoded Secrets": 0},
            },
            "issues": [
                {"issue_id": "DC-001", "location": {"file": "templates/feedback_list.html", "line": 1, "class_or_function": "feedback list"}, "category": "XSS", "description": "Feedback content rendered with |safe, enabling stored XSS.", "severity": "high", "related_fields": ["feedback_content"], "impact": "Script execution in admin/browser context.", "code_snippet": "{{ i.feedback_content|safe }}"},
                {"issue_id": "DC-002", "location": {"file": "core/models.py", "line": 7, "class_or_function": "Feedback"}, "category": "Sensitive Data Exposure", "description": "Email and phone stored in plaintext.", "severity": "critical", "related_fields": ["email", "phone"], "impact": "Contact data leak risk.", "code_snippet": "phone = models.CharField(max_length=20)"},
                {"issue_id": "DC-003", "location": {"file": "core/models.py", "line": 4, "class_or_function": "Feedback"}, "category": "Missing Consent", "description": "No consent field for collecting contact information.", "severity": "high", "related_fields": [], "impact": "Lack of lawful basis evidence.", "code_snippet": "class Feedback(models.Model):"},
            ],
        },
    },
    "example08": {
        "model": dedent(
            """\
            from django.db import models


            class SupportTicket(models.Model):
                name = models.CharField(max_length=100)
                id_card = models.CharField(max_length=20)
                phone = models.CharField(max_length=20)
                email = models.EmailField()
                ticket_content = models.TextField()
                status = models.CharField(max_length=30, default="open")
                created_at = models.DateTimeField(auto_now_add=True)
            """
        ),
        "views": dedent(
            """\
            import logging
            from django.shortcuts import redirect, render
            from .models import SupportTicket

            logger = logging.getLogger(__name__)


            def create_ticket(request):
                if request.method == "POST":
                    logger.info("ticket request body: %s", request.POST.dict())
                    SupportTicket.objects.create(
                        name=request.POST.get("name", ""),
                        id_card=request.POST.get("id_card", ""),
                        phone=request.POST.get("phone", ""),
                        email=request.POST.get("email", ""),
                        ticket_content=request.POST.get("ticket_content", ""),
                        status=request.POST.get("status", "open"),
                    )
                    return redirect("ticket_list")
                return render(request, "create_ticket.html")


            def ticket_list(request):
                tickets = SupportTicket.objects.all().order_by("-id")
                return render(request, "ticket_list.html", {"tickets": tickets})
            """
        ),
        "urls": dedent(
            """\
            from django.urls import path
            from .views import create_ticket, ticket_list

            urlpatterns = [
                path("ticket/create/", create_ticket, name="create_ticket"),
                path("tickets/", ticket_list, name="ticket_list"),
            ]
            """
        ),
        "templates": {
            "create_ticket.html": "<h1>创建工单</h1><form method='post'>{% csrf_token %}<input name='name' placeholder='姓名'><input name='id_card' placeholder='身份证'><input name='phone' placeholder='手机号'><input name='email' placeholder='邮箱'><textarea name='ticket_content' placeholder='问题描述'></textarea><button type='submit'>提交工单</button></form>",
            "ticket_list.html": "<h1>工单列表</h1><table border='1'><tr><th>姓名</th><th>身份证</th><th>电话</th><th>邮箱</th><th>内容</th><th>状态</th></tr>{% for t in tickets %}<tr><td>{{ t.name }}</td><td>{{ t.id_card }}</td><td>{{ t.phone }}</td><td>{{ t.email }}</td><td>{{ t.ticket_content }}</td><td>{{ t.status }}</td></tr>{% endfor %}</table>",
        },
        "report": {
            "project_name": "easy_08",
            "difficulty_level": "easy",
            "source_vuln_plan": "vuln_plan_easy_08.md",
            "generated_date": TODAY,
            "total_issues": 3,
            "summary": {
                "by_severity": {"critical": 1, "high": 2, "medium": 0, "low": 0},
                "by_category": {"Sensitive Data Exposure": 1, "Data Minimization": 0, "Data Over-exposure": 1, "Missing Consent": 0, "Unauthorized Access": 0, "Data Lifecycle": 0, "SQL Injection": 0, "XSS": 0, "Sensitive Logging": 1, "Hardcoded Secrets": 0},
            },
            "issues": [
                {"issue_id": "DC-001", "location": {"file": "core/views.py", "line": 10, "class_or_function": "create_ticket"}, "category": "Sensitive Logging", "description": "Logs full request payload containing id card and phone.", "severity": "high", "related_fields": ["id_card", "phone"], "impact": "Sensitive data leaks to logs.", "code_snippet": "logger.info('ticket request body: %s', request.POST.dict())"},
                {"issue_id": "DC-002", "location": {"file": "core/models.py", "line": 6, "class_or_function": "SupportTicket"}, "category": "Sensitive Data Exposure", "description": "ID card stored in plaintext.", "severity": "critical", "related_fields": ["id_card"], "impact": "Identity data leakage risk.", "code_snippet": "id_card = models.CharField(max_length=20)"},
                {"issue_id": "DC-003", "location": {"file": "core/views.py", "line": 24, "class_or_function": "ticket_list"}, "category": "Data Over-exposure", "description": "Ticket list displays all sensitive fields.", "severity": "high", "related_fields": ["id_card", "phone", "email"], "impact": "Unnecessary broad exposure of personal data.", "code_snippet": "tickets = SupportTicket.objects.all().order_by('-id')"},
            ],
        },
    },
    "example09": {
        "model": dedent(
            """\
            from django.db import models


            class CouponUser(models.Model):
                name = models.CharField(max_length=100)
                phone = models.CharField(max_length=20)
                id_card = models.CharField(max_length=20)
                occupation = models.CharField(max_length=100)
                income_level = models.CharField(max_length=100)
                coupon_code = models.CharField(max_length=50)
                claimed_at = models.DateTimeField(auto_now_add=True)
            """
        ),
        "views": dedent(
            """\
            from django.shortcuts import redirect, render
            from .models import CouponUser


            def claim(request):
                if request.method == "POST":
                    CouponUser.objects.create(
                        name=request.POST.get("name", ""),
                        phone=request.POST.get("phone", ""),
                        id_card=request.POST.get("id_card", ""),
                        occupation=request.POST.get("occupation", ""),
                        income_level=request.POST.get("income_level", ""),
                        coupon_code=request.POST.get("coupon_code", ""),
                    )
                    return redirect("record_list")
                return render(request, "claim.html")


            def record_list(request):
                records = CouponUser.objects.all().order_by("-id")
                return render(request, "record_list.html", {"records": records})
            """
        ),
        "urls": dedent(
            """\
            from django.urls import path
            from .views import claim, record_list

            urlpatterns = [
                path("coupon/claim/", claim, name="claim"),
                path("coupons/", record_list, name="record_list"),
            ]
            """
        ),
        "templates": {
            "claim.html": "<h1>优惠券领取</h1><form method='post'>{% csrf_token %}<input name='name' placeholder='姓名'><input name='phone' placeholder='手机号'><input name='id_card' placeholder='身份证'><input name='occupation' placeholder='职业'><input name='income_level' placeholder='收入水平'><input name='coupon_code' placeholder='优惠券码'><button type='submit'>领取</button></form>",
            "record_list.html": "<h1>领取记录</h1><table border='1'><tr><th>姓名</th><th>手机号</th><th>身份证</th><th>职业</th><th>收入</th><th>券码</th><th>时间</th></tr>{% for r in records %}<tr><td>{{ r.name }}</td><td>{{ r.phone }}</td><td>{{ r.id_card }}</td><td>{{ r.occupation }}</td><td>{{ r.income_level }}</td><td>{{ r.coupon_code }}</td><td>{{ r.claimed_at }}</td></tr>{% endfor %}</table>",
        },
        "report": {
            "project_name": "easy_09",
            "difficulty_level": "easy",
            "source_vuln_plan": "vuln_plan_easy_09.md",
            "generated_date": TODAY,
            "total_issues": 3,
            "summary": {
                "by_severity": {"critical": 1, "high": 1, "medium": 1, "low": 0},
                "by_category": {"Sensitive Data Exposure": 1, "Data Minimization": 1, "Data Over-exposure": 0, "Missing Consent": 0, "Unauthorized Access": 0, "Data Lifecycle": 1, "SQL Injection": 0, "XSS": 0, "Sensitive Logging": 0, "Hardcoded Secrets": 0},
            },
            "issues": [
                {"issue_id": "DC-001", "location": {"file": "core/models.py", "line": 6, "class_or_function": "CouponUser"}, "category": "Data Lifecycle", "description": "No retention or deletion strategy for coupon records.", "severity": "medium", "related_fields": ["claimed_at"], "impact": "User data retained indefinitely.", "code_snippet": "class CouponUser(models.Model):"},
                {"issue_id": "DC-002", "location": {"file": "core/models.py", "line": 7, "class_or_function": "CouponUser"}, "category": "Sensitive Data Exposure", "description": "Phone and id card stored in plaintext.", "severity": "critical", "related_fields": ["phone", "id_card"], "impact": "Sensitive data leakage risk.", "code_snippet": "id_card = models.CharField(max_length=20)"},
                {"issue_id": "DC-003", "location": {"file": "core/models.py", "line": 8, "class_or_function": "CouponUser"}, "category": "Data Minimization", "description": "Collects occupation and income level unrelated to coupon claim.", "severity": "high", "related_fields": ["occupation", "income_level"], "impact": "Excessive personal data collection.", "code_snippet": "income_level = models.CharField(max_length=100)"},
            ],
        },
    },
    "example10": {
        "model": dedent(
            """\
            from django.db import models


            class VisitorLog(models.Model):
                name = models.CharField(max_length=100)
                id_card = models.CharField(max_length=20)
                phone = models.CharField(max_length=20)
                company = models.CharField(max_length=200)
                visit_reason = models.CharField(max_length=200)
                host_name = models.CharField(max_length=100)
                visit_time = models.DateTimeField()
            """
        ),
        "views": dedent(
            """\
            from django.shortcuts import redirect, render
            from django.utils import timezone
            from .models import VisitorLog

            NOTIFY_API_KEY = "hardcoded_notify_key_visitor_001"


            def register(request):
                if request.method == "POST":
                    VisitorLog.objects.create(
                        name=request.POST.get("name", ""),
                        id_card=request.POST.get("id_card", ""),
                        phone=request.POST.get("phone", ""),
                        company=request.POST.get("company", ""),
                        visit_reason=request.POST.get("visit_reason", ""),
                        host_name=request.POST.get("host_name", ""),
                        visit_time=timezone.now(),
                    )
                    _ = NOTIFY_API_KEY
                    return redirect("visitor_list")
                return render(request, "register.html")


            def visitor_list(request):
                visitors = VisitorLog.objects.all().order_by("-visit_time")
                return render(request, "visitor_list.html", {"visitors": visitors})
            """
        ),
        "urls": dedent(
            """\
            from django.urls import path
            from .views import register, visitor_list

            urlpatterns = [
                path("visitor/register/", register, name="visitor_register"),
                path("visitors/", visitor_list, name="visitor_list"),
            ]
            """
        ),
        "templates": {
            "register.html": "<h1>访客登记</h1><form method='post'>{% csrf_token %}<input name='name' placeholder='姓名'><input name='id_card' placeholder='身份证'><input name='phone' placeholder='手机号'><input name='company' placeholder='单位'><input name='visit_reason' placeholder='来访事由'><input name='host_name' placeholder='被访人'><button type='submit'>登记</button></form>",
            "visitor_list.html": "<h1>访客列表</h1><table border='1'><tr><th>姓名</th><th>身份证</th><th>电话</th><th>单位</th><th>来访事由</th><th>被访人</th><th>来访时间</th></tr>{% for v in visitors %}<tr><td>{{ v.name }}</td><td>{{ v.id_card }}</td><td>{{ v.phone }}</td><td>{{ v.company }}</td><td>{{ v.visit_reason }}</td><td>{{ v.host_name }}</td><td>{{ v.visit_time }}</td></tr>{% endfor %}</table>",
        },
        "report": {
            "project_name": "easy_10",
            "difficulty_level": "easy",
            "source_vuln_plan": "vuln_plan_easy_10.md",
            "generated_date": TODAY,
            "total_issues": 3,
            "summary": {
                "by_severity": {"critical": 2, "high": 1, "medium": 0, "low": 0},
                "by_category": {"Sensitive Data Exposure": 1, "Data Minimization": 0, "Data Over-exposure": 1, "Missing Consent": 0, "Unauthorized Access": 0, "Data Lifecycle": 0, "SQL Injection": 0, "XSS": 0, "Sensitive Logging": 0, "Hardcoded Secrets": 1},
            },
            "issues": [
                {"issue_id": "DC-001", "location": {"file": "core/views.py", "line": 5, "class_or_function": "module scope"}, "category": "Hardcoded Secrets", "description": "Notification API key hardcoded in source code.", "severity": "critical", "related_fields": ["NOTIFY_API_KEY"], "impact": "Key exposure enables unauthorized third-party API usage.", "code_snippet": "NOTIFY_API_KEY = 'hardcoded_notify_key_visitor_001'"},
                {"issue_id": "DC-002", "location": {"file": "core/models.py", "line": 6, "class_or_function": "VisitorLog"}, "category": "Sensitive Data Exposure", "description": "Visitor id card and phone stored in plaintext.", "severity": "critical", "related_fields": ["id_card", "phone"], "impact": "Identity and contact data can be leaked.", "code_snippet": "id_card = models.CharField(max_length=20)"},
                {"issue_id": "DC-003", "location": {"file": "core/views.py", "line": 24, "class_or_function": "visitor_list"}, "category": "Data Over-exposure", "description": "Visitor list shows all personal fields including ID card.", "severity": "high", "related_fields": ["id_card", "phone"], "impact": "Overly broad disclosure of visitor data.", "code_snippet": "visitors = VisitorLog.objects.all().order_by('-visit_time')"},
            ],
        },
        "secret": "secret",
    },
}


def generate_project(name: str, cfg: dict) -> None:
    root = BASE / name
    core = root / "core"
    project = root / "project"
    templates = root / "templates"

    write(root / "manage.py", MANAGE_PY)
    write(project / "__init__.py", "")
    write(project / "asgi.py", ASGI)
    write(project / "wsgi.py", WSGI)
    write(project / "settings.py", settings_py(cfg.get("secret", f"django-insecure-{name}")))
    write(project / "urls.py", ROOT_URLS)

    write(core / "__init__.py", "")
    write(core / "apps.py", APPS)
    write(core / "admin.py", "from django.contrib import admin\n")
    write(core / "models.py", cfg["model"])
    write(core / "views.py", cfg["views"])
    write(core / "urls.py", cfg["urls"])
    write(core / "migrations" / "__init__.py", "")

    for tpl_name, tpl_content in cfg["templates"].items():
        write(templates / tpl_name, tpl_content)

    write(root / "compliance_report.json", json.dumps(cfg["report"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    for project_name, conf in PROJECTS.items():
        if project_name == "example01":
            continue
        generate_project(project_name, conf)
    print("Generated easy projects: example02-example10")
