import mlflow
import bentoml

def load_save_model():
    loaded_model = mlflow.lightgbm.load_model('./mlruns/985497283900259339/1bb7d01fa8fc4bf8b8c83d9634ff93c7/artifacts/model')

    bento_model = bentoml.picklable_model.save_model(
        'light_gbm',
        loaded_model,
        signatures={"predict": {"batchable": True}}
    )
    print(f"Bento model tag = {bento_model.tag}")

if __name__ == "__main__":
    load_save_model()