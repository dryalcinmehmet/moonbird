from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import OsosDocument


class OsosDocumentSerializer(DocumentSerializer):
    class Meta:
        document = OsosDocument
        fields = '__all__'