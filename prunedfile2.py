def main():
    detail = get_details()
    print(f"{detail[0]} from {detail[1]}")

def get_details():
    name = input("Name: ")
    address = input("Address: ")
    return (name, address)

if __name__ == "__main__":
    main()