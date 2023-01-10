import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('プレグレスバーの表示')
'Start!!'
latest_iteration=st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)
'Done!!s'

option = st.selectbox(
    'あなたが好きな数字を教えてください,',
    list(range(1,11))
)
'あなたの好きな数字は',option, 'です。'
left_column,right_column=st.columns(2)
button = left_column.button('右カラムにボタンを表示')
if button:
    right_column.write('右に表示')
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味:',text
condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション',condition



# if st.checkbox('Show Image'):
#     img = Image.open('a.png')
#     st.image(img,caption='Kida Daichi',use_column_width=True)

# st.write('Display Image')

# st.write('DataFrame')
# df = pd.DataFrame({
#     '１列目':[1,2,3,4],
#     '２列目':[10,20,30,40]
# })
# df1 = pd.DataFrame({
#     '１列目':[1,2,3,4],
#     '２列目':[10,20,30,40]
# })
# #writeだと引数のweigh,heightが指定できない.dataframeだとできる
# st.dataframe(df)

# st.table(df1)
# df2 = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )
# st.line_chart(df2)

# df3 = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df3)

# """
# # 章
# ## 節
# ### 項　

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

