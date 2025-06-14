# Online Auction System
# Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan

import time
from datetime import datetime
import uuid
from typing import Dict, List

class Item:
    def __init__(self, item_id: str, name: str, starting_price: float, end_time: datetime):
        self.item_id = item_id
        self.name = name
        self.starting_price = starting_price
        self.current_price = starting_price
        self.end_time = end_time
        self.bids: Dict[str, float] = {}
        self.highest_bidder = None

    def place_bid(self, bidder: str, amount: float) -> bool:
        if datetime.now() > self.end_time:
            return False
        if amount <= self.current_price:
            return False
        self.bids[bidder] = amount
        self.current_price = amount
        self.highest_bidder = bidder
        return True

class AuctionSystem:
    def __init__(self):
        self.items: Dict[str, Item] = {}
        self.users: List[str] = []

    def register_user(self, username: str):
        if username not in self.users:
            self.users.append(username)
            return True
        return False

    def add_item(self, name: str, starting_price: float, duration_hours: float) -> str:
        item_id = str(uuid.uuid4())
        end_time = datetime.now() + timedelta(hours=duration_hours)
        self.items[item_id] = Item(item_id, name, starting_price, end_time)
        return item_id

    def place_bid(self, item_id: str, username: str, amount: float) -> bool:
        if item_id not in self.items or username not in self.users:
            return False
        return self.items[item_id].place_bid(username, amount)

    def get_item_status(self, item_id: str) -> str:
        if item_id not in self.items:
            return "Item not found"
        item = self.items[item_id]
        status = f"Item: {item.name}\nCurrent Price: ${item.current_price:.2f}\n"
        status += f"End Time: {item.end_time}\n"
        status += f"Highest Bidder: {item.highest_bidder if item.highest_bidder else 'None'}\n"
        status += f"Status: {'Active' if datetime.now() < item.end_time else 'Ended'}"
        return status

    def get_all_items(self) -> List[str]:
        return [item_id for item_id in self.items]

def main():
    print("""
    ╔════════════════════════════════════════════════════╗
    ║      Online Auction System                          ║
    ║      Coded by Pakistani Ethical Hacker              ║
    ║      Mr Sabaz Ali Khan                             ║
    ╚════════════════════════════════════════════════════╝
    """)
    
    auction = AuctionSystem()
    
    while True:
        print("\n1. Register User")
        print("2. Add Auction Item")
        print("3. Place Bid")
        print("4. View Item Status")
        print("5. List All Items")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            username = input("Enter username: ")
            if auction.register_user(username):
                print(f"User {username} registered successfully!")
            else:
                print("Username already exists!")
                
        elif choice == "2":
            name = input("Enter item name: ")
            try:
                starting_price = float(input("Enter starting price: $"))
                duration = float(input("Enter auction duration (hours): "))
                item_id = auction.add_item(name, starting_price, duration)
                print(f"Item added with ID: {item_id}")
            except ValueError:
                print("Invalid price or duration!")
                
        elif choice == "3":
            item_id = input("Enter item ID: ")
            username = input("Enter your username: ")
            try:
                amount = float(input("Enter bid amount: $"))
                if auction.place_bid(item_id, username, amount):
                    print("Bid placed successfully!")
                else:
                    print("Bid failed! Check item ID, username, or bid amount.")
            except ValueError:
                print("Invalid bid amount!")
                
        elif choice == "4":
            item_id = input("Enter item ID: ")
            print(auction.get_item_status(item_id))
            
        elif choice == "5":
            items = auction.get_all_items()
            if items:
                print("\nAvailable Items:")
                for item_id in items:
                    print(f"ID: {item_id} - {auction.items[item_id].name}")
            else:
                print("No items available!")
                
        elif choice == "6":
            print("Thank you for using the Online Auction System!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    from datetime import timedelta
    main()