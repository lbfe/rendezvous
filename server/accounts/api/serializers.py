from rest_framework.serializers import ModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from django.db import models
Volunteer = get_user_model()

class VolunteerSerializer(ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        volunteer = Volunteer(
            email=validated_data['email'],
            hearts=0,
            badges=0
        )
        volunteer.set_password(validated_data['password'])
        volunteer.save()
        return volunteer

class VolunteerLoginSerializer(ModelSerializer):
    token = models.CharField(blank=True)
    class Meta:
        model = Volunteer
        fields = ['email', 'password', 'token',]
        extra_kwargs = {"password": {"write_only": True}}

class VolunteerProfileSerializer(ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'phone', 'hearts', 'badges']
        extra_kwargs = {'password': {'write_only': True}, 'hearts': {'read_only': True}, 'badges': {'read_only': True}}
# class VolunteerDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Volunteer.objects.all()
#     serializer_class = VolunteerSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self, *args, **kwargs):
#         queryset_list = Activity.objects.all().filter(user = self.request.user)
#         return queryset_list