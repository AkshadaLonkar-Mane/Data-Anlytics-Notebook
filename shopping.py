class ShoppingCart:

    # Class Variables
    products = ( {"product_name":"Apple","Price":2}
                ,{"product_name":"Banana","Price":0.5}
                ,{"product_name":"Pear","Price":2}
                ,{"product_name":"Watermelon","Price":5}
                ,{"product_name":"Grapes","Price":6}
                ,{"product_name":"Orange","Price":3})

    cust_name = None
    cart = [] 
    total_price = None
    product_name = None


    '''
    1. Add product to a shopping cart
    2. update cart
    3. Check product name is valid or not
    4. remove item from cart
    5. total price
    '''

# Add products to shopping cart
    def add_to_cart(self, p_name, p_qty):
        for p in self.products:
            if p['product_name'] == p_name:
                l_price = p_qty*p["Price"] 
# Update cart:
                for item in self.cart:
                    if item["product_name"] == p_name:
                        item["Qty"] += p_qty
                        item["Line_Item_Price"] += l_price
                        break
                else:
                    self.cart.append({"product_name":p_name,"Qty":p_qty,"Line_Item_Price":l_price})
                break

# Invalid product name:
        if p['product_name'] != p_name:
            print(f"{p_name} not found .")
            

#check the cart: 
    def show_cart(self):
        print('cart = ', self.cart, '\n')
        for item in self.cart:
            print('product_name = ', item['product_name'],'\t' 'qty = ',item['Qty'],'\t', 'total_price= ',item['Line_Item_Price'])



# Remove Item from cart:
    def remove_from_cart(self,p_name,p_qty):
        for p in self.products:
            # 1. Validate the Product Name
            if p["product_name"] == p_name:
                # 2. Check the cart for the product
                for c in self.cart:
                    if c["product_name"] == p_name and p_qty >= c["Qty"]:
                        self.cart.remove({"product_name":c["product_name"]
                                          ,"Qty":c["Qty"]
                                          ,"Line_Item_Price":c["Line_Item_Price"]})
                    elif  c["product_name"] == p_name and p_qty < c["Qty"]:
                       print(f"{p_qty} {p_name} removed from cart . \n")
                       # IF qty to remove is < the Qty in cart
                       # 1. Remove qty
                       # 2. Update new price
                       c["Qty"] = c["Qty"]-p_qty
                       c["Line_Item_Price"] = c["Line_Item_Price"]-(p["Price"]*p_qty)


# Total Bill:                      
    def bill_total(self):
        total_price = sum(item['Line_Item_Price'] for item in self.cart)
        print('\n','Line_Item_Price = ',total_price, '\n')




            
# calling functions    

cust1 = ShoppingCart()
cust1.cust_name="AAA"

cust1.add_to_cart("Onion",4)     # print(f"{p_name} not found .")

cust1.add_to_cart("Apple",2)   
cust1.add_to_cart("Apple",2)      # Adding to an existing product in cart
cust1.add_to_cart("Banana",3)
cust1.add_to_cart("Grapes",4)


cust1.remove_from_cart("Apple",1)  # Remove product from the cart

cust1.show_cart()
cust1.bill_total()

# Result:

'''
Onion not found .
1 Apple removed from cart . 

cart =  [{'product_name': 'Apple', 'Qty': 3, 'Line_Item_Price': 6}, {'product_name': 'Banana', 'Qty': 3, 'Line_Item_Price': 1.5}, {'product_name': 'Grapes', 'Qty': 4, 'Line_Item_Price': 24}] 

product_name =  Apple   qty =  3         total_price=  6
product_name =  Banana  qty =  3         total_price=  1.5
product_name =  Grapes  qty =  4         total_price=  24

 Line_Item_Price =  31.5 

'''

             

        

    


     