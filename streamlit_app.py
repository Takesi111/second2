import streamlit as st
import geopandas as gpd
from shapely.geometry import Polygon

# 市町村の境界データを読み込む
boundaries = gpd.read_file('path_to_boundaries_shapefile.shp')

def main():
    st.title("市町村の人口重心座標計算アプリ")
    
    # 市町村名を入力
    city_name = st.text_input("市町村名を入力してください:")
    
    if st.button("計算"):
        # 指定した市町村のデータを取得
        city_data = boundaries[boundaries['市町村名'] == city_name]

        if not city_data.empty:
            # 市町村の人口データを取得（仮にランダムな数値としています）
            population = city_data['人口'].values[0]

            # 市町村の境界を取得
            city_boundary = city_data['geometry'].values[0]

            # 市町村の人口重心を計算
            population_center = city_boundary.centroid

            # 結果を表示
            st.write(f"{city_name}の人口重心座標:")
            st.write(f"緯度: {population_center.y[0]}")
            st.write(f"経度: {population_center.x[0]}")
            st.write(f"人口: {population}")
        else:
            st.write(f"{city_name}はデータが見つかりませんでした。")

if __name__ == "__main__":
    main()
