stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

# for purchase in purchases:
#     total_purchase = purchase[1]*purchase[3]
#     name = stockDict[purchase[0]]
#     print(f'I bought ${total_purchase} from {name}')

GE_dict = {"ticker": "GE", "info": []}
CAT_dict = {"ticker": "CAT",  "info": []}
for purchase in purchases:
    if purchase[0] == "GE":
        newList = [purchase[1], purchase[2], purchase[3]]
        GE_dict["info"].append(newList)
    elif purchase[0] =="CAT":
        newList = [purchase[1], purchase[2], purchase[3]]
        CAT_dict["info"].append(newList)

arr = [GE_dict, CAT_dict]
for dic in arr:
    name= dic["ticker"]
    print(f"-----{name}-----")
    for info in dic["info"]:
        print(f"{info[0]} shares of {info[2]} on {info[1]}")

