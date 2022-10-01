import random


class FlightProgram (object):
    def __init__(self, code:str, route: str, airplane: str, outgoing: str, sales_economic: int, sales_premium:int ):
        self.code:str = code
        self.route: str = route
        self.airplane:str = airplane
        self.outgoing:str = outgoing
        self.sales_economic: int = sales_economic
        self.sales_premium: int = sales_premium

    

        