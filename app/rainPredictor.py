import streamlit as st
from additional_info import locations, directions


class Form:
    def __init__(self):
        self.location = st.selectbox('Location', options=locations)
        self.minTemp = st.number_input('The minimum temperature in degrees celsius', min_value=-100.0, max_value=100.0,
                                       value=0.0, step=1.0)
        self.maxTemp = st.number_input('The maximum temperature in degrees celsius', min_value=-100.0, max_value=100.0,
                                       value=0.0, step=1.0)
        self.rainfall = st.number_input('The amount of rainfall recorded for the day in mm', min_value=0.0, value=0.0,
                                        step=0.1)
        self.evaporation = st.number_input('The so-called Class A pan evaporation (mm) in the 24 hours to 9am',
                                           min_value=0.0, value=0.0, step=0.1)
        self.sunshine = st.number_input('The number of hours of bright sunshine in the day', min_value=0.0, value=0.0,
                                        step=0.1)
        self.windGustDir = st.selectbox('The direction of the strongest wind gust in the 24 hours to midnight',
                                        options=directions)
        self.windGustSpeed = st.number_input('The speed (km/h) of the strongest wind gust in the 24 hours to midnight',
                                             min_value=0.0, value=0.0, step=0.1)
        self.windDir9am = st.selectbox('Direction of the wind at 9am', options=directions)
        self.windDir3pm = st.selectbox('Direction of the wind at 3pm', options=directions)
        self.windSpeed9am = st.number_input('Wind speed (km/hr) averaged over 10 minutes prior to 9am', min_value=0.0,
                                            value=0.0, step=0.1)
        self.windSpeed3pm = st.number_input('Wind speed (km/hr) averaged over 10 minutes prior to 3pm', min_value=0.0,
                                            value=0.0, step=0.1)
        self.humidity9am = st.number_input('Humidity (percent) at 9am', min_value=0.0, value=0.0, step=0.1)
        self.humidity3pm = st.number_input('Humidity (percent) at 3pm', min_value=0.0, value=0.0, step=0.1)
        self.pressure9am = st.number_input('Atmospheric pressure (hpa) reduced to mean sea level at 9am', min_value=0.0,
                                           value=0.0, step=0.1)
        self.pressure3pm = st.number_input('Atmospheric pressure (hpa) reduced to mean sea level at 3pm', min_value=0.0,
                                           value=0.0, step=0.1)
        self.cloud9am = st.number_input('Fraction of sky (oktas) obscured by cloud at 9am', min_value=0, max_value=8,
                                        value=0, step=1)
        self.cloud3pm = st.number_input('Fraction of sky (oktas) obscured by cloud at 3pm', min_value=0, max_value=8,
                                        value=0, step=1)
        self.temp9am = st.number_input('Temperature (degrees C) at 9am', min_value=-100.0, max_value=100.0, value=0.0,
                                       step=0.1)
        self.temp3pm = st.number_input('Temperature (degrees C) at 3pm', min_value=-100.0, max_value=100.0, value=0.0,
                                       step=0.1)
        self.rainToday = st.checkbox(
            'Is the amount of precipitation (mm) in the 24 hours before 9 am greater than 1 mm?')
        self.submit = st.button('Predict')


def main():
    st.title('Weather Prediction 🌦')

    form = Form()

    if form.submit:
        try:
            result = form.rainToday
            # waiting for the model
            st.write(f"Predicted Result: {result}")
        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
