import streamlit as st
import pandas as pd
# from big-mart-sales-prediction.ipynb import predict   # replace with your actual model file and function

def main():
    st.title("Big Mart Sales Prediction")
    
    # Input fields
    item_weight = st.number_input('Item Weight')
    item_fat_content = st.selectbox('Item Fat Content', ['Low Fat', 'Regular'])
    item_visibility = st.number_input('Item Visibility')
    item_type = st.selectbox('Item Type', ['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables', 'Household', 'Baking Goods', 'Snack Foods', 'Frozen Foods', 'Breakfast', 'Health and Hygiene', 'Hard Drinks', 'Canned', 'Breads', 'Starchy Foods', 'Others', 'Seafood'])
    item_mrp = st.number_input('Item MRP')
    
    # When 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        input_data = {'Item_Weight': item_weight, 
                      'Item_Fat_Content': item_fat_content, 
                      'Item_Visibility': item_visibility, 
                      'Item_Type': item_type, 
                      'Item_MRP': item_mrp}
        input_df = pd.DataFrame([input_data])
        result = predict_sales(input_df)
        st.success(f'The predicted sales are {result}')

if __name__ == '__main__':
    main()
