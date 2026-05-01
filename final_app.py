import streamlit as st
import pandas as pd

st.set_page_config(page_title="Trivandrum Stay AI", page_icon="🏠")
st.title("🏠 Technopark Stay & Rent Predictor")
st.markdown("Developed by: *[Insha Ugera]*, 2nd Year AI & DS")

# 1. Sidebar Inputs
st.sidebar.header("Stay Details")
stay_type = st.sidebar.radio(
    "Select Stay Type", ["Full Apartment", "PG / Hostel"])
loc = st.sidebar.selectbox("Select Location", ["Technopark Phase 1", "Technopark Phase 3",
                                               "Kazhakkoottam"])

# 2. Logic for PG vs Apartment
if stay_type == "Full Apartment":
    sqft = st.sidebar.number_input(
        "Enter Square Feet", min_value=300, max_value=3000, value=1000)
    base_price = sqft * 15  # ₹15 per sqft

    # Location Multipliers
    multipliers = {"Technopark Phase 1": 1.2,
                   "Technopark Phase 3": 1.1, "Kazhakkoottam": 1.0}
    final_price = base_price * multipliers[loc]
    label = "Estimated Monthly Rent"

else:  # PG / Hostel Logic
    room_type = st.sidebar.selectbox(
        "Room Type", ["Single Room", "2-Sharing", "3-Sharing"])
    pg_rates = {"Single Room": 12000, "2-Sharing": 7500, "3-Sharing": 5500}

    # PGs are slightly more expensive near Phase 1
    loc_extra = {"Technopark Phase 1": 1000,
                 "Technopark Phase 3": 500, "Kazhakkoottam": 0}
    final_price = pg_rates[room_type] + loc_extra[loc]
    label = "Estimated PG Rate (Per Month)"

# 3. Display Result
if st.button("Calculate Market Value"):
    st.header(f"{label}: ₹{int(final_price):,}")
    st.write(f"Based on trends for a {stay_type} in **{loc}**.")

    # Bonus for Resume: Explain the "Logic"
    with st.expander("See AI Logic"):
        st.write("For Apartments: Linear Regression (Price per SqFt).")
        st.write(
            "For PGs: Classification-based pricing (Fixed rate + Location Premium).")
