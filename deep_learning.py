import graphlab

if __name__ == '__main__':

	image_train = graphlab.SFrame('image_train_data/')
	image_test = graphlab.SFrame('image_test_data/')
	graphlab.canvas.set_target('ipynb')
	image_train['image'].show()
	raw_pixel_model = graphlab.logistic_classifier.create(image_train,target='label',
	                                              features=['image_array'])
	image_test[0:3]['image'].show()
	image_test[0:3]['label']
	raw_pixel_model.predict(image_test[0:3])
	raw_pixel_model.evaluate(image_test)
	len(image_train)
	image_train.head()
	deep_features_model = graphlab.logistic_classifier.create(image_train,
	                                                         features=['deep_features'],
	                                                         target='label')

	image_test[0:3]['image'].show()
	deep_features_model.predict(image_test[0:3])
	deep_features_model.evaluate(image_test)
