import bentoml
from bentoml.io import JSON
import numpy as np

bento_model: bentoml.Model = bentoml.models.get("light_gbm:latest")
my_runner: bentoml.Runner = bento_model.to_runner()

single_ts_svc = bentoml.Service("single_ts", runners=[my_runner])

@single_ts_svc.api(input=JSON(), output=JSON())
def predict(input_data: np.ndarray) -> np.ndarray:
    return my_runner.predict.run(input_data)

# add JSON return for api usage 
# add import data transformation to timeseries