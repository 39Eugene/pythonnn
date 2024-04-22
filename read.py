def read_f1():
    a = open("details.txt","r")

    lists = []

    for each in a:
        new_lists = each.strip().split(',')

        new_dict ={
            "kitta_no": new_lists[0],
            "city": new_lists[1],
            "land_direction": new_lists[2],
            "area": new_lists[3],
            "price": new_lists[4],
            "status": new_lists[5]
        }

        lists.append(new_dict)

    a.close()

    return lists

new_lists = read_f1()

'''# Print the data in the console
for item in new_lists:
    print("Kitta Number:", item["kitta_no"])
    print("City:", item["city"])
    print("Land Direction:", item["land_direction"])
    print("Area:", item["area"])
    print("Price:", item["price"])
    print("Status:", item["status"])
    print()  # Empty line for better readability between entries '''


