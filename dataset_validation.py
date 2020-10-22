import pandas as pd

JSON_FILE = "./rawcsv/jumpinJacks.json"
labels = ['up', 'down']
jsonValidatedName = 'validationJumpingJacks.json'


validation_df = pd.read_json(JSON_FILE, orient='records')


validation_df = validation_df[(~pd.isna(validation_df.rightElbowAngle)) & (~pd.isna(validation_df.leftElbowAngle))]

validation_df['label'] = validation_df['label'].replace(labels, [0, 1])
validation_df.to_json(jsonValidatedName, orient='records')


