import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

data = pd.read_csv('D:/VSCODE/Phising Domain Detection/dataset_small.csv')

X = data.iloc[:,:-1]
y = data.iloc[:,-1]

# Define numerical features
numerical_features = X.columns.tolist()

# Define preprocessing steps for numerical features
numerical_transformer = Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='mean')), #impute missing values with the mean
    ('scaler',StandardScaler())
    ])

#Combine preprocessing steps for numerical features
preprocessor = ColumnTransformer(transformers=[
    ('num',numerical_transformer,numerical_features)
    ])

#split dataset into traning and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

#preprocess the training data
X_train_preprocessed = preprocessor.fit_transform(X_train)

#preprocess the testing data
X_test_preprocessed = preprocessor.transform(X_test)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Initialize the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier on the preprocessed training data
rf_classifier.fit(X_train_preprocessed, y_train)

# Predict the target variable for the preprocessed testing data
y_pred = rf_classifier.predict(X_test_preprocessed)

# Evaluate the performance of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

