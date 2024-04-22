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

'''for new_dict in new_lists:
    print(new_dict)'''

def display_lists(lists):
    print("Availabe lands:" )
    for new_dict in lists:
        if new_dict["status"] == "Available":
            print(new_dict["kitta_no"] + ":" + new_dict["city"] + "- " + new_dict["land_direction"] + ", Area:" + new_dict["area"] + "anna, Price:" + new_dict["price"])


    print("\n Not Availabe lands:" )
    for new_dict in lists:
        if new_dict["status"] == "Not Available":
            print(new_dict["kitta_no"] + ":" + new_dict["city"] + "- " + new_dict["land_direction"] + ", Area:" + new_dict["area"] + "anna, Price:" + new_dict["price"])


# Call read_f1() to read land details
new_lists = read_f1()

# Call display_lists() to display availability
display_lists(new_lists)