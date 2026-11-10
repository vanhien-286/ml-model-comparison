import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data/spam.csv", encoding="latin-1")
df = df[['label', 'Message']]   
df.columns = ['label', 'message']  

df['label'] = df['label'].map({'spam': 1, 'ham': 0})


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

new_messages = [
    "Win a free iPhone now!!!", 
    "Ok I will call you tomorrow.", 
    "Congratulations, you have won $1000 cash prize!",
    "Are we still meeting at 7pm?"
]
X_new = vectorizer.transform(new_messages)


y_new_pred = model.predict(X_new)

for msg, label in zip(new_messages, y_new_pred):
    print(f"Message: {msg} => {'Spam' if label == 1 else 'Ham'}")