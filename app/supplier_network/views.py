from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Counterparty
from .permissions import CounterpartyPermissions
from .serializers import CounterpartySerializer


class CounterpartyView(ModelViewSet):
    queryset = Counterparty.objects.all()
    serializer_class = CounterpartySerializer
    permission_classes = [IsAuthenticated, CounterpartyPermissions]


    def get_queryset(self):
        queryset = Counterparty.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = Counterparty.objects.prefetch_related('contacts').filter(
                contacts__type_contacts = 2, contacts__contact = country
            )
        return queryset
