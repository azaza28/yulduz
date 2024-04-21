import time

import numpy as np
from langchain_openai import OpenAIEmbeddings
import pandas as pd
import faiss


def get_closest(question, k = 5, lang=None):
    embeddings = OpenAIEmbeddings(openai_api_key='API KEY', model="text-embedding-3-large", dimensions=1536)

    if lang == None:
        df = pd.read_csv('data/FAQ.csv')
        df = df[['question', 'answer']]
        index = faiss.read_index("mohirdev_index.index")

    else:
        df = pd.read_csv('data/uzbek_question.csv',index_col=[0])
        index = faiss.read_index("mohirdev_uzb_index.index")

    question_vector = embeddings.embed_query(question)
    question_vector = np.array([question_vector]).astype('float32')

    distances, indices = index.search(question_vector, k)
    closest = [(df['question'].iloc[x].values, df['answer'].iloc[x].values) for x in indices[::-1]]

    return closest

# questions = [x for x in df.question]
# questions
#
# embedded_list = []
# for i in questions:
#     embedded_list.append(embeddings.embed_query(i))
#     time.sleep(20)
#
# embedded_list = np.array(embedded_list).astype('float32')
#
#
# index = faiss.IndexFlatL2(1536)
# index.add(embedded_list)
#
# faiss.write_index(index, 'mohirdev_index.index')


#print(get_closest('Кто основатель мохирдева?'))