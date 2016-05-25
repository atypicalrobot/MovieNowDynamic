from rest_framework import viewsets

from movienow.recommendations.models import Recommendation
from movienow.recommendations.serializers import RecommendationSerializer


# ViewSets define the view behavior.
class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
