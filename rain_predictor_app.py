import streamlit as st
from app.additional_info import locations, directions
import pickle
from model.encoders import LabelEncoder

with open("pkl/model.pkl", 'rb') as file:
    model = pickle.load(file)

with open("pkl/scaler.pkl", 'rb') as file:
    scaler = pickle.load(file)


class Form:
    def __init__(self):
        self.location = st.selectbox('Location 🌏', options=locations)
        self.minTemp = st.number_input('🌡️ The minimum temperature in degrees celsius', min_value=-100.0,
                                       max_value=100.0,
                                       value=0.0, step=1.0)
        self.maxTemp = st.number_input(' 🌡️The maximum temperature in degrees celsius', min_value=-100.0,
                                       max_value=100.0,
                                       value=0.0, step=1.0)
        self.rainfall = st.number_input('⛈️ The amount of rainfall recorded for the day in mm', min_value=0.0,
                                        value=0.0,
                                        step=0.1)

        self.sunshine = st.number_input('⛈️ The number of hours of bright sunshine in the day', min_value=0,max_value=24,
                                        value=0,
                                        step=1)
        self.windGustDir = st.selectbox('🌪️ The direction of the strongest wind gust in the 24 hours to midnight',
                                        options=directions)
        self.windGustSpeed = st.number_input(
            '🌪️ The speed (km/h) of the strongest wind gust in the 24 hours to midnight',
            min_value=0.0, value=0.0, step=0.1)
        self.windDir9am = st.selectbox('💨 Direction of the wind at 9am', options=directions)
        self.windDir3pm = st.selectbox('💨 Direction of the wind at 3pm', options=directions)
        self.windSpeed9am = st.number_input('🌬 Wind speed (km/hr) averaged over 10 minutes prior to 9am', min_value=0.0,
                                            value=0.0, step=0.1)
        self.windSpeed3pm = st.number_input('🌬 Wind speed (km/hr) averaged over 10 minutes prior to 3pm', min_value=0.0,
                                            value=0.0, step=0.1)
        self.humidity9am = st.number_input('💦 Humidity (percent) at 9am', min_value=0.0, value=0.0,max_value=100.0, step=0.1)
        self.humidity3pm = st.number_input('💦 Humidity (percent) at 3pm', min_value=0.0, value=0.0,max_value=100.0, step=0.1)
        self.pressure9am = st.number_input('💭 Atmospheric pressure (hpa) reduced to mean sea level at 9am',
                                           min_value=0.0,
                                           value=0.0, step=0.1)
        self.pressure3pm = st.number_input('💭 Atmospheric pressure (hpa) reduced to mean sea level at 3pm',
                                           min_value=0.0,
                                           value=0.0, step=0.1)
        self.cloud9am = st.number_input('🌫 Fraction of sky (oktas) obscured by cloud at 9am', min_value=0.0, max_value=8.0,
                                        value=0.0, step=0.1)
        self.cloud3pm = st.number_input('🌫 Fraction of sky (oktas) obscured by cloud at 3pm', min_value=0.0, max_value=8.0,
                                        value=0.0, step=0.1)
        self.temp9am = st.number_input('🌡 Temperature (degrees C) at 9am', min_value=-100.0, max_value=100.0, value=0.0,
                                       step=0.1)
        self.temp3pm = st.number_input('🌡 Temperature (degrees C) at 3pm', min_value=-100.0, max_value=100.0, value=0.0,
                                       step=0.1)
        self.rainToday = st.checkbox(
            'Is it raining today?(Is the amount of precipitation (mm) in the 24 hours before 9 am greater than 1 mm?)')
        self.submit = st.button('Predict')


def main():
    st.title('🇦🇺  Rain in Australia Prediction ⛅')

    form = Form()

    if form.submit:
        try:
            encoder = LabelEncoder()
            encoder.fit(locations, "Location")
            encoder.fit(directions, "WindGustDir")
            encoder.fit(directions, "WindDir9am")
            encoder.fit(directions, "WindDir3pm")

            data = [
                encoder.transform([form.location], "Location")[0],
                form.minTemp,
                form.maxTemp,
                form.rainfall,
                form.sunshine,
                encoder.transform([form.windGustDir], "WindGustDir")[0],
                form.windGustSpeed,
                encoder.transform([form.windDir9am], "WindDir9am")[0],
                encoder.transform([form.windDir3pm], "WindDir3pm")[0],
                form.windSpeed9am,
                form.windSpeed3pm,
                form.humidity9am,
                form.humidity3pm,
                form.pressure9am,
                form.pressure3pm,
                form.cloud9am,
                form.cloud3pm,
                form.temp9am,
                form.temp3pm,
                1 if form.rainToday else 0
            ]

            scaled = scaler.transform(data)

            result = model.predict([scaled])[0]

            if result:
                st.subheader(f"It will rain in {form.location} tomorrow.Don't forget to take an umbrella ☔")
            else:
                st.subheader(f"It won't rain in {form.location} tomorrow. 🌅")
        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
