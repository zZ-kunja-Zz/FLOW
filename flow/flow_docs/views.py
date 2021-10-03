import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import User, Document, Viewer

# Create your views here.

def index(request):
    return render(request, "flow_docs/index.html")

def new(request):
    return render(request, "flow_docs/new.html")

#This function gets the people who are allowed to edit the document and passes it to the HTML
#I could have checked if the user was in the list of editors here but I want to add 
#UI in the future that shows all editors
def edit(request, document_id):
    document = Document.objects.get(id = document_id)
    viewers = Viewer.objects.filter(Document = document_id)
    editors = []
    for viewer in viewers:
        if viewer.canEdit:
            editors.append(viewer.User)
    return render(request, "flow_docs/edit.html", {
    "document_id": document_id,
    "title": document.title,
    "editors": editors
    })

#This function is very similar to the last one but it only checks for the viewer permission
#It also sends different information about the document.
def view(request, document_id):
    document = Document.objects.get(id = document_id)
    viewers = Viewer.objects.filter(Document = document_id)
    users = []
    for viewer in viewers:
        users.append(viewer.User)
    return render(request, "flow_docs/view.html", {
        "document": document,
        "users": users
    })

#This is an API function which will share a document with all users specified
#It goes through every user and creates a viewer object for them
@csrf_exempt
@login_required
def share(request, document_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)

    users = data.get("users", "")
    can_edit = data.get("can_edit", "")

    document = Document.objects.get(id = document_id)

    split_users = users.split(', ')

    for user in split_users:
        current_user = User.objects.get(email = user)
        if(current_user):
            new_viewer = Viewer.objects.create(User = current_user, Document = document, canEdit = can_edit)
            new_viewer.save()

    return HttpResponse(status=204)


def documentation(request):
    return render(request, "flow_docs/documentation.html")

#creates a document object with the specified body and title
@csrf_exempt
@login_required
def save(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    
    title = data.get("title", "")
    body = data.get("body", "")

    document = Document(
        owner = request.user,
        title = title,
        body = body,
    )

    document.save()

    viewer = Viewer(
        User = request.user,
        Document = document,
        canEdit = True
    )
    viewer.save()


    return JsonResponse(document.serialize())

#when called it will give the data from a certain document
#this being the owner, id, title, body and timestamp
@csrf_exempt
def document(request, document_id):
    try: 
        document = Document.objects.get(pk=document_id)
    except Document.DoesNotExist:
        return JsonResponse({"error": "Email not found."}, status=404)

    if request.method == "GET":
        return JsonResponse(document.serialize())

    elif request.method == "PUT":
        data = json.loads(request.body)
        if data.get("title") is not None:
            document.title = data["title"]
        if data.get("body") is not None:
            document.body = data["body"]
        document.save()
        return HttpResponse(status=204)

#this will sort and return all of the documents a user has saved
@login_required
def saved(request):
    saved_documents = Document.objects.filter(owner = request.user)
    saved_documents = saved_documents.order_by("-timestamp").all()
    return render(request, "flow_docs/saved.html", {
        "saved_documents" : saved_documents
    })

#this will sort and return all of the documents a user can view or edit
def all(request):
    viewable_documents = Viewer.objects.filter(User = request.user)
    viewable_documents = viewable_documents.order_by("-Document").all()
    documents = []
    for document in viewable_documents:
        documents.append(document.Document)
    return render(request, "flow_docs/all.html", {
        "documents": documents
    })

#stuff taken from past projects
def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse("index"))

        else:

            return render(request, "flow_docs/login.html", {
                "message": "Invalid username and/or password."
            })

    else:
        return render(request, "flow_docs/login.html")

@login_required
def logout_view(request):

    logout(request)

    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "flow_docs/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()

        except IntegrityError:
            
            return render(request, "flow_docs/register.html", {
                "message": "Username already taken."
            })
        
        login(request, user)

        return HttpResponseRedirect(reverse("index"))

    else:

        return render(request, "flow_docs/register.html")