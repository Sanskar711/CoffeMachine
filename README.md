# Coffee Machine
There are total 4 classes 
1. CoffeeMaker - Models the machine that makes the coffee
   Attributes -> resources {water, milk, and coffee}
   Functions -> a. report (Prints a report of all resources.)
                b. is_resource_sufficient (Returns True when order can be made, False if ingredients are insufficient.) 
                c. make_coffee (Deducts the required ingredients from the resources.)
           
2. MoneyMachine - Handles all transactions
  Attributes -> profit , money_recieved
  Functions -> a. report (Prints the current profit)
               b. process_coins (Returns the total calculated from coins inserted.)
               c. make_payment (Returns True when payment is accepted, or False if insufficient.)
               
3. MenuItem - Models each Menu Item.
  Attributes -> name, cost , ingredients {water , milk, coffee}

4. Menu - Models the Menu with drinks.
  Funtions -> a. get_items (Returns all the names of the available menu items)
              b. find_drink (Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None)
