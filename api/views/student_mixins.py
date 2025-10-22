from ..serializers import StudentSerializer
from rest_framework import mixins, generics
from students.models import student



class Students(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class StudentDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

    def get (self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)