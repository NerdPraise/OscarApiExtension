# Third party import
from rest_framework import status, viewsets

# Django import
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Local Import
from .serializers import UserViewSerializer

User = get_user_model()


class UserViewAPI(viewsets.ViewSet):
    """
    A simple viewset for users to create, list or update instance
    """
    model = User
    serializer_class = UserViewSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            print(serializer.save())
            return JsonResponse(serializer.data, safe=False,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def update(self, request, pk=None):
        if pk:
            user = get_object_or_404(User, pk=pk)

            serializer = self.serializer_class(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False,
                                    status=status.HTTP_202_ACCEPTED)
            return JsonResponse(serializer.errors, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
