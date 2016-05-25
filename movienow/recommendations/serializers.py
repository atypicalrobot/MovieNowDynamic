from rest_framework import serializers

from movienow.recommendations.models import Recommendation

# Serializers define the API representation.
class RecommendationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('movie_id', 'rating', 'created_by')
