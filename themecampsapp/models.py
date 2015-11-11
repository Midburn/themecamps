from django.db import models

# User - a real person with midburn profile.
class User(models.Model):
    email = models.CharField(unique=True)
    facebook = models.CharField()
    first_name_he = models.CharField()
    last_name_he = models.CharField()
    first_name_en = models.CharField()
    last_name_en = models.CharField()
    phone = models.Charfield()


CAMPSTATUS = (
    (-1,'deleted'),
    (1,'open'),
    (2,'closed'),
    (3,'inactive'),
)
# Create your models here.
class Camp(models.Model):
    camp_name_he = models.CharField(max_length=50, unique=True)
    camp_name_en = models.CharField(max_length=50, unique=True)
    camp_desc_he = models.TextField()
    camp_desc_en = models.TextField()
    main_contact = models.ForeigKey(User)
    moop_contact = models.ForeignKey(User)
    safety_contact = models.ForeignKey(User)
    camp_status = models.IntegerField(choices=CAMPSTATUS)
    is_published = models.BooleanField()

CAMPTYPES = (
    (1,'food'),
    (2,'drinking/bar'),
    (3,'music'),
    (4,'workshops'),
    (5,'art-supporting'),
    (6,'other'),
)
CAMPTIMES = (
    (1,'morning'),
    (2,'noon'),
    (3,'evening'),
    (4,'night'),
)
NOISE_LEVELS = (
    (1,'quiet'),
    (2,'medium')
    (3,'noisy'),
    (4,'very noisy')
)

class CampLocation(models.Model): # Can be part of camp, but for better modularity
    camp=models.OneToOneField(Camp)
    camp_type=models.IntegerField(choices=CAMPTYPES)
    camp_type_other=models.Textfield()
    camp_activity_time=models.CommaSeparatedIntegerField(choices=CAMPTIMES)
    child_friendly=models.BooleanField()
    noise_level=models.IntegerField(choises=NOISE_LEVELS)
    public_activity_area_sqm=models.IntegerField()
    public_activity_area_desc=models.TextField()
    support_art=models.BooleanField()
    location_comments=models.TextField()
    # These 3 will be set by mikumation
    camp_location_street=models.Charfield()
    camp_location_street_time=models.Charfield()
    camp_location_area=models.IntegerField()
    # Arrival
    arriving_at=models.DateTimeField()
    # Arrival Checklist
    has_construction_team=models.BooleanField()
    has_deconst_team=models.BooleanField()
    has_gifting=models.BooleanField()
    has_leds=models.BooleanField()

CAMP_MEMBERSHIP_STATUS = (
    (1,'not a member'),
    (2,'awaiting approval'),
    (3,'approved'),
)
class CampMember(Models.Model):
    camp=models.ForeignKey(Camp)
    user=models.ForeignKey(User)
    status=models.IntegerField(choices=CAMP_MEMBERSHIP_STATUS)
    has_ticket=models.BooleanField()
    early_arrival=models.BooleanField()

class CampEditor(Models.Model):
    camp=models.ForeignKey(Camp)
    user=models.ForeignKey(User)

class CampSafety(Models.Model):
    camp=models.OneToOneField(Camp)
    have_art=models.BooleanField()
    installation_over_2m=models.BooleanField()
    # Safety checklist:
    is_gas_2m_from_stove=models.BooleanField()
    is_electricity_not_near_water=models.BooleanField()

class CampLocationNeighbours(models.Model):
    requesting_camp=ForeignKey(Camp)
    requested_camp=ForeignKey(Camp)

ACTIVITY_TYPES = (
    (1, 'workshop'),
    (2, 'party'),
    (3, 'lecture'),
    (4, 'show'),
    (5, 'parade/hike'),
    (6, 'game'),
    (7, 'movie'),
    (8, 'other'),
)

class Workshop(models.Model):
    owner=models.ForeignKey(Camp)
    activity_name_he=models.CharField(max_length=50)
    activity_name_en=models.CharField(max_length=50)
    activity_desc_he=models.TextField()
    activity_desc_en=models.TextField()
    activity_datetime=models.DatetimeField()
    activity_type=models.IntegerField(choises=ACTIVITY_TYPES)
    activity_type_other=models.TextField()
    adult_only=models.BooleanField()
    child_friendly=models.BooleanField()

