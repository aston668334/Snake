import os
os.chdir('/work/data/Line_bot/final/Snaked/src/')
from predict import model_predict

def image_predict(path):
    a = model_predict()
    ans = a.predict(path)
    return(ans)