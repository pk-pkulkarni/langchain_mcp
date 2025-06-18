from typing import Dict, List, Tuple
from datetime import datetime, time

# Restaurant Information
RESTAURANT_INFO = {
    "name": "Spice Garden - Authentic Indian Cuisine",
    "address": "123 Main Street, Connaught Place, New Delhi, India - 110001",
    "phone": "+91-11-2345-6789",
    "email": "info@spicegarden.com",
    "website": "www.spicegarden.com",
    "cuisine": "Indian",
    "rating": 4.5,
    "price_range": "₹₹₹"
}

# Operating Hours
OPERATING_HOURS = {
    "monday": {"open": "11:00", "close": "23:00"},
    "tuesday": {"open": "11:00", "close": "23:00"},
    "wednesday": {"open": "11:00", "close": "23:00"},
    "thursday": {"open": "11:00", "close": "23:00"},
    "friday": {"open": "11:00", "close": "23:30"},
    "saturday": {"open": "11:00", "close": "23:30"},
    "sunday": {"open": "12:00", "close": "22:00"}
}

# Menu Categories and Items
MENU = {
    "appetizers": [
        {"name": "Samosa", "description": "Crispy pastry filled with spiced potatoes and peas", "price": 120,
         "vegetarian": True},
        {"name": "Paneer Tikka", "description": "Grilled cottage cheese with Indian spices", "price": 180,
         "vegetarian": True},
        {"name": "Chicken 65", "description": "Spicy deep-fried chicken with curry leaves", "price": 220,
         "vegetarian": False},
        {"name": "Veg Spring Roll", "description": "Crispy rolls with mixed vegetables", "price": 140,
         "vegetarian": True},
        {"name": "Fish Pakora", "description": "Spiced fish fritters", "price": 200, "vegetarian": False}
    ],
    "soups": [
        {"name": "Tomato Soup", "description": "Classic tomato soup with Indian spices", "price": 100,
         "vegetarian": True},
        {"name": "Chicken Soup", "description": "Hearty chicken soup with herbs", "price": 150, "vegetarian": False},
        {"name": "Mulligatawny Soup", "description": "Traditional Indian lentil soup", "price": 120, "vegetarian": True}
    ],
    "main_course": [
        {"name": "Butter Chicken", "description": "Creamy tomato-based curry with tender chicken", "price": 350,
         "vegetarian": False},
        {"name": "Paneer Butter Masala", "description": "Cottage cheese in rich tomato gravy", "price": 280,
         "vegetarian": True},
        {"name": "Chicken Biryani", "description": "Aromatic rice with tender chicken and spices", "price": 320,
         "vegetarian": False},
        {"name": "Veg Biryani", "description": "Fragrant rice with mixed vegetables", "price": 250, "vegetarian": True},
        {"name": "Dal Makhani", "description": "Creamy black lentils slow-cooked overnight", "price": 180,
         "vegetarian": True},
        {"name": "Fish Curry", "description": "Fresh fish in tangy coconut curry", "price": 380, "vegetarian": False},
        {"name": "Palak Paneer", "description": "Spinach curry with cottage cheese", "price": 220, "vegetarian": True},
        {"name": "Chicken Tikka Masala", "description": "Grilled chicken in spiced tomato sauce", "price": 340,
         "vegetarian": False}
    ],
    "breads": [
        {"name": "Naan", "description": "Soft leavened bread", "price": 30, "vegetarian": True},
        {"name": "Butter Naan", "description": "Naan brushed with butter", "price": 40, "vegetarian": True},
        {"name": "Roti", "description": "Whole wheat flatbread", "price": 25, "vegetarian": True},
        {"name": "Paratha", "description": "Layered flatbread", "price": 35, "vegetarian": True}
    ],
    "desserts": [
        {"name": "Gulab Jamun", "description": "Sweet milk dumplings in sugar syrup", "price": 80, "vegetarian": True},
        {"name": "Rasmalai", "description": "Soft cottage cheese patties in sweet milk", "price": 90,
         "vegetarian": True},
        {"name": "Kheer", "description": "Rice pudding with nuts and saffron", "price": 70, "vegetarian": True}
    ],
    "beverages": [
        {"name": "Masala Chai", "description": "Spiced Indian tea", "price": 40, "vegetarian": True},
        {"name": "Lassi", "description": "Sweet yogurt drink", "price": 60, "vegetarian": True},
        {"name": "Mango Lassi", "description": "Mango-flavored yogurt drink", "price": 70, "vegetarian": True},
        {"name": "Coca Cola", "description": "Soft drink", "price": 50, "vegetarian": True}
    ]
}

# Table Information
TABLES = {
    1: {"capacity": 2, "location": "Window", "status": "available"},
    2: {"capacity": 2, "location": "Window", "status": "available"},
    3: {"capacity": 4, "location": "Center", "status": "available"},
    4: {"capacity": 4, "location": "Center", "status": "available"},
    5: {"capacity": 6, "location": "Garden", "status": "available"},
    6: {"capacity": 6, "location": "Garden", "status": "available"},
    7: {"capacity": 8, "location": "Private", "status": "available"},
    8: {"capacity": 8, "location": "Private", "status": "available"}
}

# Booking System
BOOKINGS = {}
