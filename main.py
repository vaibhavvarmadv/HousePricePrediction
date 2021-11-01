# Importing Pickle and streamlit
import pickle
from sklearn.linear_model import LinearRegression
import streamlit as st

# opening the pickle file and loading it.
pickle_file = open('house_pred.pkl','rb')
pickle_model = pickle.load(pickle_file)

# defining a function that takes in the required inputs for the price prediction
def house_price_pred():
    # Title attribute is being used
    st.title("House Price Prediction")
    # inputs are being fetched from the user
    name = st.text_input('Name ', '')
    sqft_living = st.number_input('Square Ft Living ',0,10000)
    sqft_living15 = st.number_input('Nearest 15 Square Ft Living', 0,100000)
    grade = st.number_input("Grade of the House(1-13 Scale)",1,13)
    yr_built = st.number_input('Year Built ', 1950,2021)
    bathrooms = st.number_input('No of bathrooms',0,10) 
    view = st.selectbox("View",('Yes', 'No'))
    waterfront = st.selectbox("Waterfront",('Yes', 'No'))
    
    # changing the text to number so that we can feed into the model
    # View and Waterfront convertion to 0,1
    if view.lower() == 'yes':
        view = 1
    elif view.lower() == 'no' :
        view = 0
        
    if waterfront.lower() == 'yes':
        waterfront = 1
    elif waterfront.lower() == 'no':
        waterfront = 0
    # using the model to predict the house price and round it out 
    output = pickle_model.predict([[waterfront, bathrooms, sqft_living, grade, yr_built,view,sqft_living15]])
    house_price =  round(output[0], 2)
    
    # using a button to output the price
    if st.button("Find"):
        st.success(f"Hello {name} !, the expected price of the house with the above specification is $ {house_price}")        

if __name__ == "__main__":
    house_price_pred()
