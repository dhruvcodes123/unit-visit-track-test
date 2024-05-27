from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .constants import INVALID_WORKER_PHONE_NUMBER, INVALID_PHONE_NUMBER, VISIT_CREATE_SUCCESS, \
    UNAUTHORIZED_USER, LIST_OF_UNITS_LINKED_TO_SPECIFIED_WORKER_SUCCESS
from .models import Worker, Unit, Visit
from .serializers import UnitSerializer, VisitSerializer


class UnitListCreateView(generics.ListAPIView):
    """
    get:
    Return a list of all units linked to the specified worker by phone number..
    """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def get(self, request, *args, **kwargs):
        """
        Return a customized response with a list of units linked to the specified worker.
        """
        phone_number = request.META.get('HTTP_PHONE_NUMBER')
        if not phone_number:
            return Response({
                'message': UNAUTHORIZED_USER,
            }, status=status.HTTP_401_UNAUTHORIZED)

        try:
            worker = Worker.objects.get(phone_number=phone_number)
        except Worker.DoesNotExist:
            raise ValidationError(INVALID_WORKER_PHONE_NUMBER)

        units = self.queryset.filter(worker=worker)
        serializer = self.get_serializer(units, many=True)
        return Response({
            'message': LIST_OF_UNITS_LINKED_TO_SPECIFIED_WORKER_SUCCESS,
            'data': serializer.data,
        }, status=status.HTTP_200_OK)


class VisitListCreateView(generics.CreateAPIView):
    """
        post:
        Create a new visit instance.

        Validates the worker's phone number is the same as the one linked to the specified unit
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def make_visit(self, serializer):
        """
            Save the new visit instance after ensuring that the worker's phone number is the same as the one linked to
            the specified unit

            Raises:
                ValidationError: If the worker's phone number does not match the unit's worker phone number.
        """
        worker_phone = self.request.META.get('HTTP_PHONE_NUMBER')
        unit_id = self.request.data.get('unit')
        unit = Unit.objects.get(pk=unit_id)

        if unit.worker.phone_number != worker_phone:
            raise ValidationError(INVALID_PHONE_NUMBER)

    def create(self, request, *args, **kwargs):
        """
        Create a new visit instance and return a visited time with visit id.
        """
        phone_number = request.META.get('HTTP_PHONE_NUMBER')

        if not phone_number:
            return Response({
                'message': UNAUTHORIZED_USER,
            }, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            self.make_visit(serializer)
            self.perform_create(serializer)

        except ValidationError as e:
            error_message = e.detail[0] if isinstance(e.detail, list) else str(e.detail)
            return Response({
                'message': error_message,
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'message': VISIT_CREATE_SUCCESS,
            'data': serializer.data,
        }, status=status.HTTP_201_CREATED)
