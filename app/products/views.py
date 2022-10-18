from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cars
from .serializers import CarsDetailSerializer


class CarsListView(APIView):
        """Представление для детальной информации по автомобилям"""
        def get(self, request):
            queryset = Cars.objects.all()
            serializer = CarsDetailSerializer(
                instance=queryset,
                many=True
            )
            return Response(serializer.data)