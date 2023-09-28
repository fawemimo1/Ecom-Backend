from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryWithDetails(APIView):

    def get(self, request, category_id):
        try:
            # Retrieve the category object
            category = Category.objects.get(id=category_id)

            # Serialize the category data
            category_data = CategorySerializer(category).data

            # Retrieve and serialize the related types
            types = CategoryType.objects.filter(category=category)
            types_data = []

            for type in types:
                type_data = CategoryTypeDetailSerializer(type).data

                # Retrieve and serialize the related subcategories for each type
                subcategories = SubCategory.objects.filter(category_type=type)
                subcategories_data = []

                for subcategory in subcategories:
                    subcategory_data = SubCategoryDetailSerializer(subcategory).data

                    # Retrieve and serialize the related brands for each subcategory
                    brands = Brand.objects.filter(subcategory=subcategory)
                    brands_data = BrandDetailSerializer(brands, many=True).data

                    # Include brands data within the subcategory
                    subcategory_data["brands"] = brands_data

                    subcategories_data.append(subcategory_data)

                # Include subcategories data within the type
                type_data["subcategories"] = subcategories_data

                types_data.append(type_data)

            # Create a single object containing all the data
            result = {
                "category": category_data,
                "types": types_data,
            }

            return Response(result)

        except Category.DoesNotExist:
            return Response({"message": "Category not found"}, status=404)



class CategoryViewAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

class SubCategoryViewAPI(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return SubCategoryDetailSerializer
        return SubCategorySerializer

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        category_type = self.request.query_params.get('category_type')
        if category is not None:
            queryset = queryset.filter(category=category)

        if category_type is not None:
            queryset = queryset.filter(category_type=category_type)

        return queryset



class BrandViewAPI(viewsets.ModelViewSet):
    queryset = Brand.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BrandDetailSerializer
        return BrandSerializer

    def get_queryset(self):
        queryset = self.queryset
        subcategory = self.request.query_params.get('subcategory')

        if subcategory is not None:
            queryset = queryset.filter(subcategory=subcategory)
        return queryset


class TypeViewAPI(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    # serializer_class = TypeSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CategoryTypeDetailSerializer
        return TypeSerializer

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset