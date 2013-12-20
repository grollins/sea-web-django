from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Job, Result


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result


class JobSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    result = ResultSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ('id', 'url', 'title', 'status', 'owner', 'structure', 'topology',
                  'iterations', 'result')
        read_only_fields = ('status',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.HyperlinkedRelatedField(many=True, view_name='job-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'jobs')
