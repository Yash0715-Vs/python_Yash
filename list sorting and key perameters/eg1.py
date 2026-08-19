cars = [{"name": "hundai","model":"creta", "price":1500000},
        {"name": "toyota", "model": "fortuner", "price": 5000000},
        {"name": "kia","model": "seltos", "price": 2500000}]

total = 0
for car in cars:
    total+= car["price"]

average = total/len(cars)

cars.sort(key=lambda x:x["price"],reverse=True)
cheapest= min(cars ,key=lambda x:x["price"])
highest= max(cars ,key=lambda x:x["price"])
count = 0
for car in cars:
    if car["price"] < 3000000:
        count+=1
print(cars)
print(f"the cheapest price: {cheapest}")
print(f"the highest price: {highest}")
print(f"the average is: {average}")
print(f"below 30000: {count}")