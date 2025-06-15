import os
import django
import json
from datetime import datetime
from decimal import Decimal
from bson import Decimal128

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bmw_shop.settings')
django.setup()

from pymongo import MongoClient
from app.models import CarRecord, Order, BMWSeries, Item, OrderItem

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client['bmw_shop']

def decimal_to_str(obj):
    """Convert Decimal objects to string for JSON serialization"""
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def datetime_to_str(dt):
    """Convert datetime objects to ISO format string"""
    return dt.isoformat() if dt else None

def sync_series():
    """Sync BMW Series data to MongoDB"""
    series_collection = db['bmw_series']
    series_collection.delete_many({})  # Clear existing data
    
    series_list = []
    for series in BMWSeries.objects.all():
        series_data = {
            'id': series.id,
            'name': series.name,
            'description': series.description,
            'image': str(series.image) if series.image else None,
            'created_at': datetime_to_str(series.created_at)
        }
        series_list.append(series_data)
    
    if series_list:
        series_collection.insert_many(series_list)
    print(f"Synced {len(series_list)} BMW Series records")

def sync_car_records():
    """Sync Car Records data to MongoDB"""
    car_records_collection = db['car_records']
    car_records_collection.delete_many({})  # Clear existing data
    
    records_list = []
    for record in CarRecord.objects.all():
        record_data = {
            'id': record.id,
            'bmw_series_id': record.bmw_series_id,
            'car_model': record.car_model,
            'registration_number': record.registration_number,
            'created_at': datetime_to_str(record.created_at),
            'updated_at': datetime_to_str(record.updated_at)
        }
        records_list.append(record_data)
    
    if records_list:
        car_records_collection.insert_many(records_list)
    print(f"Synced {len(records_list)} Car Records")

def sync_orders():
    """Sync Orders and Order Items data to MongoDB"""
    orders_collection = db['orders']
    orders_collection.delete_many({})  # Clear existing data
    
    orders_list = []
    for order in Order.objects.all():
        # Get order items for this order
        order_items = []
        for item in OrderItem.objects.filter(order=order):
            order_items.append({
                'id': item.id,
                'item_id': item.item_id,
                'quantity': item.quantity,
                'price_at_time': str(item.price_at_time)
            })
        
        order_data = {
            'id': order.id,
            'car_record_id': order.car_record_id,
            'total_amount': str(order.total_amount),
            'status': order.status,
            'paid_at': datetime_to_str(order.paid_at),
            'created_at': datetime_to_str(order.created_at),
            'order_items': order_items
        }
        orders_list.append(order_data)
    
    if orders_list:
        orders_collection.insert_many(orders_list)
    print(f"Synced {len(orders_list)} Orders with their items")

if __name__ == "__main__":
    try:
        print("Starting data sync to MongoDB...")
        sync_series()
        sync_car_records()
        sync_orders()
        print("Data sync completed successfully!")
    except Exception as e:
        print(f"Error during sync: {str(e)}")
    finally:
        client.close() 