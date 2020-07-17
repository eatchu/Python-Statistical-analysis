# -*- coding: utf-8 -*-
"""
문) tree_data.csv 파일의 변수를 이용하여 아래 조건으로 DecisionTree model를 생성하고,
    의사결정 tree 그래프를 시각화하시오.
    
 <변수 선택>   
 x변수 : iq수치, 나이, 수입, 사업가유무, 학위유무
 y변수 : 흡연유무
 
 <그래프 저장 파일명> : smoking_tree_graph.dot
"""

import pandas as pd

tree_data = pd.read_csv("data/tree_data.csv")
print(tree_data.info())
'''
iq         6 non-null int64 - iq수치
age        6 non-null int64 - 나이
income     6 non-null int64 - 수입
owner      6 non-null int64 - 사업가 유무
unidegree  6 non-null int64 - 학위 유무
smoking    6 non-null int64 - 흡연 유무
'''

x = tree_data.iloc[:,:5]
y = tree_data.iloc[:,5]
name = list(x.columns)
type(name)

from sklearn.tree import DecisionTreeClassifier, export_graphviz  # tree model
from sklearn.metrics import accuracy_score, confusion_matrix
# tree 시각화 관련
from sklearn.tree.export import export_text  # tree 구조 텍스트
from sklearn import tree

dt = DecisionTreeClassifier()
model = dt.fit(x,y)

tree.plot_tree(model,feature_names=name)

export_graphviz(model, 
                out_file='smoking_tree_graph.dot',
                max_depth=5,
                feature_names = name)


print(export_text(model,name))

# income, age


# 중요변수 기준 subset 
dataset = tree_data[tree_data['income'] <= 24.0]
dataset 

dataset2 = tree_data[tree_data['income'] > 24.0]
dataset2




