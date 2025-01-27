import streamlit as st

# App Title
st.title("Crypto OTC Settlement Calculator")

# User Inputs
btc_market_price = st.number_input("Enter Bitcoin Market Price in USD (e.g., 98826):", min_value=0.0, step=0.01, value=98826.0)
btc_quantity = st.number_input("Enter BTC Quantity (e.g., 68.728886):", min_value=0.0, step=0.000001, value=68.728886)
spread_percentage = st.number_input("Enter Spread (%) (e.g., 0.1 for 10 bps):", min_value=0.0, step=0.01, value=0.1)
settlement_currency = st.selectbox("Select Settlement Currency:", ["USDC", "USDT", "EUR", "GBP"])

# Calculate Price Offered to Customer
spread_decimal = spread_percentage / 100
price_offered = btc_market_price * (1 - spread_decimal)

# Calculate Settlement Amount
settlement_amount = price_offered * btc_quantity

# Display Results
st.write("### Results:")
st.write(f"**Input BTC Market Price:** ${btc_market_price:,.2f} USD")
st.write(f"**Input BTC Quantity:** {btc_quantity:.6f}")
st.write(f"**Input Spread (%):** {spread_percentage:.2f}")
st.write(f"**Selected Settlement Currency:** {settlement_currency}")
st.write(f"**Price Offered to Customer:** ${price_offered:,.2f} {settlement_currency}")
st.write(f"**Settlement Amount:** {settlement_amount:,.2f} {settlement_currency}")

# Final Output Message
if settlement_currency:
    st.write(
        f"Xapo can pay **${price_offered:,.2f} {settlement_currency}** on **{btc_quantity:.6f} BTC**, "
        f"for a total of **{settlement_amount:,.2f} {settlement_currency}**."
    )