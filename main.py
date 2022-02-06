import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time




st.title('Streamlit')


st.write('プログレスバーの表示')
'start!!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
        latest_iteration.text(f'iteration{i+1}')
        bar.progress(i+1)
        time.sleep(0.02)

'done!!!!!'




text = st.sidebar.text_input('あなたの趣味を入力してください。')
condition = st.sidebar.slider('あなたの今の調子は',0,100,20)

st.write('あなたの趣味:',text)
st.write('あなたの調子:',condition)

# if st.checkbox('Show image'):
#     img = Image.open('sample.jpg')
#     st.image(img,caption='イメージ図',use_column_width=True)




# # st.dataframe(df.style.highlight_max(axis=0))
# df = pd.DataFrame(
#     np.random.randn(100,2)/[50,50] + [35.69,139.70],
#     columns = ['lat','lon']
# )
# st.map(df)