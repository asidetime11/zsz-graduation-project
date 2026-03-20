from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Article, Comment, UserProfile
from .serializers import UserProfileSerializer


def article_detail(request: HttpRequest, article_id_path: int) -> HttpResponse:
	article = get_object_or_404(Article, id=article_id_path)
	comments = article.comments.select_related("author").all().order_by("-id")
	return render(request, "article_detail.html", {"article": article, "comments": comments})


def create_comment(request: HttpRequest) -> HttpResponse:
	if request.method == "POST":
		username = request.POST.get("username", "")
		user, _ = UserProfile.objects.get_or_create(
			username=username,
			defaults={
				"email": request.POST.get("email", ""),
				"phone": request.POST.get("phone", ""),
				"id_card": request.POST.get("id_card", ""),
				"occupation": request.POST.get("occupation", ""),
				"medical_history": request.POST.get("medical_history", ""),
				"marketing_agree": True,
			},
		)
		article_id = int(request.POST.get("article_id", "0") or 0)
		article = get_object_or_404(Article, id=article_id)
		Comment.objects.create(
			article=article,
			author=user,
			content=request.POST.get("content", ""),
		)
		return redirect("article_detail", article_id=article.id)

	latest_article = Article.objects.order_by("-id").first()
	return render(request, "add_comment.html", {"latest_article": latest_article})


def user_list(request: HttpRequest) -> HttpResponse:
	users = UserProfile.objects.all().order_by("-id")
	serializer = UserProfileSerializer(users, many=True)
	if request.headers.get("Accept") == "application/json":
		return JsonResponse(serializer.data, safe=False)
	return render(request, "user_list.html", {"users": serializer.data})
