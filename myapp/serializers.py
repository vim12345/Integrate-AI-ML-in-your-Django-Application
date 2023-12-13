from rest_framework import serializers

class ProductDescriptionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)

class ImageRecognitionSerializer(serializers.Serializer):
    image = serializers.ImageField()
    # Add more fields if needed
    additional_field1 = serializers.CharField(max_length=100, required=False)
    additional_field2 = serializers.IntegerField(required=False)

    def validate_additional_field1(self, value):
        # Add custom validation logic for additional_field1 if needed
        # Custom validation logic for additional_field1
        if value and not value.isalpha():
            raise serializers.ValidationError("additional_field1 must contain only letters.")

        return value

    def validate_additional_field2(self, value):
        # Add custom validation logic for additional_field2 if needed
        # Custom validation logic for additional_field2
        if value is not None and (value < 0 or value > 100):
            raise serializers.ValidationError("additional_field2 must be between 0 and 100.")
        return value
