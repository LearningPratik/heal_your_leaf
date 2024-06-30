import re
import torch
import warnings
from PIL import Image
import streamlit as st

from util import Classifier

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False


# set title
st.title("Disease Detection")
st.sidebar.header("Check Image")

# set header
st.header("Please upload a image of potato leaf")

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png', 'jfif'])

# load model
model_path = './models/model_1_scripted.pt'
model = torch.jit.load(model_path)

# load class names
with open('./labels.txt', 'r') as f:
    class_names = []
    for i in f.readlines():
        class_name = i.split(' ')[1]
        class_name = re.sub('\n', '', class_name)
        class_names.append(class_name)
    # class_names = [i.split(' ')[1] for i in f.readlines()]
    f.close()
# class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

print(class_names)

# display image
if file is not None:
    image = Image.open(file)
    st.image(image, use_column_width=True)


    # classify image
    class_name = Classifier(image, model, class_names)

    # write predictions
    # st.write('## {}'.format(class_name))

    if class_name == 'healthy':
        st.write(f'## Class for the uploaded image is :green[{class_name}]')
    else:
        st.write(f'## Class for the uploaded image is :red[{class_name}] get its details from Pest Details section')