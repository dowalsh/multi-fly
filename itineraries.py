class Itinerary:
    def __init__(self, id, price, legs, isSelfTransfer, isProtectedSelfTransfer, farePolicy, eco, fareAttributes, isMashUp, hasFlexibleOptions, score):
        self.id = id
        self.price = price
        self.legs = legs
        self.isSelfTransfer = isSelfTransfer
        self.isProtectedSelfTransfer = isProtectedSelfTransfer
        self.farePolicy = farePolicy
        self.eco = eco
        self.fareAttributes = fareAttributes
        self.isMashUp = isMashUp
        self.hasFlexibleOptions = hasFlexibleOptions
        self.score = score