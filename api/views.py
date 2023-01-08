from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from book.models import BookReview
from .serializers import BookReviewSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class BookReviewApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        book_review = BookReview.objects.get(pk=pk)
        serializer = BookReviewSerializer(book_review)
        return Response(data=serializer.data)

    def delete(self, request, pk):
        book_review = BookReview.objects.get(pk=pk)
        book_review.delete()
        return Response(data=request.data, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        book_review = BookReview.objects.get(pk=pk)
        serializer = BookReviewSerializer(instance=book_review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        book_review = BookReview.objects.get(pk=pk)
        serializer = BookReviewSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
        #
        # json_response = {
        #     'pk': book_review.pk,
        #     'star_given': book_review.star_given,
        #     'comment': book_review.comentary,
        #     'user': {
        #         'pk': book_review.user.pk,
        #         'first_name': book_review.user.first_name,
        #         'last_name': book_review.user.last_name,
        #         'email': book_review.user.email,
        #         'username': book_review.user.username,
        #     },
        #     'book': {
        #         'pk': book_review.book2.pk,
        #         'title': book_review.book2.title,
        #         'description': book_review.book2.description,
        #         'isbn': book_review.book2.isbn,
        #
        #     },
        # }
        # return JsonResponse(json_response)
class BookReviewAllAPIView(APIView):
    def get(self, request):
        book_review = BookReview.objects.all()
        serializer = BookReviewSerializer(book_review, many=True)
        return Response(data=serializer.data)


    def post(self, request):
        serializer = BookReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
