import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import copy

st.set_page_config(
    page_title="Phone",
    page_icon=":sunny:",
    layout="wide",
    initial_sidebar_state="expanded",
)


def cramer(arr):
	# arr = [[6, 2, 3, 78], [1, 5, 3, 46], [2, 4, 7, 58]]
	# arr2 = [[6, 2, 3, 78], [1, 5, 3, 46], [2, 4, 7, 58]]
	arr2 = copy.deepcopy(arr)
	def det(x):
		temp = [[0 for _ in range(3)] for _ in range(3)]
		for i in range(3):
		    for j in range(3):
		        temp[i][j] = arr[i][j]
		if x:
		    for i in range(3):
		        temp[i][x-1] = arr[i][3]
		a = temp[0][0] * (temp[1][1]*temp[2][2] - temp[1][2]*temp[2][1])
		b = temp[0][1] * (temp[1][0]*temp[2][2] - temp[1][2]*temp[2][0])
		c = temp[0][2] * (temp[1][0]*temp[2][1] - temp[1][1]*temp[2][0])
		return a-b+c

	D = det(0)
	x = det(1)/D
	y = det(2)/D
	z = det(3)/D
	lis = [x, y, z]
	col1, col2 ,col3= st.columns([1,1,1])
	labels = 'Iphone', 'Huawei', 'Samsung'
	sizes1 = [x*arr2[0][0],y*arr2[0][1],z*arr2[0][2]]
	sizes2 = [x*arr2[1][0],y*arr2[1][1],z*arr2[1][2]]
	sizes3 = [x*arr2[2][0],y*arr2[2][1],z*arr2[2][2]]
	fig1, ax1 = plt.subplots()
	fig2, ax2 = plt.subplots()
	fig3, ax3 = plt.subplots()
	ax1.pie(sizes1,labels=labels, autopct='%1.1f%%',startangle=90)
	ax2.pie(sizes2,labels=labels, autopct='%1.1f%%',startangle=90)
	ax3.pie(sizes3,labels=labels, autopct='%1.1f%%',startangle=90)
	col1.write(fig1)
	col1.write("Bangladesh")
	col2.write(fig2)
	col2.write("China")
	col3.write(fig3)
	col3.write("Japan")
	st.subheader("Phone Quantity")
	source = pd.DataFrame({
		'Quantity': [x, y, z],
		'Phone': ['Iphone', 'Huawei', 'Samsung']
	})

	bar_chart = alt.Chart(source).mark_bar().encode(
	    y='Quantity:Q',
	    x='Phone:O',
	)

	st.altair_chart(bar_chart, use_container_width=True)



def guasselemination(arr):
    # arr = []
	# arr = [[6, 2, 3, 78], [1, 5, 3, 46], [2, 4, 7, 58]]
	# arr2 = [[6, 2, 3, 78], [1, 5, 3, 46], [2, 4, 7, 58]]
	arr2 = copy.deepcopy(arr)
	k = -(arr[1][0] / arr[0][0])
	m = -(arr[2][0] / arr[0][0])
	for i in range(4):
	    arr[1][i] += k * arr[0][i]
	for i in range(4):
	    arr[2][i] += m * arr[0][i]

	n = -(arr[2][1] / arr[1][1])
	for i in range(4):
	    arr[2][i] += n * arr[1][i]

	z = arr[2][3] / arr[2][2]
	y = (arr[1][3] - (arr[1][2] * z)) / arr[1][1]
	x = (arr[0][3] - (arr[0][1] * y) - (arr[0][2] * z)) / arr[0][0]
	
	lis = [x, y, z]

	col1, col2 ,col3= st.columns([1,1,1])
	labels = 'Iphone', 'Huawei', 'Samsung'
	sizes1 = [x*arr2[0][0],y*arr2[0][1],z*arr2[0][2]]
	sizes2 = [x*arr2[1][0],y*arr2[1][1],z*arr2[1][2]]
	sizes3 = [x*arr2[2][0],y*arr2[2][1],z*arr2[2][2]]
	fig1, ax1 = plt.subplots()
	fig2, ax2 = plt.subplots()
	fig3, ax3 = plt.subplots()
	ax1.pie(sizes1,labels=labels, autopct='%1.1f%%',startangle=90)
	ax2.pie(sizes2,labels=labels, autopct='%1.1f%%',startangle=90)
	ax3.pie(sizes3,labels=labels, autopct='%1.1f%%',startangle=90)
	col1.write(fig1)
	col1.write("Bangladesh")
	col2.write(fig2)
	col2.write("China")
	col3.write(fig3)
	col3.write("Japan")
	st.subheader("Phone Quantity")
	source = pd.DataFrame({
		'Quantity': [x, y, z],
		'Phone': ['Iphone', 'Huawei', 'Samsung']
	})

	bar_chart = alt.Chart(source).mark_bar().encode(
	    y='Quantity:Q',
	    x='Phone:O',
	)

	st.altair_chart(bar_chart, use_container_width=True)


def gauss_jordan(arr):
	# arr = [[6, 2, 3, 78], [1, 5, 3, 46], [2, 4, 7, 58]]
	# arr2 = [[6, 2, 3, 78], [1, 5, 3, 46], [2, 4, 7, 58]]
	arr2 = copy.deepcopy(arr)
	k = -(arr[1][0]/arr[0][0])
	m = -(arr[2][0]/arr[0][0])
	for i in range(4): arr[1][i] += k*arr[0][i]
	for i in range(4): arr[2][i] += m*arr[0][i]

	n = -(arr[2][1]/arr[1][1])
	for i in range(4): arr[2][i] += n*arr[1][i]

	n = -(arr[1][2]/arr[2][2])
	for i in range(4): arr[1][i] += n*arr[2][i]

	n = -(arr[0][2]/arr[2][2])
	for i in range(4): arr[0][i] += n*arr[2][i]

	n = -(arr[0][1]/arr[1][1])
	for i in range(4): arr[0][i] += n*arr[1][i]

	z = arr[2][3]/arr[2][2]
	y = arr[1][3]/arr[1][1]
	x = arr[0][3]/arr[0][0]
	lis = [x, y, z]
	col1, col2 ,col3= st.columns([1,1,1])
	labels = 'Iphone', 'Huawei', 'Samsung'
	sizes1 = [x*arr2[0][0],y*arr2[0][1],z*arr2[0][2]]
	sizes2 = [x*arr2[1][0],y*arr2[1][1],z*arr2[1][2]]
	sizes3 = [x*arr2[2][0],y*arr2[2][1],z*arr2[2][2]]
	fig1, ax1 = plt.subplots()
	fig2, ax2 = plt.subplots()
	fig3, ax3 = plt.subplots()
	ax1.pie(sizes1,labels=labels, autopct='%1.1f%%',startangle=90)
	ax2.pie(sizes2,labels=labels, autopct='%1.1f%%',startangle=90)
	ax3.pie(sizes3,labels=labels, autopct='%1.1f%%',startangle=90)
	col1.write(fig1)
	col1.write("Bangladesh")
	col2.write(fig2)
	col2.write("China")
	col3.write(fig3)
	col3.write("Japan")

	st.subheader("Phone Quantity")
	source = pd.DataFrame({
		'Quantity': [x, y, z],
		'Phone': ['Iphone', 'Huawei', 'Samsung']
	})

	bar_chart = alt.Chart(source).mark_bar().encode(
	    y='Quantity:Q',
	    x='Phone:O',
	)

	st.altair_chart(bar_chart, use_container_width=True)



def main():

	st.title("Phone Selling Ratio")
	st.header("Bangladesh, China and Japan")

	selected=st.sidebar.selectbox('Menu',
						('Gauss Elimination',
						'Cramer Rule',
						'Gauss Jordan',
						))
	uploaded_file = st.sidebar.file_uploader("Choose a file")
	# df = [[6, 2, 3, 78], [1, 5, 3, 46], [2, 4, 7, 58]]
	if uploaded_file is not None:
		df = pd.read_csv(uploaded_file).values.tolist()
		if selected=='Gauss Elimination':
			st.subheader("_Gauss Elimination_")
			guasselemination(df)
		elif selected=='Cramer Rule':
			st.subheader("_Cramer Rule_")
			cramer(df)
		elif selected=='Gauss Jordan':
			st.subheader("_Gauss Jordan_")
			gauss_jordan(df)
	else:
		df = [[6, 2, 3, 78], [1, 5, 3, 46], [2, 4, 7, 58]]
		if selected=='Gauss Elimination':
			guasselemination(df)
		elif selected=='Cramer Rule':
			cramer(df)
		elif selected=='Gauss Jordan':
			gauss_jordan(df)


if __name__=='__main__':
    main()