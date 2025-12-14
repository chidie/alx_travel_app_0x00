from rest_framework import serializers
from .models import User, Listing, Booking, Review

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = User
        fields = ("user_id", "email", "first_name", "last_name", "role", "created_at", "password")
        read_only_fields = ("user_id", "created_at")

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = self.Meta.model(**validated_data)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ("listing_id", "user", "title", "description", "price", "location", "created_at")
        read_only_fields = ("listing_id", "created_at")

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("booking_id", "listing", "user", "status", "start_date", "end_date", "total_price", "created_at")
        read_only_fields = ("booking_id", "created_at")

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("review_id", "listing", "user", "rating", "comment")
        read_only_fields = ("review_id",)