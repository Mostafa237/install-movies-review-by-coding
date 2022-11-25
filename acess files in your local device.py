import  glob
import pandas as pd
# List of dictionaries to build file by file and later convert to a DataFrame
df_list = []
folder="D:\Projects\Data analysis FWD\project\install _files_by_codeing\ebert_reviews".replace("\ ", "/")
for ebert_review in glob.glob(folder+'/*.txt'):
    with open(ebert_review, encoding='utf-8') as file:
        title = file.readline()[:-1]
        review_url=file.readline()[:-1]
        review_text=file.read()

        # Append to list of dictionaries
        df_list.append({'title': title,
                        'review_url': review_url,
                        'review_text': review_text})
df = pd.DataFrame(df_list, columns=['title', 'review_url', 'review_text'])
print(df.head())