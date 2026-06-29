import streamlit as st
import numpy as np
import joblib

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="House Price Prediction",
    layout="wide"
)
st.markdown("""
<style>

/* Highlight Predict Button */
.stButton > button {
    background-color: #000000;
    color: white;
    font-size: 18px;
    font-weight: 600;
    padding: 0.7rem 1rem;
    border-radius: 10px;
    border: none;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background-color: #333333;
    transform: scale(1.02);
    cursor: pointer;
}

</style>
""", unsafe_allow_html=True)
# ----------------------------
# Load Model
# ----------------------------
model = joblib.load("house_price_model.pkl")

# ----------------------------
# Sidebar
# ----------------------------


st.sidebar.info(
    """
    Enter the house details and click **Predict Price**
    to estimate the selling price.
    """
)

# ----------------------------
# Title
# ----------------------------
st.title("House Price Prediction")

st.write(
    "Fill in the property details below to estimate the house price."
)

st.divider()

# ----------------------------
# Input Section
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        "Area (sq.ft)",
        min_value=500,
        max_value=20000,
        value=3000
    )

    bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5, 6])

    bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4, 5, 6])

    stories = st.selectbox("Stories", [1, 2, 3, 4])

    parking = st.selectbox("Parking", [0, 1, 2, 3])

with col2:
    mainroad = st.selectbox("Main Road", ["yes", "no"])

    guestroom = st.selectbox("Guest Room", ["yes", "no"])

    basement = st.selectbox("Basement", ["yes", "no"])

    hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])

    airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])

    prefarea = st.selectbox("Preferred Area", ["yes", "no"])

    furnishingstatus = st.selectbox(
        "Furnishing Status",
        ["furnished", "semi-furnished", "unfurnished"]
    )

# ----------------------------
# Manual Encoding
# ----------------------------
yes_no = {
    "yes": 1,
    "no": 0
}

furnishing = {
    "furnished": 0,
    "semi-furnished": 1,
    "unfurnished": 2
}

mainroad = yes_no[mainroad]
guestroom = yes_no[guestroom]
basement = yes_no[basement]
hotwaterheating = yes_no[hotwaterheating]
airconditioning = yes_no[airconditioning]
prefarea = yes_no[prefarea]
furnishingstatus = furnishing[furnishingstatus]

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Price", use_container_width=True):

    features = np.array([[
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad,
        guestroom,
        basement,
        hotwaterheating,
        airconditioning,
        parking,
        prefarea,
        furnishingstatus
    ]])

    with st.spinner("Calculating estimated house price..."):
        prediction = model.predict(features)[0]

    st.success(
        f"""


Estimated House Price: ₹  {prediction:,.0f}
"""
    )



