import os
from catboost import CatBoostClassifier
def get_model_path(path: str) -> str:
    if os.environ.get("IS_LMS") == "1":  # проверяем где выполняется код в лмс, или локально. Немного магии
        MODEL_PATH = '/workdir/user_input/model'
    else:
        MODEL_PATH = path
    return MODEL_PATH

def load_models():
    model_path = get_model_path("E://ML/lesson_22/catboost_model_3")
    from_file = CatBoostClassifier()
    return from_file.load_model(model_path)

