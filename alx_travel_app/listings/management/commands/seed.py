# listings/management/commands/seed.py
import uuid
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing, Booking, Review
from datetime import date, timedelta

User = get_user_model()

class Command(BaseCommand):
    help = "Seed database with sample users, listings, bookings, and reviews"

    def handle(self, *args, **kwargs):
        # Create users
        guest = User.objects.create_user(
            username="guestuser",
            email="guest@example.com",
            first_name="Guest",
            last_name="User",
            role="guest",
            password="guest123"
        )

        host = User.objects.create_user(
            username="hostuser",
            email="host@example.com",
            first_name="Host",
            last_name="User",
            role="host",
            password="host123"
        )

        admin = User.objects.create_superuser(
            username="adminuser",
            email="admin@example.com",
            first_name="Admin",
            last_name="User",
            role="admin",
            password="admin123"
        )
        
        # Create listings
        apt = Listing.objects.create(
            user=host,
            title="Cozy Apartment",
            description="2 bedroom flat in city center",
            price=75.00,
            location="Kaiserslautern"
        )
        villa = Listing.objects.create(
            user=host,
            title="Luxury Villa",
            description="Spacious villa with pool",
            price=250.00,
            location="Berlin"
        )

        # Create bookings
        Booking.objects.create(
            listing=apt,
            user=guest,
            status="confirmed",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=3),
            total_price=225.00
        )

        # Create reviews
        Review.objects.create(
            listing=apt,
            user=guest,
            rating=5,
            comment="Amazing stay, highly recommend!"
        )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
