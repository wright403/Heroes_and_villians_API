from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
      supers = Super.objects.all()
      serializer = SuperSerializer(supers, many =True) 
      return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def supers_detail(request, pk):
    try:
        supers = Super.objects.get(pk=pk)
        serializer = SuperSerializer(supers)
        return Response(serializer.data)
    except Super.DoesNotExist:    
        return Response(status=status.HTTP_404_NOT_FOUND)        
