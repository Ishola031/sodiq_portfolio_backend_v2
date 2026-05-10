from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project, Service
from .serializers import ProjectSerializer, ServiceSerializer
from .paginations import ProjectPagination
from django.views.decorators.cache import cache_page
from project.tasks import send_contact_email
# Cache for 5 minutes
@cache_page(60 * 5)
@api_view(['GET'])
def projectApi(request):
    category = request.GET.get('category', None)

    if category and category != 'All':
        projects = (
            Project.objects
            .select_related('category')
            .filter(category__slug=category)
        )
    else:
        projects = Project.objects.select_related('category').all()

    paginator = ProjectPagination()
    page = paginator.paginate_queryset(projects, request)

    serializer = ProjectSerializer(
        page,
        many=True,
        context={'request': request}
    )

    return paginator.get_paginated_response(serializer.data)

# Cache for 5 minutes
@cache_page(60 * 5)
@api_view(['GET'])
def serviceApi(request):
    services = Service.objects.all()

    serializer = ServiceSerializer(
        services,
        many=True,
        context={'request': request}
    )

    return Response(serializer.data)

@api_view(['POST'])
def send_email(request):
    data = request.data

    firstName = data.get("firstName")
    lastName = data.get("lastName")
    user_email = data.get("email")
    number = data.get("number")
    message = data.get("message")

    send_contact_email.delay(number, firstName,lastName,user_email, message)
    return Response({"message": "Email sent successfully"})