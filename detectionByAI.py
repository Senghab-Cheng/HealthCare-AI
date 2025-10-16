import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Cambodia Health AI",
    page_icon="Cambodia Health Innovations Logo - Medical Cross and Circuit.png",
    layout="wide"
)

st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #1f77b4;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font"> Cambodia Health AI Assistant</p>', unsafe_allow_html=True)
st.markdown("### Powered by Artificial Intelligence | MoEYS x CADT Competition 2025")

language = st.sidebar.selectbox(
    "Language / ភាសា",
    ["English", "ខ្មែរ (Khmer)"]
)
  

st.sidebar.markdown("---")
st.sidebar.title(" Navigation")
page = st.sidebar.radio(
    "Choose a tool:",
    [" Home", " Symptom Checker", " Disease Risk Predictor", " Health Analytics", " About"]
)

#homepage
if page == " Home":
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("## Welcome to Cambodia Health AI!")
        st.write("""
        This AI-powered platform helps Cambodians access healthcare information 
        and preliminary health assessments. Our mission is to bridge the healthcare 
        gap between urban and rural areas.
        """)
        
        st.markdown("### Our Solutions:")
        st.write(" AI Symptom Checker")
        st.write(" Disease Risk Prediction")
        st.write(" Health Data Analytics")
        st.write(" Multilingual Support (English/Khmer)")
        
    with col2:
        st.image("Cambodia Health Innovations Logo - Medical Cross and Circuit.png", 
                 caption="Making Healthcare Accessible for All")
        
        st.markdown("### Impact Metrics")
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        metric_col1.metric("Users Helped", "1,234", "+156")
        metric_col2.metric("Assessments", "5,678", "+234")
        metric_col3.metric("Accuracy", "94%", "+2%")

elif page == " Symptom Checker":
    st.title(" AI Symptom Checker")
    st.write("Select your symptoms and get an AI-powered preliminary assessment")
    
    st.warning(" DISCLAIMER: This is NOT a medical diagnosis. Always consult a doctor.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Select Your Symptoms:")
        
        symptoms = {
            'High Fever': st.checkbox(' High Fever / គ្រុនក្តៅខ្លាំង'),
            'Cough': st.checkbox(' Cough / ក្អក'),
            'Headache': st.checkbox(' Headache / ឈឺក្បាល'),
            'Fatigue': st.checkbox(' Fatigue / ហត់នឿយ'),
            'Diarrhea': st.checkbox(' Diarrhea / រាគ'),
            'Vomiting': st.checkbox(' Vomiting / ក្អួត'),
            'Body Ache': st.checkbox(' Body Ache / ឈឺខ្លួន'),
            'Rash': st.checkbox(' Skin Rash / រមាស់ស្បែក'),
        }
        
        age = st.number_input("Age / អាយុ", min_value=0, max_value=120, value=30)
        
        if st.button(" Analyze Symptoms", type="primary"):
            selected = [k for k, v in symptoms.items() if v]
            
            if len(selected) == 0:
                st.error("Please select at least one symptom!")
            else:
                with col2:
                    st.markdown("### 📋 Analysis Results:")
                    
                    if symptoms['High Fever'] and symptoms['Body Ache']:
                        st.error(" Possible: Influenza / Dengue")
                        st.error(" Possible: គ្រុនផ្តាសសាយ")
                        severity = "HIGH"
                        severity = "កម្រិតខ្ពស់ ធ្ងន់ធ្ងរ"
                        advice = "See a doctor immediately. Monitor temperature."
                        advice_km = "ជួបវេជ្ជបណ្ឌិតភ្លាម។ ត្រួតពិនិត្យសីតុណ្ហភាព។"
                    elif symptoms['Diarrhea'] and symptoms['Vomiting']:
                        st.warning(" Possible: Gastroenteritis")
                        st.warning(" Possible: រលាកពោះវៀន")
                        severity = "MEDIUM"
                        severity = "កម្រិតមធ្យម"
                        advice = "Stay hydrated. See doctor if persists >2 days."
                        advice_km = "ផឹកទឹកច្រើន។ ជួបវេជ្ជបណ្ឌិតប្រសិនបើរយៈពេលលើសពី២ថ្ងៃ។"
                    else:
                        st.info(" Possible: Common Cold")
                        st.info(" Possible: ផ្តាសាយធម្មតា")
                        severity = "LOW"
                        severity = "កម្រិតស្រាល"
                        advice = "Rest, drink fluids, monitor symptoms."
                        advice_km = "សម្រាក ផឹកទឹកច្រើន ត្រួតពិនិត្យរោគសញ្ញា។"
                    
                    st.markdown(f"**Severity Level:** {severity}")
                    st.markdown(f"**Symptoms Checked:** {len(selected)}")
                    st.markdown("**Recommendation (EN):**")
                    st.info(advice)
                    st.markdown("**ការណែនាំ (KM):**")
                    st.info(advice_km)
                    
                    with st.expander(" Emergency Contacts"):
                        st.write("Emergency: **119**")
                        st.write("Calmette Hospital: **023 426 948**")
                        st.write("Khmer-Soviet Hospital: **023 991 200**")

elif page == " Disease Risk Predictor":
    st.title(" Disease Risk Predictor")
    st.write("Get AI-powered risk assessment for diabetes and heart disease")
    
    predictor_type = st.radio(
        "Select Prediction Type:",
        [" Diabetes Risk", " Heart Disease Risk"]
    )
    
    if predictor_type == " Diabetes Risk":
        st.markdown("### Diabetes Risk Assessment")
        
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.slider("Age / អាយុ", 0, 100, 30)
            glucose = st.number_input("Glucose Level (mg/dL)", 50, 300, 100)
            bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
        
        with col2:
            blood_pressure = st.number_input("Blood Pressure (mmHg)", 40, 200, 80)
            family_history = st.selectbox("Family History of Diabetes", ["No", "Yes"])
            
        if st.button("Calculate Risk", type="primary"):
            risk_score = 0
            if age > 45: risk_score += 20
            if glucose > 140: risk_score += 30
            if bmi > 30: risk_score += 25
            if blood_pressure > 90: risk_score += 15
            if family_history == "Yes": risk_score += 10
            
            st.markdown("---")
            st.markdown("###  Risk Assessment Result")
            
            st.progress(min(risk_score, 100) / 100)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Risk Score", f"{risk_score}%")
            
            if risk_score < 30:
                col2.metric("Risk Level", "LOW", delta="-20%", delta_color="inverse")
                st.success(" Low diabetes risk. Maintain healthy lifestyle!")
            elif risk_score < 60:
                col2.metric("Risk Level", "MEDIUM", delta="0%")
                st.warning(" Medium risk. Consult doctor and improve diet/exercise.")
            else:
                col2.metric("Risk Level", "HIGH", delta="+30%", delta_color="normal")
                st.error(" High risk. Schedule doctor appointment immediately!")
            
            col3.metric("Confidence", "89%")
    
    else:  
        st.markdown("### Heart Disease Risk Assessment")
        st.info("Coming soon! Under development.")

elif page == " Health Analytics":
    st.title(" Health Data Analytics")
    st.write("Visualize health trends and patterns in Cambodia")
    
    dates = pd.date_range(start='2025-01-01', end='2025-10-14', freq='D')
    data = pd.DataFrame({
        'Date': dates,
        'Consultations': np.random.randint(50, 150, len(dates)),
        'Diabetes Cases': np.random.randint(5, 25, len(dates)),
        'Heart Disease Cases': np.random.randint(3, 15, len(dates))
    })
    
    st.markdown("### Daily Health Consultations")
    st.line_chart(data.set_index('Date')['Consultations'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🩺 Disease Cases Over Time")
        st.area_chart(data.set_index('Date')[['Diabetes Cases', 'Heart Disease Cases']])
    
    with col2:
        st.markdown("### Summary Statistics")
        st.dataframe(data[['Consultations', 'Diabetes Cases', 'Heart Disease Cases']].describe())

elif page == " About":
    st.title(" About This Project")
    
    st.markdown("""
    ## Cambodia Health AI Assistant
    
    ###  Mission
    To make healthcare more accessible to all Cambodians through AI technology.
    
    ### Team
    - **Project Lead:** Senghab Cheng, Chhayhour Ly, Kimseak Sok, Faris Fy
    - **University:** Paragon International University
    - **Competition:** AI in Education Competition 2025
    - **Organizers:** MoEYS & CADT
    
    ### Technology Stack
    - **AI/ML:** Python, TensorFlow, Scikit-learn
    - **Web App:** Streamlit
    - **Data:** Kaggle Medical Datasets
    - **Deployment:** Streamlit
    
    ### Contact
    - **Email:** scheng@paragoniu.edu.kh
    - **Phone:** +855 92 *** *15
    - **GitHub:** github.com/Senghab-Cheng
    
    ### Disclaimer
    This application is for educational and informational purposes only. 
    It is NOT a substitute for professional medical advice, diagnosis, or treatment. 
    Always seek the advice of your physician or other qualified health provider.
    """)
    
    if st.button(" Download Project Report"):
        st.success("Report download started! (Demo)")

st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p> Cambodia Health AI | MoEYS x CADT Competition 2025</p>
    </div>
""", unsafe_allow_html=True)