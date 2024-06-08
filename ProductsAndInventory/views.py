from django.shortcuts import render
from .models import Review, Product, Category
from .serializers import ReviewSerializer, ProductSerializer, CategorySerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound


class CategoryView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

    def get(self, request):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

    def get(self, request, category_id):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise NotFound(detail="Category not found")

        serializer = self.serializer_class(category)
        return Response({'message': 'Category retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        serializer = self.serializer_class(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating category', 'errors': serializer.errors}, status=400)

    def patch(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        serializer = self.serializer_class(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating category', 'errors': serializer.errors}, status=400)

    def delete(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        category.delete()
        return Response({'message': 'Category deleted successfully'}, status=204)
    

class ProductView(APIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response({'message': 'Products retrieved successfully', 'data': serializer.data})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully', 'data': serializer.data}, status=201)
        return Response({'message': 'Error creating product', 'errors': serializer.errors}, status=400)



class ProductDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get(self, request, products_id):
        product = Product.objects.get(pk=products_id)
        serializer = self.serializer_class(product)
        return Response({'message': 'Product retrieved successfully', 'data': serializer.data})

    def put(self, request, products_id):
        product = Product.objects.get(pk=products_id)
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating product', 'errors': serializer.errors}, status=400)

    def patch(self, request, products_id):
        product = Product.objects.get(pk=products_id)
        serializer = self.serializer_class(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating product', 'errors': serializer.errors}, status=400)

    def delete(self, request, products_id):
        product = Product.objects.get(pk=products_id)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=204)




class ReviewView(APIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        reviews = Review.objects.all()
        serializer = self.serializer_class(reviews, many=True)
        return Response({'message': 'Reviews retrieved successfully', 'data': serializer.data})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Review created successfully', 'data': serializer.data}, status=201)
        return Response({'message': 'Error creating review', 'errors': serializer.errors}, status=400)



class ReviewDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ReviewSerializer

    def get(self, request, review_id):
        
        try:
            review = Review.objects.get(pk=review_id)
        except Category.DoesNotExist:
            raise NotFound(detail="Review not found")
        
        serializer = self.serializer_class(review)
        return Response({'message': 'Review retrieved successfully', 'data': serializer.data})

    def put(self, request, review_id):
        review = Review.objects.get(pk=review_id)
        serializer = self.serializer_class(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Review updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating review', 'errors': serializer.errors}, status=400)

    def patch(self, request, review_id):
        review = Review.objects.get(pk=review_id)
        serializer = self.serializer_class(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Review updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating review', 'errors': serializer.errors}, status=400)

    def delete(self, request, review_id):
        review = Review.objects.get(pk=review_id)
        review.delete()
        return Response({'message': 'Review deleted successfully'}, status=204)




