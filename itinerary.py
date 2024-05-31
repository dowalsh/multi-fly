class Itinerary:
    # def __init__(self, id, price, legs, isSelfTransfer, isProtectedSelfTransfer, farePolicy, eco, fareAttributes, isMashUp, hasFlexibleOptions, score):
    def __init__(self, id, price, legs):
        self.id = id
        self.price = price
        self.legs = legs
        # commenting out until we actually need these
        # self.isSelfTransfer = isSelfTransfer
        # self.isProtectedSelfTransfer = isProtectedSelfTransfer
        # self.farePolicy = farePolicy
        # self.eco = eco
        # self.fareAttributes = fareAttributes
        # self.isMashUp = isMashUp
        # self.hasFlexibleOptions = hasFlexibleOptions
        # self.score = score

    def __str__(self):
        # print price and each leg
        return f"Price: {self.price}\n" + "\n".join([str(leg) for leg in self.legs])

    def get_total_cost(self):
        return self.price
