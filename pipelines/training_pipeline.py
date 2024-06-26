from zenml import pipeline
from steps import (
    ingest_data,
    clean_data,
    train_model,
    evaluate_model,
)
# from steps.ingest_data import ingest_data 
# from steps import 
# from steps.clean_data import clean_data 
# from steps.model_train import train_model
# from steps.evaluation import evaluate_model

@pipeline(enable_cache=True)
def training_pipeline(data_path: str):
    data = ingest_data(data_path)
    X_train, X_test, y_train, y_test = clean_data(data)

    model = train_model(X_train, X_test, y_train, y_test)
    r2_score, rmse = evaluate_model(model, X_test, y_test)


