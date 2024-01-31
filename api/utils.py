from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def get_object(model, pk):
    try:
        return model.objects.get(id=pk)
    except model.DoesNotExist:
        return None

def list_objects(request, model, serializer):
    objects = model.objects.all()
    serialized_data = serializer(objects, many=True).data
    return Response(serialized_data)

def detail_object(request, model, serializer, pk):
    obj = get_object(model, pk)
    if obj:
        serialized_data = serializer(obj).data
        return Response(serialized_data)
    else:
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

def create_object(request, model, serializer):
    serialized_data = serializer(data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
    return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

def update_object(request, model, serializer, pk):
    obj = get_object(model, pk)
    if obj:
        serialized_data = serializer(instance=obj, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

def delete_object(request, model, pk):
    obj = get_object(model, pk)
    if obj:
        obj.delete()
        return Response("Deletion Successful")
    else:
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
