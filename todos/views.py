from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET', 'POST'])
def todo_list(request):
    """
    List all todos, or create new snippet.
    """
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    """
    Retrieve, update or delete a todos.
    """
    try:
        todo = Todo.objects.get(pk=pk) # 특정 snippet 가져오기
    except Todo.DoesNotExist: # 일치하는 snippet이 없을 경우
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

