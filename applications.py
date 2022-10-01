

import random
from typing import Dict, List


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

    get_prices_economic = [float(v["base_sale_price"]+v["economic_seat"]) for k, v in enumerate(flight_ticket)]
    suma_prices_economic = float(sum([float(v["base_sale_price"]+v["economic_seat"]) for k, v in enumerate(flight_ticket)]))

    ticket_random_get_economic = [float(v["sales_economic"]) for k, v in enumerate(flight_program)]

    multi_prices_ticket_economic = round(sum([round((x*y),2) for x,y in zip(get_prices_economic,ticket_random_get_economic)]),2)

    get_prices_premium = [float(v["base_sale_price"]+v["premium_seat"]) for k, v in enumerate(flight_ticket)]
    suma_prices_premium = sum([float(v["base_sale_price"]+v["premium_seat"]) for k, v in enumerate(flight_ticket)])
    ticket_random_get_premium = [float(v["sales_premium"]) for k, v in enumerate(flight_program)]

    multi_prices_ticket_premium = round(sum([round((x*y),2) for x,y in zip(get_prices_premium,ticket_random_get_premium)]),2)
    igv_total = (multi_prices_ticket_premium + multi_prices_ticket_economic) * 1.18;

    average_economic_prices = suma_prices_economic / 8
    average_premium_prices = suma_prices_premium / 8

    economic_plus_premium_flights = ([(x+y) for x,y in zip(ticket_random_get_economic,ticket_random_get_premium)])

    max_value_economic_plus_premium = None

    for num in economic_plus_premium_flights:
        if (max_value_economic_plus_premium is None or num > max_value_economic_plus_premium):
            max_value_economic_plus_premium = num

    min_value_economic_premium = None

    for num in economic_plus_premium_flights:
        if (min_value_economic_premium is None or num < min_value_economic_premium):
            min_value_economic_premium = num
    
    flight_list_economic = ([round((x*y),2) for x,y in zip(get_prices_economic,ticket_random_get_economic)])
    flight_list_premium = ([round((x*y),2) for x,y in zip(get_prices_premium,ticket_random_get_premium)])

    flight_list_economic_plus_premium = sorted([round((x+y),2) for x,y in zip(flight_list_economic,flight_list_premium)])

    ticket_higher_passenger =  ([round((x+y),2) for x,y in zip(ticket_random_get_economic,ticket_random_get_premium)])

    first_array_passenger_tickets = ticket_higher_passenger[0:4]
    second_array_passenger_tickets = ticket_higher_passenger[4:8]

    ticket_higher_passenger_suma =  max([round((x+y),2) for x,y in zip(first_array_passenger_tickets,second_array_passenger_tickets)])

    tickets_economic:int = sum([int(v["sales_economic"]) for k, v in enumerate(flight_program)])
    tickets_premium:int = sum([int(v["sales_premium"]) for k, v in enumerate(flight_program)])
    sales_tickets_total = tickets_economic + tickets_premium

    get_tickets_higher =  [round((x+y),2) for x,y in zip(first_array_passenger_tickets,second_array_passenger_tickets)]
    get_index_higher_max = get_tickets_higher.index(ticket_higher_passenger_suma)
    get_all_airplane = [str(v["airplane"]) for k, v in enumerate(flight_program[0:4])]

    print(tickets_economic, tickets_premium)
    print(sales_tickets_total)
    print("ticket random get economic",ticket_random_get_economic)
    print("ticket random get premium",ticket_random_get_premium)
    print("prices", type(get_prices_economic))
    print("multi, suma economic", multi_prices_ticket_economic)
    print("multi, suma premium", multi_prices_ticket_premium)
    print("igv", igv_total)
    print("Promedio economico de pasajes", average_economic_prices)
    print("Promedio premium de pasajes", average_premium_prices)
    print("economicos mas premiun vuelos", economic_plus_premium_flights)
    print('Maximum pasajes de economicos mas premimun:', max_value_economic_plus_premium)
    print('Maximum pasajes de economicos mas premimun:', min_value_economic_premium)
    print('Flights lista economico:', flight_list_economic)
    print('Flights lista premium:', flight_list_premium)
    print('Flights lista economic + premium:', flight_list_economic_plus_premium)
    print('Tres vuelos con mayor ingreso', flight_list_economic_plus_premium[5:8])
    print('Tickets alto passajeros', ticket_higher_passenger)
    print('Tickets del 1 al 4', first_array_passenger_tickets)
    print('Tickets del 5 al 8', second_array_passenger_tickets)
    print('Mayor cantidad de pasajeros', ticket_higher_passenger_suma)
    print('Get ticket higher', get_tickets_higher)
    print('Get ticket higher index', get_index_higher_max)
    print('Get all airplane', get_all_airplane)

    if get_index_higher_max == 0:
        print(ticket_higher_passenger_suma, get_all_airplane[0])
    else:
        if get_index_higher_max == 1:
            print(ticket_higher_passenger_suma, get_all_airplane[1])
        else:
            if get_index_higher_max == 2:
                print(ticket_higher_passenger_suma, get_all_airplane[2])
            else:
                print(ticket_higher_passenger_suma, get_all_airplane[3])

        

if __name__ == "__main__":
    main()
