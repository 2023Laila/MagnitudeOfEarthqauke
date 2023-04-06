
import numpy as np
import pandas as pd
import joblib 
import streamlit as st

reg = joblib.load('magnitude1.pkl')

def predict_mag_Earthquake(latitude,longitude,rms,magType,locationSource,magSource):
    prediction = reg.predict(pd.DataFrame({'latitude':[latitude],'longitude':[longitude],'rms':[rms],'magType':[magType],'locationSource':[locationSource],'magSource':[magSource]}))
    return prediction

def main():
    st.title('Earthquake magnitude prediction')
    html_temp="""
                <div style="background-color:red">
                <h2 style="color:white;text-align:center;">this our first streamlit application </h2>
                </div>
              """
    st.markdown(html_temp,unsafe_allow_html=True)
    latitude = st.text_input('latitude','put the latitude of the Earthquake')
    longitude= st.text_input('longitude','put the longitude of the Earthquake')
    rms = st.text_input('rms','put the rmsof the Earthquake')
    magType= st.selectbox('magType',['md','mb','ml','mw','ms','mh','m','mc'])
    locationSource= st.selectbox('locationSource',['us','ak','guc','nc','buc','tx','tul'])
    magSource= st.selectbox('magSource',['us','ak','guc','nc','buc','tx','tul'])
    result = ""
    if st.button('predict'):
        result =predict_mag_Earthquake(latitude,longitude,rms,magType,locationSource,magSource)
    st.success('the Earthquake magnitude is {}'.format(result))  
    
        
if __name__=='__main__':
    main()



