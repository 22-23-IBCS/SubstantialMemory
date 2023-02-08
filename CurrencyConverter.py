class Converter:

    def __init__(self):
        self.countries= ["China", "Uk", "Canada", "Korea", "Japan", "Germany"]
        self.conversions= {"China" : 6.79,
                           "Uk" : 0.83,
                           "Canada": 1.35,
                           "Korea" : 1261.48,
                           "Japan": 132.66,
                           "Germany": 0.93}
        self.name={"China": "yuan",
                   "Uk" : "pounds",
                   "Canada" : "CAD",
                   "Korea": "won",
                   "Japan" : "yen",
                   "Germany" : "euros"}
    def getCountries(self):
        print("you can choose from")
        for i in range(len(self.countries)):
            print(self.countries[i])
    def getConversion(self, country):
        return str(self.conversions.get(country))+ " " + str(self.name.get(country))
    def convert(self, country):
        x=self.conversions.get(country)
        money=int(input("how much money you got?"))
        print(str(x*money)+ " " + str(self.name.get(country)))
        
    def intconvert(self, country):
        country1= input("What currency do you want to convert from")
        intmoney= int(input("how much money do you got"))
        y=self.conversions.get(country1)
        conmoney=intmoney/y
        z=self.conversions.get(country)
        return str(conmoney*z)+ " " + str(self.name.get(country))
        
def main():
    c = Converter()
    country="China"
    print(c.intconvert(country))
    
    

if __name__ == "__main__":
    main()
