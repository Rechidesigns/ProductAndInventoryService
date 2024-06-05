
from django.urls import path
from .views import CategoryView, CategoryDetailView, ProductView, ProductDetailView, ReviewView, ReviewDetailView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<str:uuid>/', CategoryDetailView.as_view()),
    path('products/', ProductView.as_view()),
    path('products/<str:uuid>/', ProductDetailView.as_view()),
    path('reviews/', ReviewView.as_view()),
    path('reviews/<str:uuid>/', ReviewDetailView.as_view()),
]





# from django.urls import path
# from .views import ReviewListCreateAPIView, ReviewDetailAPIView, CategoryListCreateAPIView, CategoryDetailAPIView, ProductListCreateAPIView, ProductDetailAPIView

# urlpatterns = [
#     path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
#     path('reviews/<uuid:review_id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
#     path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
#     path('categories/<uuid:category_id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
#     path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
#     path('products/<uuid:product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
# ]