from rest_framework.generics import RetrieveUpdateAPIView

from ..serializers.profiles import MeProfileSerializer

class PrivateMeProfileView(RetrieveUpdateAPIView):
    serializer_class = MeProfileSerializer

    def get_object(self):
        return self.request.user