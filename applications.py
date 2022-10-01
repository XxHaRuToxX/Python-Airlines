

import random
from typing import Dict, List
from config import CURRENCY_MONEY_SOLES


def main():
    flight_program:List[Dict[str, str | float | int]] = [
        {
            "code": "LIM - AYA",
            "route": "LIMA - AYACUCHO",
            "airplane": "A001",
            "outgoing": "06:30AM",
            "sales_economic": int(random.randint(int(120), int(130))),
            "sales_premium": int(random.randint(int(10), int(20))),
        },
        {
            "code": "LIM - CUS",
            "route": "LIMA - CUSCO",
            "airplane": "A002",
            "outgoing": "07:25AM",
            "sales_economic": int(random.randint(int(130), int(144))),
            "sales_premium": int(random.randint(int(15), int(24))),
        },
        {
            "code": "LIM - ARE",
            "route": "LIMA - AREQUIPA",
            "airplane": "A003",
            "outgoing": "08:10AM",
            "sales_economic": int(random.randint(int(115), int(138))),
            "sales_premium": int(random.randint(int(16), int(22))),
        },
        {
            "code": "LIMA - TAR",
            "route": "LIMA - TARAPOTO",
            "airplane": "A004",
            "outgoing": "08:50AM",
            "sales_economic": int(random.randint(int(100), int(120))),
            "sales_premium": int(random.randint(int(12), int(18))),
        },
        {
            "code": "AYA - LIM",
            "route": "AYACUCHO - LIMA",
            "airplane": "A001",
            "outgoing": "15:45AM",
            "sales_economic":int( random.randint(int(100), int(115))),
            "sales_premium": int(random.randint(int(10), int(15))),
        },
        {
            "code": "CUS - LIM",
            "route": "CUSCO - LIMA",
            "airplane": "A002",
            "outgoing": "16:25AM",
            "sales_economic": int(random.randint(int(105), int(120))),
            "sales_premium": int(random.randint(int(14), int(20))),
        },
        {
            "code": "ARE - LIM",
            "route": "AREQUIPA - LIMA",
            "airplane": "A003",
            "outgoing": "17:15AM",
            "sales_economic": int(random.randint(int(100), int(110))),
            "sales_premium": int(random.randint(int(13), int(18))),
        },
        {
            "code": "TAR - LIM",
            "route": "TARAPOTO - LIMA",
            "airplane": "A004",
            "outgoing": "17:50AM",
            "sales_economic": int(random.randint(int(90), int(105))),
            "sales_premium": int(random.randint(int(10), int(15))),
        },
    ]

    flight_ticket: List[Dict[str, str | float | int]] = [
        {
            "base_sale_price": 55.19,
            "economic_seat": 8,
            "premium_seat": 16,
        },
        {
            "base_sale_price": 136.51,
            "economic_seat": 8,
            "premium_seat": 16,
        },
        {
            "base_sale_price": 90.59,
            "economic_seat": 8,
            "premium_seat": 16,
        },
        {
            "base_sale_price": 71.89,
            "economic_seat": 8,
            "premium_seat": 16,
        },
        {
            "base_sale_price": 40.42,
            "economic_seat": 7,
            "premium_seat": 16,
        },
        {
            "base_sale_price": 124.32,
            "economic_seat": 7,
            "premium_seat": 16,
        },
        {
            "base_sale_price": 86.59,
            "economic_seat": 7,
            "premium_seat": 16,
        },
        {
            "base_sale_price": 68.42,
            "economic_seat": 7,
            "premium_seat": 16,
        },
    ]
    # Getting the base_price plus the economic seat
    get_prices_economic = [float(v["base_sale_price"]+v["economic_seat"]) for k, v in enumerate(flight_ticket)]

    # Getting the addition from base sales price plus the economic seat
    suma_prices_economic = float(sum([float(v["base_sale_price"]+v["economic_seat"]) for k, v in enumerate(flight_ticket)]))

    # Getting the randon ticket from economic sales
    ticket_random_get_economic = [float(v["sales_economic"]) for k, v in enumerate(flight_program)]

    # Getting the total income from the sale of economy tickets
    multi_prices_ticket_economic = round(sum([round((x*y),2) for x,y in zip(get_prices_economic,ticket_random_get_economic)]),2)

    # Getting the base_price plus the premium seat
    get_prices_premium = [float(v["base_sale_price"]+v["premium_seat"]) for k, v in enumerate(flight_ticket)]

    # Getting the addition from base sales price plus the premium seat
    suma_prices_premium = sum([float(v["base_sale_price"]+v["premium_seat"]) for k, v in enumerate(flight_ticket)])

    # Getting the randon ticket from premium sales
    ticket_random_get_premium = [float(v["sales_premium"]) for k, v in enumerate(flight_program)]

    # Getting the total income from the sale of premium tickets
    multi_prices_ticket_premium = round(sum([round((x*y),2) for x,y in zip(get_prices_premium,ticket_random_get_premium)]),2)

    #Addition from sales economic
    tickets_economic:int = sum([int(v["sales_economic"]) for k, v in enumerate(flight_program)])

    #Addition from sales premium
    tickets_premium:int = sum([int(v["sales_premium"]) for k, v in enumerate(flight_program)])

    # The whole tickets passenger sold
    sales_tickets_total = tickets_economic + tickets_premium
    
    # Getting the whole IGV 
    igv_total = (multi_prices_ticket_premium + multi_prices_ticket_economic) * 1.18;

    # Average value of a ticket economic
    average_economic_prices = suma_prices_economic / 8

    # Average value of a ticket premium
    average_premium_prices = suma_prices_premium / 8

    # Adsition from two list between economic and premium
    economic_plus_premium_flights = ([(x+y) for x,y in zip(ticket_random_get_economic,ticket_random_get_premium)])

    # Maximun quantity passengers
    max_value_economic_plus_premium = None

    for num in economic_plus_premium_flights:
        if (max_value_economic_plus_premium is None or num > max_value_economic_plus_premium):
            max_value_economic_plus_premium = num

    # Minimun quantity passengers
    min_value_economic_premium = None

    for num in economic_plus_premium_flights:
        if (min_value_economic_premium is None or num < min_value_economic_premium):
            min_value_economic_premium = num
    
    # List of flights economic
    flight_list_economic = ([round((x*y),2) for x,y in zip(get_prices_economic,ticket_random_get_economic)])

    # List of flights premium
    flight_list_premium = ([round((x*y),2) for x,y in zip(get_prices_premium,ticket_random_get_premium)])

    # Flights economic plus Premium / the three higher flights
    flight_list_economic_plus_premium = sorted([round((x+y),2) for x,y in zip(flight_list_economic,flight_list_premium)])

    # Flight higher tickets passenger
    ticket_higher_passenger =  ([round((x+y),2) for x,y in zip(ticket_random_get_economic,ticket_random_get_premium)])

    # First Array from higher ticket passenger from 0 - 4
    first_array_passenger_tickets = ticket_higher_passenger[0:4]

    # Second Array from higher ticket passenger from 5 - 8
    second_array_passenger_tickets = ticket_higher_passenger[4:8]

    #Higher quantity of tickets passengers
    ticket_higher_passenger_suma =  max([round((x+y),2) for x,y in zip(first_array_passenger_tickets,second_array_passenger_tickets)])

    #Higher quantity of tickets passengers addition
    get_tickets_higher =  [round((x+y),2) for x,y in zip(first_array_passenger_tickets,second_array_passenger_tickets)]

    #Get the index from the higher ticket passenger
    get_index_higher_max = get_tickets_higher.index(ticket_higher_passenger_suma)

    # Get the airplane from 0 - 4
    get_all_airplane = [str(v["airplane"]) for k, v in enumerate(flight_program[0:4])]
    
    # "{}{:,.2f}".format(CURRENCY_SYMBOL, rep_total_sale)
    print("¿Cuál es el total de pasajes vendidos entre todos los vuelos? ", sales_tickets_total)
    print("¿Cuál es el total de ingresos por la venta de pasajes económicos? ", "{}{:,.2f}".format(CURRENCY_MONEY_SOLES ,multi_prices_ticket_economic))
    print("¿Cuál es el total de ingresos por la venta de pasajes premium? ", "{}{:,.2f}".format(CURRENCY_MONEY_SOLES ,multi_prices_ticket_premium))
    print("¿Cuál es el importe total de IGV cobrado? ", "{}{:,.2f}".format(CURRENCY_MONEY_SOLES ,igv_total))
    print("¿Cuál es el valor promedio de un pasaje económico? ", "{}{:,.2f}".format(CURRENCY_MONEY_SOLES ,average_economic_prices))
    print("¿Cuál es el valor promedio de un pasaje premium? ", "{}{:,.2f}".format(CURRENCY_MONEY_SOLES ,average_premium_prices))
    print('¿Cuál fue el vuelo con la mayor cantidad de pasajeros? ', max_value_economic_plus_premium)
    print('¿Cuál fue el vuelo con la menor cantidad de pasajeros? ', min_value_economic_premium)
    print('¿Cuáles son los tres primeros vuelos que obtuvieron los mayores ingresos por la venta de asientos?',"S/.", " S/. ".join([str(_) for _ in flight_list_economic_plus_premium[5:8]]))
    print('Mayor cantidad de pasajeros', ticket_higher_passenger_suma)

    if get_index_higher_max == 0:
        print("¿Cuál fue el avión que transportó la mayor cantidad de pasajeros? ", ticket_higher_passenger_suma, get_all_airplane[0])
    else:
        if get_index_higher_max == 1:
            print("¿Cuál fue el avión que transportó la mayor cantidad de pasajeros? ", ticket_higher_passenger_suma, get_all_airplane[1])
        else:
            if get_index_higher_max == 2:
                print("¿Cuál fue el avión que transportó la mayor cantidad de pasajeros? ", ticket_higher_passenger_suma, get_all_airplane[2])
            else:
                print("¿Cuál fue el avión que transportó la mayor cantidad de pasajeros? ", ticket_higher_passenger_suma, get_all_airplane[3])

        

if __name__ == "__main__":
    main()
