from rest_framework import serializers
from .models import Tag, Post
from accounts.models import CustomUser


class TagSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_list',
        read_only=True
    )
    tag_url = serializers.ModelSerializer.serializer_url_field(
        view_name='tag_detail'
    )

    class Meta:
        model = Tag
        fields = ('id', 'category_name', 'description',
                  'image_url', 'posts', 'tag_url',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        source='author'
    )
    category = serializers.HyperlinkedRelatedField(
        view_name='tag_detail',
        read_only=True
    )
    tag_id = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        source='category'
    )

    class Meta:
        model = Post
        fields = ('id', 'author', 'category', 'tag_id', 'user_id'
                  'title', 'date', 'content', 'image_url', 'source')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=True,
        read_only=True
    )
    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail')
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        source='post'
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'is_logged_in', 'is_verified' 'posts', )
