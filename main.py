import streamlit as st


def calculate_price(
    price_per_sheet: float,
    sheet_width: float,
    sheet_height: float,
    sticker_width: float,
    sticker_height: float,
):
    sheet_area = sheet_width * sheet_height
    sticker_area = sticker_width * sticker_height

    return (sheet_area / sticker_area) / price_per_sheet


price_per_sheet = st.number_input("Price Per Sheet ($)", min_value=0.01)
sheet_width = st.number_input("Sheet Width (mm)", min_value=1.0)
sheet_height = st.number_input("Sheet Height (mm)", min_value=1.0)
sticker_width = st.number_input("Sticker Width (mm)", min_value=1.0)
sticker_height = st.number_input("Sticker Height (mm)", min_value=1.0)

if st.button("Calculate"):
    st.write(
        f"Price Per Sticker: ${
            calculate_price(
                price_per_sheet,
                sheet_width,
                sheet_height,
                sticker_width,
                sticker_height,
            ):.2f}"
    )
