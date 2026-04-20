import streamlit as st

st.title("Input Your Information",anchor=False)

st.divider()

name = st.text_input("Enter your name:")

print(type(name))

st.divider()

age = st.number_input("Enter your age:", min_value=0, max_value=120,step=1,value=None,placeholder = "Enter your age")  

print(type(age))


st.divider()

selected_profession = st.selectbox("Choose your profession:", options=["Engineer", "Doctor", "Teacher", "Artist"],
                                   index=None,accept_new_options= True)

print(type(selected_profession))

st.write(f"Your selected profession is : {selected_profession}")

# password = st.text_input("Enter your password : ", type = "password")

pressed = st.button("Submit")

if pressed:
    st.write(f"Your Name is : {name}, Your age is : {age} ")
    
    


  