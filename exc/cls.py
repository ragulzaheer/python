class mobile:
    def __init__(self,Name,Model,Battery,Disply,RAM,ROM,Amount):
        self.name = Name
        self.model = Model
        self.battery = Battery
        self.disply = Disply
        self.ram = RAM
        self.rom = ROM
        self.amount = Amount
    def Mobile_Data(self):
        print("Mobile Name:",self.name,"Mobile Model:",self.model,
            "Battery :",self.battery,"Disply:",self.disply,
                "Size of RAM:",self.ram,"Size of ROM:",self.rom,
                    "Amont of Mobile:",self.amount)
        
        '''print("Battery :",self.battery)
        print("Disply:",self.disply)
        print("Size of RAM:",self.ram) 
        print("Size of ROM:",self.rom) 
        print("Amont of Mobile:",self.amount)'''
mob1 = mobile("samsung","F13","5000","corila","4","128","13,000")
mob1.Mobile_Data()

mob2 = mobile("Nokia","Gold","4500","corila","8","128","18,000")
mob2.Mobile_Data()

mob3 = mobile("Lava","Iris","4000","corila","4","32","8000")
mob3.Mobile_Data()

mob4 = mobile("OPPO","Magic","5000","corila","8","128","17,500")
mob4.Mobile_Data()