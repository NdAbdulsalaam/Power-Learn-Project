from rest_framework.permissions import AllowAny
from django_elasticsearch_dsl_drf.constants import (
    SUGGESTER_COMPLETION,
    FUNCTIONAL_SUGGESTER_COMPLETION_PREFIX,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    CompoundSearchFilterBackend,
    SuggesterFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from apps.search.documents import MovieDocument
from apps.search.serializers.movie import MovieDocumentSerializer


class MovieDocumentView(DocumentViewSet):
    document = MovieDocument
    serializer_class = MovieDocumentSerializer
    lookup_field = "id"
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
        SuggesterFilterBackend,
    ]

    # Suggester fields
    suggester_fields = {
        "title_suggest": {
            "field": "title.suggest",
            "suggesters": [
                SUGGESTER_COMPLETION,
            ],
            "options": {
                "size": 10,  # Override default number of suggestions
                "skip_duplicates": True,  # Whether duplicate suggestions should be filtered out.
            },
        },
    }

    # Define search fields
    search_fields = (
        "title",
        "description",
        "director",
        "genres",
    )

    # Define filtering fields
    filter_fields = {
        "id": None,
        "title": "title.raw",
        "year": "year.raw",
        "rating_average": "rating_average.raw",
        "genres": "genres.raw",
        "imdb_rating": "imdb_rating.raw",
    }

    # Define ordering fields
    ordering_fields = {
        "id": None,
        "rating_average": None,
        "imdb_rating": None,
        "view_count": None,
        "year": None,
    }

    # Specify default ordering
    ordering = (
        "id",
        "view_count",
    )
