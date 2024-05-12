from core.models import Orders, OrderLine
from rest_framework import generics
from ..serializers import OrderSerializer, OrderLineSerializer
from core.views import BaseAdminAPIView


# Orders
class OrderCreate(BaseAdminAPIView, generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderListCreate(BaseAdminAPIView, generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroy(BaseAdminAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_id'

class OrderRetrieve(BaseAdminAPIView, generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_id'

class OrderList(BaseAdminAPIView, generics.ListAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        queryset = Orders.objects.all()

        # Filter by user
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)

        # Sort by order attribute
        sort_by = self.request.query_params.get('sort_by', None)
        if sort_by is not None:
            descending = sort_by.startswith('-')
            field = sort_by.lstrip('-')
            queryset = queryset.order_by(f'{"-" if descending else ""}{field}')

        return queryset

# Order Line
class OrderLineCreate(BaseAdminAPIView, generics.CreateAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    
class OrderLineListCreate(BaseAdminAPIView, generics.ListCreateAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer

class OrderLineRetrieveUpdateDestroy(BaseAdminAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    lookup_field = 'order_line_id'

class OrderLineRetrieve(BaseAdminAPIView, generics.RetrieveAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    lookup_field = 'order_line_id'

class OrderLineList(BaseAdminAPIView, generics.ListAPIView):
    serializer_class = OrderLineSerializer

    def get_queryset(self):
        queryset = OrderLine.objects.all()

        # Filter by order
        order = self.request.query_params.get('order', None)
        if order is not None:
            queryset = queryset.filter(order=order)

        # Sort by order line attribute
        sort_by = self.request.query_params.get('sort_by', None)
        if sort_by is not None:
            descending = sort_by.startswith('-')
            field = sort_by.lstrip('-')
            queryset = queryset.order_by(f'{"-" if descending else ""}{field}')

        return queryset