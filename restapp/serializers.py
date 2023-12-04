from.models import Student
from rest_framework import serializers

class Studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    email=serializers.EmailField()
    age=serializers.IntegerField()
    

    def create(self,validated_data):
        return Student.objects.create(validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.age=validated_data.get('age',instance.age)
        instance.save()
        return instance

# class Studentserializer(serializers.Serializer):
#     class Meta:
#         model=Student
#         fields='__all__'