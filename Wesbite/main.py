import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image
import pickle
from our_model import our_model 
from meet_the_team import meet_the_team
from history import history
# from matplotlib.pyplot import imread
# from matplotlib.pyplot import imshow
# from tensorflow.keras.models import load_model
# from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.imagenet_utils import decode_predictions
# from tensorflow.keras.applications.imagenet_utils import preprocess_input
# from flask import Flask, render_template

# Set the color scheme
PRIMARY_COLOR = "#81D4FA"
SECONDARY_COLOR = "#A5D6A7"
ACCENT_COLOR = "#FFE0B2"
TEXT_COLOR = "#616161"
BACKGROUND_COLOR = "#FAFAFA"

# app = Flask(__name__)

# @app.route('/results')
# def results():
#     # subheader 1
#     section1_data = [
#         {"description": "Based on our model,  you may have cancer."}
#     ]
#     # subheader 2
#     section2_data = [
#         {"description": "We understand this may be concerning news. We advise that you go to a medical professional to get checked out as soon as possible. It is important to follow their recommendations, which may include further diagnostic tests,  consultations with specialists, and  discussing potential treatment options. Early detection and intervention are crucial for the best possible outcomes."}
#     ]
#     return render_template('results.html', section1_data=section1_data, section2_data=section2_data)

# GLOBAL variables
# loaded_model = pickle.load(open('trained_model.sav', 'rb'))
uploaded_file = None

def make_prediction():
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        
    img = np.array(img)
    img = cv2.resize(img, (100, 100))

    x = np.expand_dims(img, axis=0)
    x = preprocess_input(x)
    result = loaded_model.predict(x)
    print((result*100).astype('int'))

    p = list((result*100).astype('int'))
    pp=list(p[0])
    print(pp)

    index = pp.index(max(pp))

    name_class = ['BCC', 'ACK', 'NEV', 'SEK', 'SCC', 'MEL']

    st.subheader(name_class[index])

    uploaded_file = None

def upload():
    st.title('Skin Lesion Detection', anchor=False)
    st.markdown(
        f"""
        <style>
        .title h1 {{
            color: {PRIMARY_COLOR};
            font-family: 'Arial', sans-serif;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.write(
        "Welcome to the Skin Lesion Detection app! Upload an image of a skin lesion and we'll analyze it for you.",
        unsafe_allow_html=True
    )

    # Upload image
    uploaded_file = st.file_uploader("Upload a skin lesion image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption='Uploaded Image', width=300)

        # Add rest of the code here!!

    if st.button("Evaluate image"):
        if uploaded_file is None:
            st.subheader("Error: Please upload an image")
        else:
            st.session_state.page = "buffer"
            st.experimental_rerun()


def buffer():
        st.title("Your results: ")
        if st.button("Show results"):
            st.session_state.page = "results"
            st.experimental_rerun()

        st.subheader("Disclaimer: ")
        st.write("This model is not fully accurate and we only intend this to be a preliminary prediction. Please consult a doctor if there are any concerns.")

def results():
    st.title("Prediction: ")

    # subheader 1
    st.write("Based on our model,  you may have ")

    make_prediction()
    # subheader 2
    st.write("We understand this may be concerning news. We advise that you go to a medical professional to get checked out as soon as possible. It is important to follow their recommendations, which may include further diagnostic tests,  consultations with specialists, and  discussing potential treatment options. Early detection and intervention are crucial for the best possible outcomes.")

    if st.button("Back to Home"):
        st.session_state.page = "upload"
        st.experimental_rerun()

def home():
    # Initialize session state if not already done
    if 'page' not in st.session_state:
        st.session_state.page = "upload"

    # Page routing logic
    if st.session_state.page == "upload":
        upload()
    elif st.session_state.page == "buffer":
        buffer()
    elif st.session_state.page == "results":
        results()

    # Footer
    st.write("___")
    st.write("© 2024 GDSC Link. All rights reserved.")

def main():
    st.markdown(
        f"""
        <style>
        .css-18e3th9 {{
            background-color: {BACKGROUND_COLOR};
        }}
        .css-1d391kg {{
            color: {TEXT_COLOR};
            font-family: 'Arial', sans-serif;
        }}
        .css-1v3fvcr {{
            color: {TEXT_COLOR};
            font-family: 'Arial', sans-serif;
        }}
        .stButton > button {{
            background-color: {PRIMARY_COLOR};
            color: white;
            border-radius: 5px;
            font-family: 'Arial', sans-serif;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set page title and description
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Home", "Our Model", "About Us", "History"],
            icons=["house", "gear", "people-fill", "clock-history"],
            menu_icon="cast",
            default_index=0,
            styles={
                "nav-link-selected": {"background-color": PRIMARY_COLOR, "color": "white"},
                "nav-link": {"font-family": "Arial, sans-serif", "color": TEXT_COLOR}
            }
        )


    # Defining each page
    if selected == "Home":
        home()

    elif selected == "Our Model":
        our_model()

    elif selected == "About Us":
        meet_the_team()

    elif selected == "History":
        history()

if __name__ == '__main__':
    main()


#     [theme]
# primaryColor="#76bdb1"
# backgroundColor="#e3e3dc"
# secondaryBackgroundColor="#5b5d6f"
# textColor="#0077e5"