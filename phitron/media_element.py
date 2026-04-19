import streamlit as st

st.title("Input Media",anchor=False)

st.divider()

images = st.file_uploader("Upload your Image", type=["jpg", "jpeg", "png"],
                         accept_multiple_files=True)

print(type(images))

if images:
    col = st.columns(len(images)) 
    
    for i, per_image in enumerate(images):
        with col[i]:
            st.image(per_image) 