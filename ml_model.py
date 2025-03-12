import os
import pandas as pd
import numpy as np
from sklearn.ensemble import VotingRegressor, RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
# from xgboost import XGBRegressor  # Optional: Requires xgboost install

class CropHealthPredictor:
    def __init__(self, data_file="synthetic_crop_data_10000_uniform.csv"):
        # Define base models
        self.models = [
            ('rf', RandomForestRegressor(n_estimators=100)),
            # ('xgb', XGBRegressor(n_estimators=100)),  # Optional
            ('gbr', GradientBoostingRegressor(n_estimators=100)),
            ('svr', SVR(kernel='rbf', C=100))
        ]
        
        # Initialize Voting Regressor (averaging predictions)
        self.model = VotingRegressor(estimators=self.models)
        
        self.data_file = data_file
        self.is_trained = False
        if os.path.exists(self.data_file) and os.stat(self.data_file).st_size > 0:
            self.train()

    def train(self):
        df = pd.read_csv(self.data_file)
        if df.empty:
            print("⚠️ Warning: No data available for training.")
            return
        
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
        
        self.model.fit(X, y)
        self.is_trained = True

    def predict(self, conditions):
        if not self.is_trained:
            print("⚠️ Warning: Model is not trained yet.")
            return 100
        
        # Ensure the input is a dictionary with correct keys
        if not isinstance(conditions, dict):
            print("❌ Error: Conditions must be a dictionary.")
            return 100
        
        # Ensure all values are numeric
        conditions = {k: float(v) for k, v in conditions.items() if v is not None}

        conditions_df = pd.DataFrame([conditions])
        return self.model.predict(conditions_df)[0]
