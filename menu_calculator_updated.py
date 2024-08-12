import streamlit as st

# Menu Items with their Prices
menu = {
    "Breakfast": {
        "Crater Cinnamon Roll Pancakes": 73.50,
        "Nebula Nosh Chicken & Waffles": 115.50,
        "Extraterrestrial Omelet": 87.50
    },
    "Starters": {
        "Celestial Caesar Salad": 70.00,
        "Alien Antenna Bites": 98.00,
        "Orbiting Onion Rings": 52.50
    },
    "Mains": {
        "Celestial Creature Gyro": 115.50,
        "Andromeda Invader Curry": 105.00,
        "Planetary Pizza": 70.00,
        "Galaxy Guac Burger and Meteorite Fries": 122.50
    },
    "Desserts": {
        "Spacecraft S’mores Shake": 56.00,
        "Blackhole Brownies": 66.50,
        "Martian Mousse": 73.50
    },
    "Alcoholic Drinks": {
        "UFO Umbrella Drink": 50.00,
        "Asteroid Amaretto Sour": 57.50,
        "Alien Ambrosia": 62.50
    },
    "Non-Alcoholic Drinks": {
        "Lunar Lemonade": 27.50,
        "Comet Cola Float": 32.50,
        "Galactic Grape Cola": 27.50,
        "Nebula Nectar Cola": 27.50
    }
}

# Function to calculate total price
def calculate_total(order, discount=0, fee=0):
    subtotal = 0
    for item, quantity in order.items():
        subtotal += menu[item[0]][item[1]] * quantity

    discount_amount = subtotal * (discount / 100)
    subtotal -= discount_amount

    fee_amount = subtotal * (fee / 100)
    total = subtotal + fee_amount

    return round(total, 2)

# Streamlit Interface
st.title("🚀 Sightings Menu Calculator 🌌")

st.sidebar.title("Settings")
discount = st.sidebar.slider("Discount (%)", 0, 100, 0)
fee = st.sidebar.slider("Additional Fee (%)", 0, 100, 0)

order = {}
cols = st.columns(2)

with cols[0]:
    st.subheader("🌅 Breakfast")
    for item, price in menu["Breakfast"].items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=10, step=1, key=item)
        if quantity > 0:
            order[("Breakfast", item)] = quantity

with cols[1]:
    st.subheader("🍲 Starters")
    for item, price in menu["Starters"].items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=10, step=1, key=item)
        if quantity > 0:
            order[("Starters", item)] = quantity

st.subheader("🍽️ Mains")
for item, price in menu["Mains"].items():
    quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=10, step=1, key=item)
    if quantity > 0:
        order[("Mains", item)] = quantity

st.subheader("🍰 Desserts")
for item, price in menu["Desserts"].items():
    quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=10, step=1, key=item)
    if quantity > 0:
        order[("Desserts", item)] = quantity

st.subheader("🍹 Alcoholic Drinks")
for item, price in menu["Alcoholic Drinks"].items():
    quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=10, step=1, key=item)
    if quantity > 0:
        order[("Alcoholic Drinks", item)] = quantity

st.subheader("🥤 Non-Alcoholic Drinks")
for item, price in menu["Non-Alcoholic Drinks"].items():
    quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=10, step=1, key=item)
    if quantity > 0:
        order[("Non-Alcoholic Drinks", item)] = quantity

if st.button("Calculate Total"):
    total_price = calculate_total(order, discount=discount, fee=fee)
    st.markdown(f"## 🧾 The total price of the order is: **${total_price}**")
