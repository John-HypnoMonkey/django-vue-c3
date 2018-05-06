from django.shortcuts import render

from .models import PostSnapshot
from rest_framework import views
from rest_framework.response import Response

from .serializers import PostSnapshotSerializer


class viewChartAPI(views.APIView):
    def get(self, request):
        dummy_data = PostSnapshot(0, 1, 2, 3)
        results = PostSnapshotSerializer(dummy_data).data
        return Response(results)


def viewChart(request):
    context = {}
    return render(request, "chart/base.html", context)
