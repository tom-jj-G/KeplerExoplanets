import flask
import pickle
import pandas as pd
import tensorflow as tf 

# Use keras to load in the trained model.
model = tf.keras.models.load_model('model/trained_kepler.h5')

app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        input_1 = flask.request.form['input_1']
        input_2 = flask.request.form['input_2']
        input_3 = flask.request.form['input_3']
        input_variables = pd.DataFrame([[input_1, input_2, input_3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]],
                                       columns=["input_1", "input_2", "input_3","input_4","input_5","input_6","input_7","input_8","input_9","input_10","input_11","input_12","input_13","input_14","input_15","input_16","input_17","input_18","input_19","input_20","input_21","input_22","input_23"],
                                       dtype=float)
        prediction = model.predict(input_variables)[0][2]
        return flask.render_template('main.html',
                                     original_input={'input_1':input_1,
                                                     'input_2':input_2,
                                                     'input_3':input_3},
                                     result=prediction,
                                     )