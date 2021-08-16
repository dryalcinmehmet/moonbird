from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    SUGGESTER_COMPLETION,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    SearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet, Search
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import parsers, renderers, status
from rest_framework.response import Response
from .documents import OsosDocument
from .serializers import OsosDocumentSerializer
from .data import msgWithNamedFields
from .models import Osos

class OsosInsertData(APIView):
    queryset = Osos.objects.all()
    model = Osos
    serializer_class = OsosDocumentSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        data = msgWithNamedFields
        if type(data) == dict:
            self.model.objects.create(**data)
        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'message': 'Password updated successfully',
            'data': []
        }

        return Response(response)

class OsosViewSet(DocumentViewSet):
    document = OsosDocument
    serializer_class = OsosDocumentSerializer
    lookup_field = 'deviceId'

    filter_backends = [
        DefaultOrderingFilterBackend,
        FilteringFilterBackend,
        SearchFilterBackend,
        SuggesterFilterBackend,
    ]

    search_fields = '__all__'

    filter_fields = {
        'id': {
            'field': 'deviceId',
            'lookups': [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ],
        },
    }

    suggester_fields = {
        'deviceId_suggest': {
            'field': 'deviceId.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }
