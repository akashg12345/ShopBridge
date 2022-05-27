from rest_framework import serializers
from .models import Items

class ItemsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Items
        fields = '__all__'
    ##-----------------  validations -------------------
    def create(self,validated_data):
        item = Items.objects.create(**validated_data)
        return item
    ## if request is put or patch than will follow this validation
    def update(self, instance, validated_data): 
        instance.category = validated_data.get('category',instance.category)
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)  
        instance.discount = validated_data.get('discount', instance.discount)
        instance.status = validated_data.get ('status',instance.status)
        instance.description = validated_data.get('description',instance.description)
        instance.save()
        return instance

    # Field level validator if items having quantity less than minimum required quantity
    def validate_quantity(self,value):
        if value <= 10 :
            return value
        raise serializers.ValidationError("Quantity should be more than 25")

