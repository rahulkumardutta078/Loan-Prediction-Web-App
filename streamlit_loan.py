
from cProfile import label
import streamlit as st 
import pandas as pd 
import pickle
import sklearn
import plotly.graph_objects as go



loan_prediction_model=pickle.load(open('loan_prediction.pickle','rb'))


def predict(Gender,Married,Dependents,Education,Self_Employed,Applicant_Income,CoapplicantIncome,LoanAmount,LoanAmountTerm,Credit_History,Property_Area):
    prediction=loan_prediction_model.predict([[Gender,Married,Dependents,Education,Self_Employed,Applicant_Income,CoapplicantIncome,LoanAmount,LoanAmountTerm,Credit_History,Property_Area]])

    if prediction==0:
        score="approved"
        return score

    else:
        score="not be approved"
        return score




def main():
    st.title("Loan Prediction Web App")

    Gender=st.selectbox("Gender",(0,1))

    Married=st.selectbox("Married",(0,1))

    Dependents=st.selectbox("Dependents",(0,1,2,3))

    Education=st.selectbox("Education",(0,1))

    Self_Employed=st.selectbox("Self_Employed",(0,1))

    Applicant_Income=st.text_input("Applicant_Income")

    CoapplicantIncome=st.text_input("CoapplicantIncome")

    LoanAmount=st.text_input("LoanAmount")

    LoanAmountTerm=st.text_input("Loan_Amount_Term")

    Credit_History=st.selectbox("Credit_History",(0,1))

    Property_Area=st.selectbox("Property_Area",(0,1,2))

    result=""

    if st.button("Predict"):
        result=predict(Gender,Married,Dependents,Education,Self_Employed,Applicant_Income,CoapplicantIncome,LoanAmount,LoanAmountTerm,Credit_History,Property_Area)

        st.success("Loan will be {}".format(result))




if __name__ == '__main__':
    import seaborn as sns
    import matplotlib.pyplot as plt

    df=pd.read_csv(r'C:\Users\RAHUL KUMAR DUTTA\OneDrive\Desktop\Documents\Loan Prediction\loan_prediction_dataset.csv')
    
    main()
    
    #fig=plt.figure(figsize=(4,2))
    #val_gender_count=df['Gender'].value_counts()

    #sns.barplot(val_gender_count.index,val_gender_count.values,alpha=0.8)
    #st.pyplot(fig)

    #st.bar_chart(df['Married'])

    #st.bar_chart(df['Loan_Status'])

    #st.bar_chart(df['Education'])

    #st.bar_chart(df['Self_Employed'])

    #st.bar_chart(df['Gender'],df['LoanAmount'])

    #st.bar_chart(df['Property_Area'])

    #st.bar_chart(df['Gender'],label='Loan_Status')
    

    #st.bar_chart(df['Married'],label='Loan_Status')

    #st.bar_chart(df['Education'],label='Loan_Status')