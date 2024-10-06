### Clone repository and run "pip install -e ." in the repo directory
### Library import:

import pandas as pd
from easycreditscoring import DataCleaner, ModelPipeLine, Ensembling, UnitEconomy

df = pd.read_csv('/tests/train.csv')


Cleaner = DataCleaner(df=df, target_column = "Credit_Score")

# ModelZoo = ModelPipeLine()

# ensemble = Ensembling(model_zoo=ModelZoo,base_models=base_models,model_list=model_list)

# Economy = UnitEconomy()