from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status, permissions, renderers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.authtoken.models import Token
from django_browserid.base import BrowserIDException

from .models import Job, Result
from .permissions import IsOwner
from .serializers import JobSerializer, UserSerializer, ResultSerializer
from .tasks import run_sea_calculation


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def pre_save(self, obj):
        obj.owner = self.request.user
        obj.status = Job.STATUS.submitted

    def post_save(self, obj, created=False):
        if created:
            try:
                run_sea_calculation.delay(obj.id)
            except:
                obj.status = Job.STATUS.error
                obj.save()
                raise

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


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login(request):
    assertion = request.DATA.get('assertion', None)
    if not assertion:
        return Response(
            'assertion parameter is missing',
            status.HTTP_400_BAD_REQUEST
        )
    # TODO: Get audience from settings
    audience = 'http://127.0.0.1:9000'
    try:
        user = authenticate(
            assertion=assertion,
            audience=audience,
        )
        return Response({
            'email': user.email,
            'token': get_auth_token(user),
        })
    except BrowserIDException:
        return Response(
            'Authentication failed',
            status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

def get_auth_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token.key
