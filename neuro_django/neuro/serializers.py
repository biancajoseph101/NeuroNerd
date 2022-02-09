from rest_framework import serializers
from .models import Tag, Post, ResourceType, Resource
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
        # many=True,
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
        fields = ('id', 'author', 'category', 'tag_id', 'user_id',
                  'title', 'date', 'content', 'image_url', 'source')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=True,
        read_only=True
    )
    user_url = serializers.ModelSerializer.serializer_url_field(
        view_name='user_detail')
    # post_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Post.objects.all(),
    #     source='posts'
    # )

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'is_logged_in', 'is_verified', 'posts', 'user_url')


class ResourceSerializer(serializers.ModelSerializer):
    resource_type = serializers.PrimaryKeyRelatedField(
        queryset=ResourceType.objects.all(),
        many=True
    )

    class Meta:
        model = Resource
        fields = ('id', 'resource_type', 'topic', 'link', 'image', 'content')


class ResourceTypeSerializer(serializers.ModelSerializer):
    resource_list = ResourceSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = ResourceType
        fields = ('id', 'resource_type', 'description',
                  'picture', 'resource_list')
