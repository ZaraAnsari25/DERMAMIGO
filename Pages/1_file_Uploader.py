
import streamlit as st
from PIL import Image
import io
import base64

import utils as ut


if 'lang' not in st.session_state:
    st.session_state.lang = "en"


with st.sidebar:
    option = st.selectbox("Please select a language",("English", "Spanish"))
    if option == "Spanish":
        st.session_state.lang = "sp"
    elif option == "English":
        st.session_state.lang = "en"

# set title
st.title(ut.translate("sent8", st.session_state.lang))

# file uploader
#file uploader
file_image = st.file_uploader(
    label = ut.translate("sent6", st.session_state.lang),
    accept_multiple_files = False,
    help = ut.translate("sent7", st.session_state.lang)
    )
if file_image:
    # display the image
    st.image(file_image)
    #converting the image to bytes
    img = Image.open(file_image)
    buf = io.BytesIO()
    img.save(buf,format = 'png')
    byte_im = buf.getvalue()

    #converting bytes to b64encoding
    payload = base64.b64encode(byte_im)

    # get predictions
    pred_index = ut.get_prediction(payload)

    # predicted labels
    st.subheader("{}: ".format(ut.translate("sent9", st.session_state.lang)) + ut.get_label(pred_index, st.session_state.lang))
