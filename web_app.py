from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# โหลด Model
if os.path.exists('iris_model.pkl'):
    model = joblib.load('iris_model.pkl')
    class_names = joblib.load('iris_class_names.pkl')
else:
    model = None

@app.route('/')
def home():
    return render_template('first.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return render_template('first.html', prediction_text="Error: Model not loaded")

    try:
        features = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]
        
        final_features = np.array([features])
        prediction_idx = model.predict(final_features)[0]
        predicted_class = class_names[prediction_idx] # ได้ค่าเป็น 'setosa', 'versicolor', หรือ 'virginica'
        
        # 1. สร้างชื่อไฟล์รูปภาพ (เช่น setosa.jpg)
        image_filename = f"{predicted_class}.jpg"
        
        result = f"Prediction: Iris {predicted_class.capitalize()}"

    except Exception as e:
        result = f"Error: {str(e)}"
        image_filename = None

    # 2. ส่งตัวแปร flower_image ไปที่ html
    return render_template('first.html', prediction_text=result, flower_image=image_filename)

if __name__ == "__main__":
    app.run(debug=True)