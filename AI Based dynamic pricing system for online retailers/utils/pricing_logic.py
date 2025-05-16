def suggest_price(base_price, demand, season, rating, competitor_price):
    price = base_price

    # Demand effect
    if demand == "High":
        price *= 1.20
    elif demand == "Medium":
        price *= 1.10
    else:
        price *= 0.95

    # Season effect
    if season == "Summer":
        price *= 1.05
    elif season == "Winter":
        price *= 0.97

    # Rating effect
    if rating >= 4.5:
        price += 20
    elif rating <= 2.0:
        price -= 10

    # Competitor price effect
    if competitor_price > 0:
        price = (price + competitor_price) / 2

    return price