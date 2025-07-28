import numpy as np
#from sklearn.ensemble import RandomForestClassifier
#from xgboost import XGBClassifier
from lightgbm import lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    # [font_size, is_bold, is_centered, y0 (top), line_len]
    X = np.array([
        [18, 1, 1, 100, 10],   # Title
        [16, 1, 1, 150, 20],   # H1
        [14, 1, 0, 200, 30],   # H2
        [12, 0, 0, 300, 80],   # Paragraph
        [10, 0, 0, 350, 90],   # Paragraph
        [16, 1, 1, 400, 15],   # H1
        [14, 1, 0, 420, 25],   # H2
    ])
    y = np.array([1, 1, 1, 0, 0, 1, 1])  # 1 = heading, 0 = not

    X_train,x_test, y_train, y_test=train_test_split(X,y,test_size=0.3,random_state=42)

    #clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf = lgb.LGBMClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    y_pred=clf.predict(x_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Trained LightGBM model with accuracy: {acc:.2f}")
    joblib.dump(clf, 'model/heading_classifier.pkl')
    print("✅ Trained and saved classifier.")

if __name__ == "__main__":
    train_model()
