import json
from unicodedata import category
from flask import Flask, abort, request
from mock_data import catalog
from config import db
from 

app = Flask("Server")

@app.route("/")
def home():
    return "hello from Flask"


@app.route("/me")
def about_me():
    return "Derek Urruita"



###############################################
###############  API ENDPOINT #################
###############################################


@app.route("/api/catalog", methods=["get"])
def get_catalog():
    products = []
    cursor = db.products.find({})

    for prod in cursor:
        prod["_id"] = str(product["_id"])
        products.append(prod)
    
    return json.dumps(products)



@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()

    db.products.inseert_one(product)
    print(product)

    # fix id
    product["_id"] = str(product["_id"])

    return json.dumps(product)




@app.route("/api/catalog/count")
def product_count():
    cursor = db.products.find({})
    count = 0 
    for prod in cursor:
        count += 1

    return json.dumps(count)


@app.route("/api/catalog/total")
def total_of_catalog():
    total = 0
    cursor = db.products.find({})
    for prod in cursor:
        total += prod["price"]

    return json.dumps(total)

@app.route("/api/product/ <id>")
def get_by_id(id):
    prod = db.products.find_one({ "_id": ObjectID(id) })

    if not prod:
        return abort(404, "No product with such id")


    prod["_id"] = str(prod["_id"])
    return json.dumps(prod)

    



@app.route("/api/product/cheapest")
def cheapest_product():
    
    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)


@app.get("/api/categories")
def unique_categories():
    categories = []
    for prod in catalog:
        category = prod["category"]
        if not category in categories:
            categories.appened(category)

    return json.dumps(categories)



@app.get("/api/catalog/ <category>")
def prods_by_category(category):
    cursor = db.products.find({"category": category})
    for prod in cursor: 
        prod["_id"] = str(prod["_id"])
        products.append(prod)

    return json.dumps(result)



@app.get("/api/someNumbers")
def some_numbers():

    numbers = []

    for num in range (1, 51):
        numbers.append(num)

    return json.dumps(numbers)



#################################################################################
#########################  Coupon Code EndPoints ################################
#################################################################################


#1 get all coupons
#2 save coupon
#3 get a coupon based on its code

allCoupons = []

app.route("/api/couponCode", methods=["GET"])
def get_coupons():


@app.route("/api/couponCode", methods=["POST"])
def save_coupon():
    coupon = request.get_json()

    #must contain code, discout
    if not "code" in coupon or not "discount" in coupon:
        abort(400, "This coupon must contain a code and discount")
    # code should have at least 5 characters
    if len(coupon["code"]) < 5:
        abort(400, "The coupon must contain a code and discount")
    # discount should not be lower than 5 and not greater than 50
    if coupon["discount"] < 5 or coupon["discount"] > 50:
        abort(400, "Invalid discount amount")

    db.couponCodes.insert_one(coupon)

    coupon["_id"] = str(coupon["_id"])
    return json.dumps(coupon)










####################################################################################
###############       User Endpoints                    ############################
####################################################################################


{
    "_id" : "",
    "email" : "",
    "userName" : "",
    "password" : "",
    "first" : "",
    "last" : ""
}


@app.route("/api/users", methods=["get"])
def get_users():
    all_users = []
    cursor = db.users.find({})
    for user in cursor:
        user["_id"] = str(user["_id"])
        all_users.append(user)

@app.route("/api/users", methods=["post"])
def save_user():
    user = request.get_json()
    db.users.insert_one(user)
    #validate username, password, email
    if not "userName" in user or not "password" in user or not "email" in user:
        return abort(400, "object must contain userName, email and password")

    #check the values that are nt empty
    if len(user["userName"]) < 1 or len(user["password"]) < 1 or len(user["email"]) < 1:
        return abort(400, "object must contain values for userName, email and password")

    user["_id"] = str(user["_id"])
    return json.dumps(user)


@app.route("/api/users/<email>")
def get_user_by_email(email):
    user = db.users.find_one({"email": email})
    if not user:
        return abort(404, "invalid code")

    user["_id"] = str(user["_id"])
    return json.dumps(user)



@app.route("/api/users/login", methods=["POST"])
def validate_user_data():
    data = request.get_json() # <= dict with user and password
    print(data)

    #if there is not user in data, return a 400 error
    if not 'user' in data:
        return abort(400, "User is required for python")

    user = db.users.find_one({"username": data["user"], "password": data["password"]})
    if not user:
        abort(401, "No such user with that user and password")

    user["_id"] = str(user["_id"])
    user.pop("password") #remove the key and value from the dict
    return json.dumps(user)

app.run(debug=True)