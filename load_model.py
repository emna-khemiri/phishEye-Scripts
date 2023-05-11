# -*- coding: utf-8 -*-
"""load_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O5_2sTlsuREaJTaFXuZUZCEqa0tOz0S9
"""

import tensorflow as tf
import numpy as np

# Load the LSTM model
lstm_model = tf.keras.models.load_model('lstm1.h5')

# Load the phishing URL detection model
url_detection_model = tf.keras.models.load_model('URL.h5')

# Define the weights for each detection method
weight_domain_validity = 0.1
weight_lstm_model = 0.3
weight_url_detection_model = 0.3
weight_api= 0.3

# Define the thresholds for the LSTM model and URL detection model
threshold_lstm_model = 0.5
threshold_url_detection_model = 0.5

# Assuming you have extracted the email text and URL from the email and have them as variables

# Compute the score for the domain validity function
domain_validity_score = is_valid_email(sender_email)

# Compute the score for the LSTM model
lstm_model_score = lstm_model.predict(np.array([email_text]))[0][0]
# The lstm_model expects a numpy array with shape (batch_size, sequence_length)
# Assuming the email_text is a single sequence, we wrap it in a numpy array with shape (1, sequence_length)
# The predict method returns a numpy array with shape (batch_size, num_classes)
# Assuming there's only one class (phishing or not), we extract the score at index 0

# Compute the score for the URL detection model
url_detection_model_score = url_detection_model.predict(np.array([url]))[0][0]
# Similar to lstm_model_score, assuming there's only one class and we extract the score at index 0

# API Score