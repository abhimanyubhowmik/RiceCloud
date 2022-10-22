import lightgbm as lgb
import numpy as np
import Logging
import streamlit as st

log = Logging.app_logging()

class lgbm:

    def __init__(self,X):
        self.lgb_model = lgb.Booster(model_file='Model/lgbm_model.mdl')
        self.X = X

    def predict(self):
        try:
            prediction_lgb = self.lgb_model.predict(self.X)
            prediction_lgbm = np.array([np.argmax(i) for i in prediction_lgb])
            label_map = {0:"brown_spot",
                    1:"healthy",
                    2:"hispa",
                    3:"leaf_blast"
                }
            prediction = []
            for i,pred in enumerate(prediction_lgbm):
                label = label_map[pred]
                prediction.append(label)
                st.text("Image {}: {}".format(i+1, label))
                log.info('Prediction Successfull')
            return prediction

        except Exception as e:
            log.error(e)
