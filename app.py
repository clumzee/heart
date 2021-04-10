from flask import Flask, render_template, request
import numpy as np
from keras.models import load_model

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        py_feature1 = request.form['feature1']
        py_feature2 = request.form['feature2']
        py_feature3 = request.form['feature3']
        py_feature4 = request.form['feature4']
        py_feature5 = request.form['feature5']
        py_feature6 = request.form['feature6']
        py_feature7 = request.form['feature7']
        py_feature8 = request.form['feature8']
        py_feature9 = request.form['feature9']
        py_feature10 = request.form['feature10']
        py_feature11 = request.form['feature11']
        py_feature12 = request.form['feature12']
        py_feature13 = request.form['feature13']
        py_feature14 = request.form['feature14']
        py_feature15 = request.form['feature15']
        py_feature16 = request.form['feature16']
        py_feature17 = request.form['feature17']
        py_feature18 = request.form['feature18']
        py_feature19 = request.form['feature19']
        py_feature20 = request.form['feature20']
        py_feature21 = request.form['feature21']

        loaded_model = load_model("heart_model.h5")

        my_list = map(int,[py_feature1,py_feature2,py_feature3,py_feature4,py_feature5,py_feature6,py_feature7,py_feature8,py_feature9,py_feature10,py_feature11,py_feature12,py_feature13,py_feature14, py_feature15,py_feature16,py_feature17,py_feature18,py_feature19,py_feature20,py_feature21])
        my_list = list(my_list)
        prediction = loaded_model.predict(np.array([my_list]))
        text = None

        if prediction < 0.5:
            text = "You have high chances of heart disease"

        else:
            text = "You seem perfectly fine"


        

        
        return render_template("result.html", text = text)
    return render_template("temp.html")


if __name__ == "__main__":
    app.run(debug=True)