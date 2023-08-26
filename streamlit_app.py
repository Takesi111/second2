# Streamlitライブラリをインポート
import streamlit as st

import pandas as pd

# メッシュマップデータのCSVファイルを読み込む（仮のデータ形式）
mesh_map_data = pd.read_csv('mesh_map_data.csv')

# 人口データを抽出する
population_data = mesh_map_data[['MESH_ID', 'POPULATION_COLUMN']]

# 緯度経度データを抽出する
lat_lon_data = mesh_map_data[['MESH_ID', 'LATITUDE_COLUMN', 'LONGITUDE_COLUMN']]

# 抽出したデータをCSVファイルに保存する
population_data.to_csv('population_data.csv', index=False)
lat_lon_data.to_csv('lat_lon_data.csv', index=False)