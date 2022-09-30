from cgitb import html
from django.http import HttpResponse
from django.shortcuts import render
from dataclasses import dataclass
from typing import Dict, List
from shutil import ReadError
@dataclass
class Flower:
    name: str
    description: str

def flower_view(request,):
    pear = {
        "flowers": ["Hydrangea", "Lilly of the valley", "Forget-Me-Nots", "Morning Glory"],
    }
    return render(request, "flower.html", pear)

def flower_info(request,input):
    mango = {
        "orange": input,
        "Hydrangea": Flower(
            "The Hydrangea",
            ""
        ),
        "Daffodill": Flower(
            "The Daffodil",
            "The BCCA Documentation Team is responsible for taking pictures and running the program's social media"
        ),
        "Forget-Me-Nots": Flower(
            "The Forget-Me-Not",
            "The BCCA Management Team is responsible for coordinating with other students and staff to get things needed or planned to keep the program running."
        ),
        "Procurement": Flower(
            "The Morning Glory",
            "The BCCA Procurement Team is responsible for planning, buying, cooking, and serving lunch to the other students."
        ),
    }
    return render(request, "stuff.html", mango)