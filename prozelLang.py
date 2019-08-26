class Process():
    def __init__(self, data):
        self.data = data
    def get_string(self):
        # for i in range(0, len(self.data) -8):
        #     tmpSTR = ""
        #     for ii in range(0, 8): #<?prozel
        #         tmpSTR += self.data[i + ii]
        #         if tmpSTR == "<?prozel":
        #             print("[PRZL LANG] Found Start at character: {}".format(i+ii))
        #             return "is PROZEL"
        # return "Not Prozel"
        self.data = self.data.replace("<?businessname?>", "Detroit Café")
        self.data = self.data.replace("<?mainstylelocation?>", "/style/main.css")
        self.data = self.data.replace("<?debug?>", "Not Implemented")
        return self.data
