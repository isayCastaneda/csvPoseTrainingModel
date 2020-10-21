import pandas as pd

JSON_FILE = "Arms Up.json"
labels = ['up', 'down']


validation_df = pd.read_json(JSON_FILE, orient='records')
#print(validation_df[~validation_df.isna()])
validation_df['label'] = validation_df['label'].replace(labels, [0, 1])
validation_df.to_json('validationArmsUp.json', orient='records' )


