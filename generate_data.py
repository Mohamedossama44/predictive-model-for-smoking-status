# import random
# import pandas as pd 
# import numpy as np

# id_1 = 7616 #change to first student id
# id_2 = 7861 #change to second student id
# id_3 = 7806#change to third student id "leave 0000 if team of 2"
# random_seed = id_1+id_2+id_3

# # random.seed(random_seed)
# data_path="C:\\Users\\pc\\Downloads\\ass3_attachments\\ass3_attachments\\Data.csv" #reaplace with data path
# output_path="C:\\Users\\pc\\Downloads\\ass3_attachments\\ass3_attachments\\newdata.csv"#reaplace with output data path

# all_data=pd.read_csv(data_path) 
# all_columns = all_data.columns.tolist()

# target_column = 'smoking'  # Replace 'specific_column_name' with the actual column name

# all_columns.remove(target_column)
# # all_columns.remove('id')
# # features_numbers = random.sample(range(23), 10)
# features_numbers = min(10, len(all_columns))

# np.random.seed(random_seed)

# selected_columns = np.random.choice(all_columns, features_numbers, replace=False)
# print(selected_columns) #MUST BE PRINTED
# selected_columns = np.append(selected_columns, target_column)
# sample_df = all_data[selected_columns].copy()
# sample_df.to_csv(output_path)   #From HERE YOU CAN SPLIT FOR TRAIN ,VALID AND TEST


import random
import pandas as pd 
import numpy as np

id_1 = 7806#change to first student id
id_2 = 7616 #change to second student id
id_3 = 7861 #change to third student id "leave 0000 if team of 2"
random_seed = id_1+id_2+id_3
random.seed(random_seed)

data_path="C:\\Users\\pc\\Downloads\\ass3_attachments\\ass3_attachments\\Data.csv" #reaplace with data path
output_path="C:\\Users\\pc\\Downloads\\ass3_attachments\\ass3_attachments\\newdata.csv"#reaplace with output data path

all_data=pd.read_csv(data_path) 
all_columns = all_data.columns.tolist()

target_column = 'smoking'  

all_columns.remove(target_column)

selected_columns = random.sample(all_columns, 10)

print(selected_columns) #MUST BE PRINTED
selected_columns = np.append(selected_columns, target_column)
sample_df = all_data[selected_columns].copy()
sample_df.to_csv(output_path)   #From HERE YOU CAN SPLIT FOR TRAIN ,VALID AND TEST