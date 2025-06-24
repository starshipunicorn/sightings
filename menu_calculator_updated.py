import streamlit as st

# Menu from Sightings
menu = {
    "Breakfast": {
        "Supernova Breakfast Sandwich": 110,
        "Crater Cinnamon Roll Pancakes": 75,
        "Nebula Nosh Chicken & Waffles": 120
    },
    "Main Dishes": {
        "Galaxy Guac Burger": 125,
        "Cosmic Corndog": 85,
        "Andromeda Invader Curry": 105,
        "Protostar Pulled Pork Sandwich": 125,
        "Planetary Pizza": 95,
        "Big Dipper Birria Tacos": 95
    },
    "Desserts": {
        "Martian Mousse": 75,
        "Black Hole Brownies": 70,
        "Pie in the Sky": 75,
        "Astronaut Ice Cream": 75,
        "Chocolate Milky Way": 75,
        "Spacecraft S’mores Shake": 450
    },
    "Beverages": {
        "Starlight Lemonade": 28,
        "Lunar Lemonade": 27,
        "Galactic Grape Soda": 27,
        "Nebula Nectar Cola": 27,
        "Horchata": 30,
        "Comet Cola Float": 52
    },
    "Extras": {
        "Preservatives": 50
    }
}

# Calculate pricing
def calculate_total(order, discount=0, fee=0):
    subtotal = sum(menu[cat][item] * qty for (cat, item), qty in order.items())
    discount_amt = subtotal * (discount / 100)
    fee_amt = (subtotal - discount_amt) * (fee / 100)
    total = subtotal - discount_amt + fee_amt
    return round(subtotal, 2), round(total, 2)

# App layout
st.title("👽 Sightings Intergalactic Order Calculator 🛸")
st.markdown("_ExtraTerrestrial Flavors & Comfort Bites_")

st.sidebar.title("🛠️ Settings")
discount = st.sidebar.slider("Discount (%)", 0, 100, 0)
fee = st.sidebar.slider("Service Fee (%)", 0, 100, 0)

order = {}

sections = list(menu.keys())
icons = {
    "Breakfast": "🥓",
    "Main Dishes": "🌮",
    "Desserts": "🍰",
    "Beverages": "🥤",
    "Extras": "🧪"
}

# Create 2-column layout
for i in range(0, len(sections), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(sections):
            section = sections[i + j]
            with cols[j]:
                st.subheader(f"{icons.get(section, '')} {section}")
                for item, price in menu[section].items():
                    qty = st.number_input(f"{item} (${price})", min_value=0, max_value=500, step=1, key=item)
                    if qty > 0:
                        order[(section, item)] = qty

# Show total on button
if st.button("🚀 Calculate Total"):
    subtotal, total = calculate_total(order, discount, fee)
    st.markdown(f"### 🌌 Subtotal: **${subtotal}**")
    st.markdown(f"### 💫 Total After Discounts/Fees: **${total}**")

    st.subheader("📦 Order Summary")
    for (cat, item), qty in order.items():
        st.markdown(f"- {item} ({cat}) x {qty} @ ${menu[cat][item]} each")
