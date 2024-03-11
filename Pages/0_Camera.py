
import streamlit as st

import utils as ut

IMAGE_NAME = "cam.jpg"


if 'lang' not in st.session_state:
    st.session_state.lang = "en"


with st.sidebar:
    option = st.selectbox("Please select a language",("English", "Spanish"))
    if option == "Spanish":
        st.session_state.lang = "sp"
    elif option == "English":
        st.session_state.lang = "en"

# set title
st.title(ut.translate("sent2", st.session_state.lang))

#camera input
cam_image = st.camera_input(ut.translate("sent3", st.session_state.lang))

if cam_image:

    st.header(ut.translate("sent4", st.session_state.lang))
    # displaying the image
    st.image(cam_image)

    # save the image
    with open (IMAGE_NAME,'wb') as file:
          file.write(cam_image.getbuffer())

    # get the base64 version
    payload = ut.encoder(IMAGE_NAME)

    # get prediction
    response_index = ut.get_prediction(payload)

    # predicted labels
    st.subheader("{}: ".format(ut.translate("sent9", st.session_state.lang)) + ut.get_label(response_index, st.session_state.lang))
