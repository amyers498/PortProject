import streamlit as st

# Title
st.title('Login')

# Username
username = st.text_input('Username')

# Password
password = st.text_input('Password', type='password')

# Login button
if st.button('Login'):
  if username == 'admin' and password == 'admin':
    st.redirect('upload.py')              ## I need to figure this out 
  else:
    st.write('Invalid username or password.')