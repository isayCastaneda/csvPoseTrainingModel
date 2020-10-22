import pandas as pd

JSON_FILE = "./rawcsv/squat.json"
labels = ['up', 'down']
jsonValidatedName = 'validationSquat.json'


validation_df = pd.read_json(JSON_FILE, orient='records')
# if (len(validation_df.index) != len(validation_df[~validation_df.isnull()].index)):
#     validation_df = validation_df[~validation_df.isna()]

print(validation_df)
print(validation_df[~validation_df.isna()])

validation_df['label'] = validation_df['label'].replace(labels, [0, 1])
validation_df.to_json(jsonValidatedName, orient='records' )


