# Streamlitライブラリをインポート
import streamlit as st

import geopandas as gpd
import pandas as pd

# メッシュマップのシェープファイルを読み込む
mesh_map = gpd.read_file('path_to_mesh_map_file.shp')

# メッシュマップの属性データを表示して、必要な列を確認する
print(mesh_map.head())

# 人口データを抽出する
population_data = mesh_map[['MESH_ID', 'POPULATION_COLUMN_NAME']]

# 緯度経度情報を抽出する
lat_lon_data = mesh_map[['MESH_ID', 'LATITUDE_COLUMN_NAME', 'LONGITUDE_COLUMN_NAME']]

# 抽出したデータをCSVファイルに保存する
population_data.to_csv('population_data.csv', index=False)
lat_lon_data.to_csv('lat_lon_data.csv', index=False)