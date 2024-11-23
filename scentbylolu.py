import streamlit as st
import stripe
# App title
st.title("Perfume Shop")

# Contact Information
st.sidebar.title("Contact Us")
st.sidebar.write("Phone: +234 123 456 7890")
st.sidebar.write("Email: info@perfumeshop.com")
st.sidebar.write("Address: 123 Perfume Street, Abuja, Nigeria")

# Order Form
st.header("Place Your Order")
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
address = st.text_area("Delivery Address")
perfume = st.selectbox("Select Perfume", ["Perfume A", "Perfume B", "Perfume C"])
quantity = st.number_input("Quantity", min_value=1, max_value=10, step=1)
payment_method = st.selectbox("Payment Method", ["Credit Card", "Debit Card", "PayPal"])

if st.button("Submit Order"):
    st.success("Order placed successfully!")


st.header("Payment")
if st.button("Proceed to Payment"):
    try:
        session = stripe.checkout.Session.create( 
            payment_method_types=['card'], 
            line_items=[{ 
                'price_data': { 
                    'currency': 'ngn', 
                    'product_data': { 
                        'name': perfume, 
                    }, 
                    'unit_amount': [perfume]["price"] * 100, 
                }, 
                'quantity': quantity, 
          }],
          mode='payment',
          success_url='https://your-success-url.com', 
          cancel_url='https://your-cancel-url.com', 
        ) 
        st.write(f"Please complete your payment [here]({session.url})") 
    except Exception as e: 
        st.error(f"An error occurred: {e}")


# FAQs
st.header("Frequently Asked Questions")
faq1 = st.expander("What is the delivery time?")
faq1.write("Delivery time is 3-5 business days within Nigeria.")
faq2 = st.expander("What payment methods are accepted?")
faq2.write("We accept Credit Card, Debit Card, and PayPal.")
faq3 = st.expander("Can I return a product?")
faq3.write("Yes, you can return a product within 30 days of purchase.")

# Run the app
if __name__ == "__main__":
    st.run()
