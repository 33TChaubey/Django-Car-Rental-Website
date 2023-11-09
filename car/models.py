from django.db import models
from django.urls import reverse
from django.conf import settings
import datetime


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    test = models.TextField(null=True, blank=True)
    time = models.DateTimeField(default=datetime.datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Features(models.Model):
    airconditions = models.BooleanField(default=False)
    child_seat = models.BooleanField(default=False)
    gps = models.BooleanField(default=False)
    luggage = models.BooleanField(default=False)
    music = models.BooleanField(default=False)
    seat_belt = models.BooleanField(default=False)
    sleeping_bed = models.BooleanField(default=False)
    water = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=False)
    onboard_computer = models.BooleanField(default=False)
    audio_input = models.BooleanField(default=False)
    long_term_trips = models.BooleanField(default=False)
    car_Kit = models.BooleanField(default=False)
    remote_central_locking = models.BooleanField(default=False)
    climate_control = models.BooleanField(default=False)
    car = models.OneToOneField(
        'Car', related_name='features', on_delete=models.CASCADE, null=True, blank=True)


class Car(models.Model):
    class FuelType(models.TextChoices):
        PETROL = 'P', 'Petrol'
        DIESEL = 'D', 'Diesel'

    class Location(models.TextChoices):
        MUMBAI = 'M', 'Mumbai'
        DELHI = 'D', 'Delhi'
        BANGALORE = 'B', 'Bangalore'
        HYDERABAD = 'H', 'Hyderabad'
        AHMEDABAD = 'A', 'Ahmedabad'
        CHENNAI = 'C', 'Chennai'
        KOLKATA = 'K', 'Kolkata'
        SURAT = 'S', 'Surat'
        VADODARA = 'V', 'Vadodara'
        PUNE = 'P', 'Pune'
        JAIPUR = 'J', 'Jaipur'
        LUCKNOW = 'L', 'Lucknow'

    class TransmissionType(models.TextChoices):
        MANUAL = 'M', 'Manual'
        AUTOMATIC = 'A', 'Automatic'

    car_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name="cars")
    num_of_seats = models.IntegerField()
    num_of_air_bag = models.PositiveSmallIntegerField(default=0)
    fuel_type = models.CharField(
        max_length=1, choices=FuelType.choices, default=FuelType.PETROL)
    mileage = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to="car-image/%Y/%m/%d", null=True, blank=True)
    transmission = models.CharField(
        max_length=1, choices=TransmissionType.choices, default=TransmissionType.MANUAL)
    location = models.CharField(
        max_length=1, choices=Location.choices, default=Location.MUMBAI)
    const_per_hour = models.PositiveIntegerField()
    cost_par_day = models.PositiveIntegerField()
    cost_of_leasing = models.PositiveIntegerField()
    description = models.TextField()
    is_avaliable = models.BooleanField(default=False)
    like = models.IntegerField(default=0)
    comment = models.ManyToManyField(Review, null=True, blank=True)

    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return reverse('cars-details', args=[self.id])


class PrivateMsg(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

class Order(models.Model):

    order_status = (
        ("Pending" , "Pending"),
        ("Approved" , "Approved"),
        ("Declined" , "Decliend"),
    )

    car = models.ForeignKey(Car , related_name="orders" , on_delete=models.CASCADE)
    status = models.CharField(choices=order_status , max_length=10 , default="Pending"  , blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    cell_no = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateTimeField()
    to = models.DateTimeField()

    def __str__(self):
        return f"{self.car.car_name} - {self.user.username} "

    def get_absolute_url(self):
        return "/detail/%s/" % (self.id)