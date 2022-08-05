import streamlit as st

st.title('Welcome to BMI Calculator')
st.write('''
### hello!!!! do you know your BMI??
''')
status = st.radio("Select Gender: ", ('Male', 'Female'))

if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

weight = st.number_input("Enter your weight in Kg")

status = st.radio('Select your height format: ',
                  ('cms', 'meters'))

if (status == 'cms'):

    height = st.number_input('Enter your height')

    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter some value of height")

elif (status == 'meters'):

    height = st.number_input('Meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")

if (st.button('Calculate BMI')):

    st.text("Your BMI is {}.".format(bmi))

    if (bmi < 16):
        st.error("You are Extremely Underweight")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif (bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif (bmi >= 30):
        st.error("Extremely Overweight")
