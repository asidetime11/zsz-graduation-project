from django.db import connection
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import Post, UserProfile
from .serializers import UserProfileSerializer


def search_posts(request: HttpRequest) -> HttpResponse:
	keyword = request.GET.get("keyword", "")
	print(f"search keyword={keyword}, request={request.GET.dict()}")

	results = []
	if keyword:
		sql = (
			"SELECT p.id, p.title, p.content, p.created_at, "
			"u.id, u.username, u.email, u.phone, u.bio "
			"FROM core_post p "
			"JOIN core_userprofile u ON p.user_id = u.id "
			f"WHERE p.title LIKE '%{keyword}%' OR p.content LIKE '%{keyword}%' "
			"ORDER BY p.created_at DESC"
		)
		with connection.cursor() as cursor:
			cursor.execute(sql)
			rows = cursor.fetchall()
		results = [
			{
				"post_id": row[0],
				"title": row[1],
				"content": row[2],
				"created_at": str(row[3]),
				"user": {
					"id": row[4],
					"username": row[5],
					"email": row[6],
					"phone": row[7],
					"bio": row[8],
				},
			}
			for row in rows
		]

	if request.headers.get("Accept") == "application/json":
		return JsonResponse(results, safe=False)
	return render(request, "search.html", {"results": results, "keyword": keyword})


def create_post(request: HttpRequest) -> HttpResponse:
	if request.method == "POST":
		username = request.POST.get("username", "")
		email = request.POST.get("email", "")
		phone = request.POST.get("phone", "")
		bio = request.POST.get("bio", "")

		user, _ = UserProfile.objects.get_or_create(
			username=username,
			defaults={"email": email, "phone": phone, "bio": bio},
		)

		Post.objects.create(
			user=user,
			title=request.POST.get("title", ""),
			content=request.POST.get("content", ""),
		)
		return redirect("search_posts")

	return render(request, "create_post.html")


def user_list(request: HttpRequest) -> HttpResponse:
	users = UserProfile.objects.all().order_by("-id")
	serializer = UserProfileSerializer(users, many=True)
	if request.headers.get("Accept") == "application/json":
		return JsonResponse(serializer.data, safe=False)
	return render(request, "user_list.html", {"users": serializer.data})
