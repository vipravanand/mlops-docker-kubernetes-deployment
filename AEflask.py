
import tensorflow as tf
from flask import Flask, jsonify, make_response, request
import numpy as np
import logging 

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)

model = tf.keras.models.load_model("autoencoder.hdf5")
logging.info('Model loaded.......')

mae_threshold = 0.275  #Mean absolute error Values higher than this is classified as an anomaly
logging.info(f'MAE Threshold : {mae_threshold}')


def mae_anomaly( instance): 
    predictions = model.predict( instance)
    mae = np.mean(np.abs( instance - predictions))
    return float(mae)



@app.route('/anomaly', methods=['POST'])
def anomaly_detector():
    logging.info(f"Request Body : {request.get_json()}")
    instance = request.get_json()['sequence']
    array = np.array( instance).reshape(-1,1,4)  #Input layer of the model expects instances of shape (-1,1,4)
    mae = mae_anomaly( array)
    anomaly = mae > mae_threshold
    response_dict = {'mae ':mae, 'anomaly ': anomaly}

    logging.info(f"Prediction : {response_dict}")
    return jsonify(response_dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')