import mlflow
import os


#logged_model = 'runs:/5ae41ba202804f7e85cb59321e8ca3bd/model'
logged_model = 'model.pkl'
# Load model as a PyFuncModel.
dest_dir = os.path.expanduser('~')
dest_path = os.path.join(dest_dir, 'model.pkl')

loaded_model = mlflow.pyfunc.load_model('/model/model.pkl')

# Predict on a Pandas DataFrame.
import pandas as pd

predict_data = pd.DataFrame({"columns": ["Suburb", "Address", "Rooms", "Type", "Method", "SellerG", "Date", "Distance", "Postcode", "Bedroom2", "Bathroom", "Car", "Landsize", "BuildingArea", "YearBuilt", "CouncilArea", "Lattitude", "Longtitude", "Regionname", "Propertycount"], "data": [["Altona", "29 Seves St", 3, "h", "S", "Barlow", "24/06/2017", 11.0, 3018.0, 3.0, 1.0, 1.0, 798.0, NaN, NaN, "Hobsons Bay", -37.86677, 144.83722, "Western Metropolitan", 5301.0], ["Collingwood", "107/10 Stanley St", 1, "u", "VB", "Jellis", "18/03/2017", 1.6, 3066.0, 1.0, 1.0, 1.0, 0.0, 52.0, NaN, "Yarra", -37.8019, 144.9845, "Northern Metropolitan", 4553.0], ["Eltham", "6/17 Silver St", 3, "h", "S", "Barry", "8/07/2017", 18.0, 3095.0, 3.0, 1.0, 2.0, 197.0, 108.0, 2009.0, "Nillumbik", -37.71613, 145.13939, "Eastern Metropolitan", 6990.0], ["Bentleigh", "11 Wheatley Rd", 4, "h", "PI", "McGrath", "12/11/2016", 13.0, 3204.0, 4.0, 2.0, 3.0, 855.0, 197.0, 1930.0, "Glen Eira", -37.9163, 145.0324, "Southern Metropolitan", 6795.0], ["Brighton", "10/32 Outer Cr", 3, "u", "VB", "Buxton", "8/07/2017", 10.5, 3186.0, 3.0, 2.0, 2.0, 0.0, NaN, 2011.0, "Bayside", -37.90542, 144.99817, "Southern Metropolitan", 10579.0]]})

predictions = loaded_model.predict(predict_data)
print(predictions)