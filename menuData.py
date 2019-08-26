class menu():

    def __init__(self):
        self.data = {
            "Cafe latte" : {
                "Regular" : 450,
                "Large" : 500
            },
            "Cappucino" : {
                "Regular" : 450,
                "Large" : 510
            },
            "Espresso" : {
               "Regular" : 400,
               "Large" : 480 
            },
            "Americano" : {
                "Regular" : 410,
                "Large" : 480
            },
            "Macchiato" : {
                "Regular" : 450,
                "Large" : 500
            }
            "Caffe Mocha" : {
                "Regular" : 350,
                "Large" : 450
            },
            "English Breakfast Tea" : {
                "Regular" : 300,
                "Large" : 400
            }
            "Sugar" : {
                "1 tsp" : 0
            }
            "Extra Chocolate" : {
                "1 tsp" : 50
            }
        }
        print("[Menu] Object INIT")
    
    def getMenu(self):
        return self.data