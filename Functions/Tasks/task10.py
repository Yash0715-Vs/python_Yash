def book_ticket(name, source="Ahmedabad", destination="Mumbai", seat_type="Sleeper"):
    
    print(f"Passenger  : {name}")
    print(f"Source     : {source}")
    print(f"Destination: {destination}")
    print(f"Seat Type  : {seat_type}")
    print()

# 1. Using only the required argument
book_ticket("Yash")

# 2. Using keyword arguments in a different order
book_ticket(destination="Delhi", name="Rahul", seat_type="AC", source="Surat")

# 3. Overriding only the destination
book_ticket("Priya", destination="Pune")

# 4. Overriding all default values
book_ticket("Amit", "Jaipur", "Goa", "First Class")