import cellphone

def main():
    phones = make_list()
    print("Here is the data you entered: ")
    display_list(phones)

def make_list():
    phone_list = []
    print("Enter data for five phones.")
    for count in range(1,6):
        print("Phone number " + str(count) + ":")
        man = input("Enter the manufacturer: ")
        mod = input("Enter the model number: ")
        retail = float(input("Enter the retail price: "))
        print()
        phone = cellphone.Cellphone(man,mod,retail)
        phone_list.append(phone)
    return phone_list

def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()

main()