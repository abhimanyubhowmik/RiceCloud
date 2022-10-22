import streamlit as st 
from PIL import Image
import imagePreprocessing as imP
import cnn
import ensemble
import Logging

log = Logging.app_logging()


im = Image.open("App/favicon.png")
st.set_page_config(
page_title="Rice Cloud",
page_icon=im,
layout="wide",
initial_sidebar_state="expanded",
menu_items={
        "Get Help": "https://github.com/abhimanyubhowmik/Machine-Learning-Model-Visualizer",
        "Report a bug": "https://github.com/abhimanyubhowmik/Machine-Learning-Model-Visualizer/issues",
        "About": "### RiceCloud Application for the research article titled 'RiceCloud: A Cloud integrated Ensemble learning based Rice leaf Diseases prediction System' \n :copyright: Abhimayu Bhowmik \n\n Github: https://github.com/abhimanyubhowmik \n\n Linkedin: https://linkedin.com/in/bhowmikabhimanyu ",
    }
)

st.title('Rice Cloud')

st.markdown('Upload or take a picture of an infected Rice Leaf image and get predictions for the Disease.')
st.text(" ")
st.text(" ")
st.text(" ")
st.text(" ")

images = []

uploaded_files = st.file_uploader("Upload one or multiple images", accept_multiple_files=True, type=['png', 'jpg','jpeg'])
for uploaded_file in uploaded_files:
     image = Image.open(uploaded_file)
     images.append(image)
     st.image(image, caption=uploaded_file.name)



picture = st.camera_input("Or take a picture")

if picture:
     st.image(picture)


if st.button('Predict'):
    with st.spinner('Wait for it...'):
        dataset = imP.LeafDataset(uploaded_files)
        model_vgg = cnn.vgg16(dataset)
        x_test = model_vgg.test_data()
        model_lgbm = ensemble.lgbm(x_test)
        st.header('Results:')
        output = model_lgbm.predict()
    # for i,uploaded_file in enumerate(uploaded_files):
    #     image = Image.open(uploaded_file)
    #     st.image(image, caption= output[i])


    # for uploaded_file in uploaded_files:
    #     image = Image.open(uploaded_file)
    #     images.append(image)
    #     st.image(image, caption='Result : Brown Spot')