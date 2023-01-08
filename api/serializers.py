from rest_framework import serializers
from book.models import Book, CustomUser, BookReview


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'title', 'description', 'isbn')

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'last_name', 'first_name', 'email')

class BookReviewSerializer(serializers.ModelSerializer):
    book2 = BookSerializer(read_only=True)
    user = Userserializer(read_only=True)
    class Meta:
        model = BookReview
        fields = ('pk', 'star_given', 'comentary', 'book2', 'user')