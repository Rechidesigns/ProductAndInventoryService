from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Review, Product, Category
from .serializers import ReviewSerializer, ProductSerializer, CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Extract the user ID from the JWT token
        userid = self.request.user.id
        serializer.save(userid=userid)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure user is authenticated

    def perform_create(self, serializer):
        # Access the user ID from the JWT token
        userid = self.request.user.id
        serializer.save(userid=userid)