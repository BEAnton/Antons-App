import mlflow


dbfs:/databricks/mlflow-tracking/556624631856953/5ae41ba202804f7e85cb59321e8ca3bd/artifacts/model/model.pkl
logged_model = 'runs:/5ae41ba202804f7e85cb59321e8ca3bd/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model('model/model')

# Predict on a Pandas DataFrame.
import pandas as pd
loaded_model.predict(pd.DataFrame(data))