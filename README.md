# Bizcard_Extraction

BizCardX: Extracting Business Card Data with OCR

Problem Statement-
You have been tasked with developing a Streamlit application that allows users to upload an image of a business card and 
extract relevant information from it using easyOCR. The extracted information should include the company name, card holder 
name, designation, mobile number, email address, website URL, area, city, state, and pin code. The extracted information 
should then be displayed in the application's graphical user interface (GUI). In addition, the application should allow 
users to save the extracted information into a database along with the uploaded business card image. The database should 
be able to store multiple entries, each with its own business card image and extracted information. To achieve this, you 
will need to use Python, Streamlit, easyOCR, and a database management system like SQLite or MySQL.

Technologies used-
Python
Streamlit
Pandas
EasyOCR
SQLite

Approach

1.Set up a Streamlit application using the python library streamlit, which allows users to upload business card image.
2.Read the image using easyocr and store the extracted data in the database.
3.Allow the user to view all the inserted business card data.
4.Use SQL queries to edit or delete the data.
