import graphlab 
import matplotlib.pyplot as plt

if __name__ == '__main__':
	nutrient = graphlab.SFrame('nutrient.csv') 	# Loading the nutrient.csv file
	nutrient 									# Display the table
	graphlab.canvas.set_target('ipynb')		# Set the canvas target to ipython notebook
	nutrient.show(view="Scatter Plot",x="Potassium",y="Growth rate")
	train_data,test_data = nutrient.random_split(.6,seed=0)
	​growth_model = graphlab.linear_regression.create(train_data, target='Growth rate', 
		features=['Potassium'],validation_set=None)
	
	print test_data['Growth rate'].mean()
	print growth_model.evaluate(test_data)
	

	%matplotlib inline
	plt.plot(test_data['Potassium'],test_data['Growth rate'],'.',
		test_data['nutrient'],sqft_model.predict(test_data),'-')
