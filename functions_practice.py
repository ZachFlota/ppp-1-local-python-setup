def hello():
    print("Hello user!")

def pack(x, y, z):
    pack_list = [x, y, z]
    return(pack_list)
    print(pack_list) 


def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")

hello()
print(pack("a", "b", "c"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple", "banana", "cherry", "kiwi", "mango"])