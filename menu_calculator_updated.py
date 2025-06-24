import streamlit as st

# 🛸 Menu based on Sightings image
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

# 🧮 Total Calculation Logic
def calculate_total(order, discount=0, fee=0):
    subtotal = sum(menu[cat][item] * qty for (cat, item), qty in order.items())
    discount_amt = subtotal * (discount / 100)
    fee_amt = (subtotal - discount_amt) * (fee / 100)
    total = subtotal - discount_amt + fee_amt
    return round(subtotal, 2), round(total, 2)

# 🌌 App Layout
st.set_page_config(page_title="Sightings Calculator", layout="centered")
st.title("👽 Sightings Order Calculator 🛸")
st.markdown("_ExtraTerrestrial Flavors & Comfort Bites_")

st.sidebar.title("🛠️ Settings")
discount = st.sidebar.slider("Discount (%)", 0, 100, 0)
fee = st.sidebar.slider("Service Fee (%)", 0, 100, 0)

order = {}

# 📱 Mobile-Friendly Expandable Sections
sections_ordered = [
    ("Breakfast", "🥓"),
    ("Main Dishes", "🌮"),
    ("Desserts", "🍰"),
    ("Beverages", "🥤"),
    ("Extras", "🧪")
]

for section, icon in sections_ordered:
    with st.expander(f"{icon} {section}", expanded=True):
        for item, price in menu[section].items():
            qty = st.number_input(f"{item} (${price})", min_value=0, max_value=500, step=1, key=f"{section}_{item}")
            if qty > 0:
                order[(section, item)] = qty

# 🚀 Calculate Button
if st.button("🚀 Calculate Total"):
    subtotal, total = calculate_total(order, discount, fee)

    st.markdown("---")
    st.markdown(f"### 🌌 Subtotal: **${subtotal}**")
    st.markdown(f"### 💫 Total After Discounts/Fees: **${total}**")

    st.subheader("📦 Order Summary")
    for (cat, item), qty in order.items():
        st.markdown(f"- **{item}** ({cat}) × {qty} @ ${menu[cat][item]} each")
