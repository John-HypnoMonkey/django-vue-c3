from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .serializers import PostSnapshotSerializer
from . import parser_script


class viewChartAPI(views.APIView):
    def get(self, request, post_id=0):
        data = parser_script.parseVK(post_id)
        results = PostSnapshotSerializer(data).data
        return Response(results)


def viewMainPage(request):
    context = {}
    return render(request, "chart/base.html", context)
