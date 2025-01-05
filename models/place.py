#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from models.review import Review
from models.amenity import Amenity
import os
import models


place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False
            ),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False
            )
        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(
            String(60),
            ForeignKey("cities.id"),
            nullable=False
            )

    user_id = Column(
            String(60),
            ForeignKey("users.id"),
            nullable=False
            )

    name = Column(
            String(128),
            nullable=False
            )

    description = Column(
            String(1024),
            nullable=True
            )

    number_rooms = Column(
            Integer,
            nullable=False,
            default=0
            )

    number_bathrooms = Column(
            Integer,
            nullable=False,
            default=0
            )

    max_guest = Column(
            Integer,
            nullable=False,
            default=0
            )

    price_by_night = Column(
            Integer,
            nullable=False,
            default=0
            )

    latitude = Column(
            Float,
            nullable=True
            )

    longitude = Column(
            Float,
            nullable=True
            )

    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
                "Review",
                backref="place",
                cascade="all, delete, delete-orphan"
                )

        amenities = relationship(
                "Amenity",
                secondary="place_amenity",
                viewonly=False,
                overlaps="place_amenities"
                )
    else:
        @property
        def reviews(self):
            """Getter for reviews"""
            reviews_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """Getter for amenities"""
            amenities_list = []
            for amenity in storage.all(Amenity).values():
                if place.amenity_ids == Amenity.id:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, value):
            """Setter for amenities"""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
