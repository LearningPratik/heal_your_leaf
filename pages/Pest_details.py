import streamlit as st

st.set_page_config(page_title="Pest Details")

st.sidebar.header("Pest Details")


option = st.selectbox("## Select disease",
                     ("", "late blight", "easy blight", "healthy"))
if option == "late blight":
    st.header(":green[Late blight]")

    st.image('D:/DeepLearning/PyTorch/DiseaseDetection/Images/late_blight.JPG', caption='Late blight')

    st.subheader("Symptoms")
    st.write('''
        * Infected potato plants may exhibit large :red[brown blotches] with a :red[green-gray edge] on their leaves.\n
        * The disease can also cause tubers to rot within two weeks.\n
        * The symptoms resemble those of other diseases, making identification challenging. 
        ''')

    st.subheader("Preventive Measures")
    st.markdown('Preventing potato late blight requires a combination of cultural, chemical, and biological controls. These include:')
    st.write('''
        * **Crop rotation:** Rotate potato crops with non-solanaceous crops to break the disease cycle.\n
        * **Sanitation:** Remove infected plants and cull piles to prevent the spread of the disease.\n
        * **Fungicides:** Apply fungicides as needed to prevent infection.\n
        * **Biological control:** Use biological control agents such as Trichoderma harzianum to suppress the pathogen.
        ''')
    
elif option == 'easy blight':
    st.header(":green[Early blight]")

    st.image('D:/DeepLearning/PyTorch/DiseaseDetection/Images/early_blight.JPG', caption='Early blight')

    st.subheader("Symptoms")
    st.write('''
        * Early symptoms of potato early blight begin as pinpoint :red[brown or black spots] on the lower (older) leaves.\n
        * These spots can grow and merge to form larger, irregularly-shaped lesions with concentric rings, often resembling a “bull’s eye” pattern.
        ''')
    
    st.subheader("Preventive Measures")
    st.write('''
        * Early blight can be controlled using organic and natural methods. 
        * These include removing infected plants, improving air circulation, and using resistant varieties of potatoes and tomatoes. 
        * Chemical controls are also available, but these can have negative environmental impacts and should be used sparingly.
        ''')
elif option == 'healthy':
    st.header("Healthy Potato leaf sample")
    st.image('D:/DeepLearning/PyTorch/DiseaseDetection/Images/healthy.JPG', caption='Healthy leaf')

else:
    st.markdown('Selection any option to see information')