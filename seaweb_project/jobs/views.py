from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Job, Result
from .permissions import IsOwner
from .serializers import JobSerializer, UserSerializer, ResultSerializer
from .tasks import run_sea_calculation


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def pre_save(self, obj):
        obj.owner = self.request.user

    def post_save(self, obj, created=False):
        if created:
            obj.status = 'Queued'
            run_sea_calculation.delay(obj.id)

    def get_queryset(self):
            """
            This view should return a list of all the jobs
            for the currently authenticated user.
            """
            user = self.request.user
            return Job.objects.filter(owner=user)


class ResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
            """
            This view should return a list of all the jobs
            for the currently authenticated user.
            """
            user = self.request.user
            return Result.objects.filter(job__owner=user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
