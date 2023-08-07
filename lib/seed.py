#!/usr/bin/env python3

# Script goes here!
import random
from faker import Faker
from random import random as rc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

company_name = [
    "Amazon",
    "Apple",
    "Google",
    "PlayStation",
    "Microsoft",
    "Meta",
    "TikTok",
    "Netflix",
    "FlatIron",
    "Spotify",
]

item = [
    "t-shirt",
    "backpack",
    "lanyard",
    "laptop case",
    "sticker",
    "pen",
    "cup",
    "bumper sticker",
    "headphones",
    "phone case",
]


def delete_records():
    session.query(Company).delete()
    session.query(Dev).delete()
    session.query(Freebie).delete()
    session.commit()


def create_companies():
    companies = []
    for i in range(10):
        company = Company(name=random.choice(company_name), founding_year=fake.year())
        session.add(company)
        session.commit()
        companies.append(company)
    return companies


def create_devs():
    devs = []
    for i in range(50):
        dev = Dev(name=fake.name())
        session.add(dev)
        session.commit()
        devs.append(dev)
    return devs


def create_freebies():
    freebies = []
    for i in range(100):
        freebie = Freebie(item_name=random.choice(item), value=random.randint(1, 60))
        session.add(freebie)
        session.commit()
        freebies.append(freebie)
    return freebies


def relate_one_to_many(companies, devs, freebies):
    for freebie in freebies:
        freebie.dev = random.choice(devs)
        freebie.company = random.choice(companies)

    session.add_all(freebies)
    session.commit()
    return companies, devs, freebies


if __name__ == "__main__":
    delete_records()
    companies = create_companies()
    devs = create_devs()
    freebies = create_freebies()
    companies, devs, freebies = relate_one_to_many(companies, devs, freebies)
