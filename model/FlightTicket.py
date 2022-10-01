
class FlightTicket(object):
    def __init__(self, code: str, base_sale_price:float, economic_seat:float, premium_seat:float ):
        self.code: str = code
        self.base_sale_price: float = base_sale_price
        self.economic_seat: float = economic_seat
        self.premium_seat: float = premium_seat
       
    
    def __repr__(self) -> str:
        """
        Método especial para representar el objeto de una clase como string.
        """
        return self.code
    
    def update_sale_price_by_seat(self) -> None:
        """
        Actualiza el precio de venta del producto según el porcentaje de incremento definido 
        por cada tienda.
        """
        self.sale_price_economic = self.base_sale_price + self.economic_seat
        self.sale_price_premium = self.base_sale_price + self.premium_seat
        self.final_sale_price = self.sale_price_economic + self.sale_price_premium

    
        
        