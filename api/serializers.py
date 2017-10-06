from rest_framework import serializers
from account.models import User
from core.models import Video, Comment


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username','first_name','phone')


class VideoSerializer(serializers.ModelSerializer):

    uploader = BaseUserSerializer(read_only=True)

    class Meta:
        model = Video
        fields = ('id','uploader','title','description','category','views','file','thumbnail','created_at','updated_at')


class CommentSerializer(serializers.ModelSerializer):

	author = BaseUserSerializer(read_only=True)

	class Meta:
	    model = Comment
	    fields = ('id', 'author','content','video','created_at','updated_at')
