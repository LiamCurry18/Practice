"""
Notes
- Line 27 and 33 is not needed since we are printing out the list on line 39

Grade:
A
"""

thislist = []
item = ""


def testduplicate(test):
    for x in thislist:
        if x == test: 
            return 1
    thislist.append(test)
    return 0

while item != "eggplant" or len("thislist") <= 20:   
        item = input("enter an item: ")
        if item == "eggplant":
            print("ah hell na")
            exit()
        elif item == 'exit':
            break
        elif item == "banana":
            print("ooh ee ooh ah ah ting tang walla balla bing bang")
            thislist.append(item)
        elif len(thislist) == 20:
            print("Too many items in list.")
            break
        else:
            blueberry = testduplicate(item)
            if blueberry == 1:
                print("already in list")
print(thislist)