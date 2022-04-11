



def test_dict():
    me = {
        "first": "Derek",
        "last": "Urruita",
        "age": 22,
        "hobbies": [],
        "address": {
            "street": "Mesa",
            "city": "Oceanside"
        },
        "another": 12,
    }
    
    print(me["first"] + " " + me["last"])

    print("My age is: " +str(me["age"]))
    print(f"My age is: {me['age']}")

    address = me["address"]
    print(address["street"])

    print(me["address"]["city"])



    # add new keys 
    me["color"] = "red"

    #  modifify existing keys 
    me["age"] = 36

    #check if a key exist in a dict
    if "age" in me:
        print("Age exist")


print("--- Dictionart Test -----")
test_dict()