from django.shortcuts import render
from django.http import HttpResponse
from .serializers import StudentModelSerializer,StandardSerializer
from rest_framework.views import APIView 
from .models import Student,Standard
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.core.paginator import Paginator
from django.core.serializers import serialize
# Create your views here.
from rest_framework.decorators import api_view, renderer_classes
# from django.http import HttpResponse

class StudetnModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer



import json
@api_view(['GET'])
def home(request):
    students=Student.objects.all().order_by('id')
    items_per_page = int(request.GET.get('rows', 10))
    paginator=Paginator(students,items_per_page)

    # if requested is not then 1
    page = request.GET.get('page', 1)

    try:
        # for requested page
        paginated_items=paginator.page(page)

    except:       
        # for last page 
        paginated_items = paginator.page(paginator.num_pages)
    
    context={
     'paginated_items':paginated_items,
     'items_per_page':items_per_page,
    #  'data':students,
     'has_next':paginated_items.has_next(),
    }
    return Response({"data":context},status=status.HTTP_200_OK)
    # return render(request, 'home.html', context)

class StudentModelAPI(APIView):
    def get(self, request):
        student_id = request.query_params.get('id')
        if student_id is None:
            student_queryset = Student.objects.all().order_by('id')

            serialized_data = StudentModelSerializer(student_queryset, many=True).data
            return Response({'students': serialized_data}, status=status.HTTP_200_OK)
        else:
            try:
                student=Student.objects.get(id=student_id)
                serialized_data=StudentModelSerializer(student).data
                return Response({"data": serialized_data}, status=status.HTTP_200_OK)
            except:
                return Response({"error":"Student Not Found."},status=status.HTTP_404_NOT_FOUND)
    
    def post(self,request):
        try:
            req_body=request.data
            serialized_data=StudentModelSerializer(data=req_body)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response({"data":serialized_data.data},status=status.HTTP_201_CREATED)
            else:
                return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        student_id=request.query_params.get('id')
        if student_id is not None:
            try:
                student=Student.objects.get(id=student_id)
                student.delete()
                return Response({"data":"Student is deleted Successfully"},status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error":"Studnet Not FOund"},status=status.HTTP_404_NOT_FOUND)


class StandardList(APIView):
    def get(self, request):
        try:
            standards = Standard.objects.all()
            serialized_data = StandardSerializer(standards, many=True).data
            # return Response(serializer.data)
            return Response({'standard': serialized_data}, status=status.HTTP_200_OK)
        except:
            return Response({"error":"Student Not Found."},status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = StandardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaginationAPI(APIView):
    def get(self,request):
        students=Student.objects.all()
        
        search_name=request.GET.get('search')
        if search_name:
            students=students.filter(name__icontains=search_name)
        items_per_page = int(request.GET.get('rows', 10))
        paginator=Paginator(students,items_per_page)

        # if requested is not then 1
        print(items_per_page)
        page = request.GET.get('page', 1)
        print(page)
        try:
            # for requested page
            paginated_items=paginator.page(page)

        except:        
            # for last page 
            paginated_items = paginator.page(paginator.num_pages)
        print(paginated_items)
        
        
        # if search_name:
        #     iData=[StudentModelSerializer(item).data for  item in paginated_items]
        #     # iData=iData.filter(name__icontains=search_name)
        
        # else:
        items_data = [{'name': item.name, 'rollno': item.rollno, 'standard': item.standard,'course': item.course } for item in paginated_items]
        iData=[StudentModelSerializer(item).data for  item in paginated_items]

        # print(items_data,iData)
        serialized_data = StudentModelSerializer(students, many=True).data

        data={'data':iData,'has_next': paginated_items.has_next()}

        return Response(data,status=status.HTTP_200_OK)