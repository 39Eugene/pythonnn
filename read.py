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

for new_dict in new_lists:
    print(new_dict)