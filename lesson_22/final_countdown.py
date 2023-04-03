import os
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
from catboost import CatBoostClassifier
from sqlalchemy import create_engine
import numpy as np


def batch_load_sql(query: str) -> pd.DataFrame:
    CHUNKSIZE = 200000
    engine = create_engine(
        "postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
        "postgres.lab.karpov.courses:6432/startml"
    )
    conn = engine.connect().execution_options(stream_results=True)
    chunks = []
    for chunk_dataframe in pd.read_sql(query, conn, chunksize=CHUNKSIZE):
        chunks.append(chunk_dataframe)
    conn.close()
    return pd.concat(chunks, ignore_index=True)

def load_features():
    return batch_load_sql("""SELECT * FROM "shatalov_dmitry_user" """)
def load_text():
    return batch_load_sql("""SELECT * FROM "shatalov_dmitry_text" """)

def get_model_path(path: str) -> str:
    if os.environ.get("IS_LMS") == "1":  # проверяем где выполняется код в лмс, или локально. Немного магии
        MODEL_PATH = '/workdir/user_input/model'
    else:
        MODEL_PATH = path
    return MODEL_PATH

def load_models():

    model_path = get_model_path("./catboost_model_3")
    from_file = CatBoostClassifier()
    from_file.load_model(model_path)
    return from_file
user_data = load_features()
posts_data = load_text()
from_file = load_models()
user_data = user_data.drop("index", axis=1)
posts_data = posts_data.drop("index", axis=1)
class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True

app = FastAPI()
@app.get("/post/recommendations/", response_model=List[PostGet])
def recommended_posts(
		id: int,
		time: datetime,
		limit: int = 5) -> List[PostGet]:
    user_data.loc[user_data['user_id'] == id, "timestamp"] = int(time.timestamp())
    data_for_prediction = pd.concat([user_data[user_data['user_id'] == id].reset_index(), posts_data.drop(['text'], axis=1)], axis=1).drop(["index"], axis=1)
    data_for_prediction = data_for_prediction.fillna(method="ffill")
    data_for_prediction.insert(9, "hour", time.hour)
    pred = from_file.predict_proba(data_for_prediction)
    pred = np.append(arr=pred, values = data_for_prediction[["post_id"]],axis=1)
    pred = pd.DataFrame(pred)
    pred = pred.sort_values(by=1, ascending=False)
    answers = []
    for i in range(limit):
        post_id = int(pred.iloc[i][2])
        answers.append({"id":post_id , "text": posts_data.loc[posts_data["post_id"] == post_id].text.iloc[0],
        "topic" : posts_data.loc[posts_data["post_id"] == post_id].topic.iloc[0]})
    return answers