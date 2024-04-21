import pandas as pd
import numpy as np
from langchain_openai import OpenAIEmbeddings
import faiss


embeddings = OpenAIEmbeddings(openai_api_key='API KEY',
                              model="text-embedding-3-large", dimensions=1536)
df = pd.read_csv('./data/uzbek_question.csv', index_col=[0])

questions = [x for x in df.question]

embedded_list = []
for i in questions:
    embedded_list.append(embeddings.embed_query(i))

embedded_list = np.array(embedded_list).astype('float32')

index = faiss.IndexFlatL2(1536)
index.add(embedded_list)

faiss.write_index(index, 'mohirdev_uzb_index.index')
