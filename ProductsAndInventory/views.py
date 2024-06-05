from django.shortcuts import render
from .models import Review, Product, Category
from .serializers import ReviewSerializer, ProductSerializer, CategorySerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'message': 'Categories retrieved successfully', 'data': serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category created successfully', 'data': serializer.data}, status=201)
        return Response({'message': 'Error creating category', 'errors': serializer.errors}, status=400)

class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response({'message': 'Category retrieved successfully', 'data': serializer.data})

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating category', 'errors': serializer.errors}, status=400)

    def patch(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating category', 'errors': serializer.errors}, status=400)

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response({'message': 'Category deleted successfully'}, status=204)
    
    

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'message': 'Products retrieved successfully', 'data': serializer.data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully', 'data': serializer.data}, status=201)
        return Response({'message': 'Error creating product', 'errors': serializer.errors}, status=400)

class ProductDetailView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response({'message': 'Product retrieved successfully', 'data': serializer.data})

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating product', 'errors': serializer.errors}, status=400)

    def patch(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating product', 'errors': serializer.errors}, status=400)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=204)





class ReviewView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response({'message': 'Reviews retrieved successfully', 'data': serializer.data})

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Review created successfully', 'data': serializer.data}, status=201)
        return Response({'message': 'Error creating review', 'errors': serializer.errors}, status=400)

class ReviewDetailView(APIView):
    def get(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response({'message': 'Review retrieved successfully', 'data': serializer.data})

    def put(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Review updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating review', 'errors': serializer.errors}, status=400)

    def patch(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Review updated successfully', 'data': serializer.data})
        return Response({'message': 'Error updating review', 'errors': serializer.errors}, status=400)

    def delete(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response({'message': 'Review deleted successfully'}, status=204)




















# class CategoryListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     permission_classes = [permissions.AllowAny]


# class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     permission_classes = [permissions.AllowAny]

    
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     permission_classes = [permissions.AllowAny]


#     # def perform_create(self, serializer):
#     #     user = self.request.user.id
#     #     serializer.save(user=user)

# class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     permission_classes = [permissions.AllowAny]

        
        
        
# class ReviewListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     #permission_classes = [permissions.IsAuthenticated]
#     permission_classes = [permissions.AllowAny]


#     # def perform_create(self, serializer):
#     #     user = self.request.user.id
#     #     serializer.save(user=user)

# class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     #permission_classes = [permissions.IsAuthenticated]
#     permission_classes = [permissions.AllowAny]
