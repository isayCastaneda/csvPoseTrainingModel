import pandas as pd

JSON_FILE = "./rawcsv/Pose match.json"
labels = ['Y', 'M', 'C']
jsonValidatedName = 'validationPoseMatch.json'


validation_df = pd.read_json(JSON_FILE, orient='records')
if (len(validation_df.index) != len(validation_df[~validation_df.isnull()].index)):
     validation_df = validation_df[~validation_df.isna()]

validation_df = validation_df[~pd.isna(validation_df.rightElbowAngle)]

validation_df['label'] = validation_df['label'].replace(labels, [0, 1, 2])
validation_df.to_json(jsonValidatedName, orient='records' )


