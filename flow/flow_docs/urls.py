from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("edit/<int:document_id>", views.edit, name="edit"),
    path("documentation", views.documentation, name="documentation"),
    path("saved", views.saved, name="saved"),
    path("view/<int:document_id>", views.view, name="view"),
    path("all", views.all, name="all"),

    # API routes
    path("share/<int:document_id>", views.share, name="share"),
    path("documents", views.save, name="save"),
    path("documents/<int:document_id>", views.document, name="document"),
    path("documents/all", views.all, name="all")
]