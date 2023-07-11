info = {
    "id": [1, 2, 3, 4],
    "Product": [
        {"id": 1, "Name": "product1", "Quantity": 50, "Rate": 500},
        {"id": 2, "Name": "product2", "Quantity": 80, "Rate": 400}
    ]
}

change = "product1"
if change in info["Product"]:
    print(change)
