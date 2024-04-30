from sklearn.ensemble import RandomForestClassifier
import streamlit as st
from URL_Extraction import extract_features
from Model import preprocessor,y_train,X_train_preprocessed,numerical_features

# Load the pre-trained model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_preprocessed, y_train)

def add_missing_columns(url_features, required_columns):
    missing_columns = set(required_columns) - set(url_features.columns)
    for column in missing_columns:
        url_features[column] = url_features[column].fillna(numerical_features[column].mean())
        
    return url_features

def predict_phishing(url):
    # Extract features from the URL
   
    '''parsed_url = urlparse(url)

    url_features = pd.DataFrame({'url_length': [len(url)],
                                 'domain_length': [len(parsed_url.netloc)],
                                 'path_length': [len(parsed_url.path)]})'''
    
    url_features = extract_features(url)
    url_features = add_missing_columns(url_features, numerical_features)
    
    # Preprocess the input data
    url_preprocessed = preprocessor.transform(url_features)
    
    # Make prediction
    prediction = model.predict(url_preprocessed)
    print(prediction)
    if prediction[0] == 1:
        result = 'Phishing'
    else:
        result = 'Legitimate'
    
    return result

st.title('Phishing Detection')

url = st.text_input('Enter URL:')
if st.button('Predict'):
    result = predict_phishing(url)
    st.write('Result:', result)

