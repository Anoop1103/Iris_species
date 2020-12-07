

from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
model = load_model('Iris_final')



def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    from PIL import Image
    image = Image.open('iris.jpg')
    image_office = Image.open('office.jpg')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict the species of Iris flower')
    st.sidebar.success('https://www.pycaret.org')
    st.sidebar.image(image_office)
    st.title("Predicting employee leaving")
    if add_selectbox == 'Online':
        sepal_length = st.number_input('sepal_length' , min_value=4.6, max_value=7.1, value=0.1)
        sepal_width = st.number_input('sepal_width',min_value=2.3, max_value=3.6, value=0.1)
        petal_length = st.number_input('petal_length', min_value=1.3, max_value=6, value=0.1)
        petal_width = st.number_input('petal_width', min_value=0.2, max_value=2.5, value=0.1)
        output=""
        input_dict={'sepal_length':sepal_length,'sepal_width':sepal_width,'petal_length':petal_length,'petal_width':petal_width}                  
        input_df = pd.DataFrame([input_dict])
        if st.button("Predict species"):
            output = predict(model=model, input_df=input_df)
            output = str(output)
        st.success('The output is {}'.format(output))
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
