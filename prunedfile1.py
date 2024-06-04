def main():
    detail = get_details()
    print(f"{detail['name']} from {detail['address']}")

def get_details():
    name = input("Name: ")
    address = input("Address: ")
    return {"name" : name, "address": address}

if __name__ == "__main__":
    main()