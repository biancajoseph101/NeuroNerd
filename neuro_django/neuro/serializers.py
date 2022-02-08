from rest_framework import serializers
from .models import Tag, Post, User


class TagSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_list',
        many=True,
        read_only=True
    )
    tag_url = serializers.ModelSerializer.serializer_url_field(
        view_name='tag_detail'
    )

    class Meta:
        model = Tag
        fields = ('id', 'category_name', 'description',
                  'image_url', 'posts',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='username'
    )
    category = serializers.HyperlinkedRelatedField(
        view_name='tag_detail',
        read_only=True
    )
    tag_id = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        source='category_name'
    )

    class Meta:
        model = Post
        fields = ('id', 'author', 'user_id', 'category', 'tag_id',
                  'title', 'date', 'content', 'image_url', 'source')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'is_logged_in', 'posts')
