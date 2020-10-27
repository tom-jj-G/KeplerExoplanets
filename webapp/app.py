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
        # Retrieve the inputs
        input_1 = flask.request.form['input_1']
        input_2 = flask.request.form['input_2']
        input_3 = flask.request.form['input_3']
        input_4 = flask.request.form['input_4']
        input_5 = flask.request.form['input_5']
        input_6 = flask.request.form['input_6']
        input_7 = flask.request.form['input_7']
        input_8 = flask.request.form['input_8']
        input_9 = flask.request.form['input_9']
        input_10 = flask.request.form['input_10']
        input_11 = flask.request.form['input_11']
        input_12 = flask.request.form['input_12']
        input_13 = flask.request.form['input_13']
        input_14 = flask.request.form['input_14']
        input_15 = flask.request.form['input_15']
        input_16 = flask.request.form['input_16']
        input_17 = flask.request.form['input_17']
        model_choose = flask.request.form['model']
        # Build the dataframe
        input_variables = pd.DataFrame([[input_2, input_5, input_1,input_3,input_9,input_13,input_8,input_11,input_4,input_17,input_10,input_12,input_6,0,input_16,input_15,input_7,0,0,input_14,0,0,0]],
                                       columns=["c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10","c11","c12","c13","c14","c15","c16","c17","c18","c19","c20","c21","c22","c23"],
                                       dtype=float)
        # Predict using the model
        prediction = model.predict(input_variables)[0][2]
        if prediction == 1:
            output = "Exoplanet not predicted..."
        else:
            output = "Exoplanet predicted!!!"

        return flask.render_template('main.html',
                                     original_input={'Centroid Offset FPF':input_1,
                                                     'Not Transit-Like FPF':input_2,
                                                     'Ephemeris Match Indicates Contamination FPF':input_3,
                                                     'Transit Depth [ppm]':input_4,
                                                     'Stellar Eclipse FPF':input_5,
                                                     'Transit Signal-to-Noise':input_6,
                                                     'Stellar Radius [Solar radii]':input_7,
                                                     'Impact Parameter':input_8,
                                                     'Orbital Period [days]':input_9,
                                                     'Equilibrium Temperature [K]':input_10,
                                                     'Transit Duration [hrs]':input_11,
                                                     'Insolation Flux [Earth flux]':input_12,
                                                     'Transit Epoch [BKJD]':input_13,
                                                     'Kepler-band [mag]':input_14,
                                                     'Stellar Surface Gravity [log10(cm/s**2)]':input_15,
                                                     'Stellar Effective Temperature [K]':input_16,
                                                     'Planetary Radius [Earth radii]':input_17,
                                                     'Machine Learning model choose':model_choose},
                                     result=output,
                                     )