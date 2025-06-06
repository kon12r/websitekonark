import streamlit as st
st.session_state.orders = []
st.header("Welcome to Konark's Website")
y = st.text_input("What is your name?")
x = st.text_input("What would you like to order? (coal, steel, gold, diamond, ruby)")
if x:
    x = x.lower()
    if x in ["coal", "steel", "gold", "diamond", "ruby"]:
        st.session_state.orders.append(x)
        st.success(f"We would love to sell you {x}!")
    else:
        st.warning("Sorry, we only sell coal, steel, gold, diamond, or ruby.")
st.subheader("Your Orders:")
if st.session_state.orders:
    for idx, item in enumerate(st.session_state.orders, 1):
        st.write(f"{idx}. {item.capitalize()}")
else:
    st.write("No orders yet.")