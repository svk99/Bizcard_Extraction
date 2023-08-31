import pandas as pd
import streamlit as st
import easyocr
from PIL import Image
import numpy as np
import sqlite3

conn=sqlite3.connect('bizcard.db')
c=conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS business_card (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        designation TEXT,
        address TEXT,
        pincode VARCHAR(25),
        phone VARCHAR(25),
        email TEXT,
        website TEXT,
        company TEXT)
''')

st.subheader('Business Card Reader')

t1,t2,t3,t4=st.tabs(['Upload','View','Edit','Delete'])
with t1:
    uploaded_image=st.file_uploader('Upload the image',type=['png','jpg'])
    if uploaded_image is not None:
        image=Image.open(uploaded_image)
        image_np=np.array(image)
        st.image(image,caption='Uploaded Image')
        reader=easyocr.Reader(['en'])
        text=reader.readtext(image_np)
        if st.button('Upload details'):
            c.execute('''
            INSERT INTO business_card (name,designation,address,pincode,phone,email,website,company)
            values (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (text[0][1], text[1][1], text[2][1], text[3][1], text[4][1], text[5][1], text[6][1], text[7][1]))
            conn.commit()
            st.success("Card Data Inserted")

with t2:
    st.subheader('Viewing business cards data')
    c.execute('Select * from business_card')
    data=c.fetchall()
    df=pd.DataFrame(data,columns=['id', 'name', 'position', 'address', 'pincode', 'phone', 'email', 'website', 'company'])
    st.table(df)

with t3:
    st.subheader('Edit the business card data')
    id=st.number_input('Select a id to edit or delete',min_value=1,step=1,key='a')
    if id in [row[0] for row in data]:
        name=st.text_input('Name',data[id-1][1])
        desn=st.text_input('Designation',data[id-1][2])
        address=st.text_input('Address',data[id-1][3])
        pincode=st.text_input('Pincode',data[id-1][4])
        phone=st.text_input('Phone',data[id-1][5])
        email=st.text_input('Email',data[id-1][6])
        website=st.text_input('Website',data[id-1][7])
        company=st.text_input('Company',data[id-1][8])

        if st.button('Update the record'):
            try:
                update_query = "Update business_card set name=?,designation=?,address=?,pincode=?,phone=?,email=?,website=?,company=? where id=?"
                c.execute(update_query,(name,desn,address,pincode,phone,email,website,company,id))
                conn.commit()
                st.success('Data updated')
            except:
                st.error('Some error occured')

with t4:
    st.subheader('Delete the business card data')
    id = st.number_input('Select a id to edit or delete', min_value=1, step=1,key='b')
    if id in [row[0] for row in data]:
        if st.button('Delete'):
            delete_query=("Delete from business_card where id=?")
            try:
                c.execute(delete_query,(id,))
                conn.commit()
                st.success('Data deleted')
            except:
                st.error('Some error occured')