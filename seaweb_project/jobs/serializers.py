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

    def validate_structure(self, attrs, source):
        """
        Check that structure file is a gro file.
        """
        uploaded_file = attrs[source]
        if uploaded_file.name.endswith('.gro'):
            return attrs
        else:
            raise serializers.ValidationError('Structure file must be a .gro file.')

    def validate_topology(self, attrs, source):
        """
        Check that topology file is a top file.
        """
        uploaded_file = attrs[source]
        if uploaded_file.name.endswith('.top'):
            return attrs
        else:
            raise serializers.ValidationError('Topology file must be a .top file.')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.HyperlinkedRelatedField(many=True, view_name='job-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'jobs')
