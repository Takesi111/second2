# Streamlitライブラリをインポート
import streamlit as st

import streamlit as st
import pandas as pd

# ファイルアップロード部分
st.title('メッシュマップからデータを抽出するアプリ')
file = st.file_uploader("メッシュマップデータのCSVファイルをアップロードしてください", type=["csv"])

if file is not None:
    mesh_map_data = pd.read_csv(file)

    st.subheader("抽出したいデータを選択してください")
    selected_data = st.multiselect("データを選択", mesh_map_data.columns)

    if selected_data:
        selected_data_df = mesh_map_data[selected_data]
        st.dataframe(selected_data_df)

        # 人口データ抽出
        if '人口データ' in selected_data:
            population_data = selected_data_df[['MESH_ID', '人口データ']]
            st.write("人口データ:")
            st.dataframe(population_data)

        # 緯度経度データ抽出
        if '緯度データ' in selected_data and '経度データ' in selected_data:
            lat_lon_data = selected_data_df[['MESH_ID', '緯度データ', '経度データ']]
            st.write("緯度経度データ:")
            st.dataframe(lat_lon_data)