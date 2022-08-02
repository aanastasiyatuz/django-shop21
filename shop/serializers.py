from rest_framework import serializers

from .models import Product, Category, Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["comments"] = CommentSerializer(instance.comments.all(), many=True).data
        rep["likes"] = instance.likes.all().count()
        return rep

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['user']

    def create(self, validated_data):
        validated_data["user"] = self.context.get("request").user
        return super().create(validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["user"] = instance.user.email
        return rep
