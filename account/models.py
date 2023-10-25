from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    pass

    class Meta:
        db_table = "account_user"


class House(TimeStamp):
    id = models.AutoField(primary_key=True)


class Ownership(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "User",
        db_column="user_id",
        on_delete=models.CASCADE,
        related_name="ownership_set",
    )
    house = models.ForeignKey(
        "House",
        db_column="house_id",
        on_delete=models.CASCADE,
        related_name="ownership_set",
    )
    created_at = models.DateTimeField(auto_now_add=True)


class OwnershipRequest(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "User",
        db_column="user_id",
        on_delete=models.SET_NULL,
        related_name="ownership_request_set",
        null=True,
        blank=True,
    )
    house = models.ForeignKey(
        "House",
        db_column="house_id",
        on_delete=models.SET_NULL,
        related_name="ownership_request_set",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "account_ownership_request"


# soft delete model
class Authority(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "User",
        db_column="user_id",
        on_delete=models.SET_NULL,
        related_name="authority_set",
        null=True,
        blank=True,
    )
    house = models.ForeignKey(
        "House",
        db_column="house_id",
        on_delete=models.SET_NULL,
        related_name="authority_set",
        null=True,
        blank=True,
    )
    allowed_at = models.DateTimeField(null=True, blank=True)
    disabled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class AuthorityRequest(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "User",
        db_column="user_id",
        on_delete=models.SET_NULL,
        related_name="authority_request_set",
        null=True,
        blank=True,
    )
    house = models.ForeignKey(
        "House",
        db_column="house_id",
        on_delete=models.SET_NULL,
        related_name="authority_request_set",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = "account_authority_request"


# soft delete model
class Record(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        "User",
        db_column="user_id",
        on_delete=models.SET_NULL,
        related_name="record_set",
        null=True,
        blank=True,
    )
    house = models.ForeignKey(
        "House",
        db_column="house_id",
        on_delete=models.SET_NULL,
        related_name="recoard_set",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
