from django.core.management.base import BaseCommand
from django.utils import timezone
from listings.models import User, Listing, Booking, Review
from django.core.validators import MinValueValidator, MaxValueValidator

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        # optional to remove existing data
        User.objects.all().delete()
        Listing.objects.all().delete()  
        Booking.objects.all().delete()
        Review.objects.all().delete()

        # Create sample users
        host = User.objects.create_user(
            email="host@example.com"
            username="hostuser",
            first_name="Host",
            last_name="User",
            role="host",
            password="password123"
        )
        guest = User.objects.create_user(
            email="guest@example.com"
            username="guestuser",
            first_name="Guest", 
            last_name="User",
            role="guest",
            password="password123"
        )

        # Listings
        listing1 = Listing.objects.create(
            user=host,
            title="Cozy Cottage",
            description="A cozy cottage in the countryside.",
            price=100.00,
            location="Countryside"
        )
        listing2 = Listing.objects.create(
            user=host,
            title="Modern Apartment",
            description="A modern apartment in the city center.",
            price=150.00,
            location="City Center"
        )

        # Bookings
        booking1 = Booking.objects.create(
            listing=listing1,
            user=guest,
            status="confirmed",
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timezone.timedelta(days=3),
            total_price=300.00
        )
        booking2 = Booking.objects.create(
            listing=listing2,
            user=guest,
            status="pending",
            start_date=timezone.now().date() + timezone.timedelta(days=5),
            end_date=timezone.now().date() + timezone.timedelta(days=8),
            total_price=450.00
        )
        # Reviews
        review1 = Review.objects.create(
            listing=listing1,
            user=guest,
            rating=5,
            comment="Amazing stay! Highly recommend."
        )
        review2 = Review.objects.create(
            listing=listing2,
            user=guest,
            rating=4,
            comment="Great location, but a bit noisy."
        )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
