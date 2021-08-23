# peoplegrove
**Assignment**

finalgrove is the notebook with final experiments.

Note1: If you want to recreate the experiments in finalgrove notebook. First download the data to your google drive. (because downloading from link has limits)
So, first download to data to your drive and connect your drive, then execute the cells in notebook sequentially.

Note2: For testing any new data of same csv format,you can see the guide at the end section of finalgrove. But remember for testing, you need to train the model first. beacuse model, labels and dicionary will be used in testing new data.

**Deployment**

There are so many ways of deployment, It mainly depends, whether your ML model has been integrate to some website (eg. you can use flask to direct route to check predictions for some data on our model, and maybe you have data coming fro different sources in web. there can be lot of api's involved). It also depends which cloud platform(GCP,AWS or Heroku) you have hosted your app or maybe model directly(eg. You can crete REST API using FAST API and deploy on Heroku). I am not going into details, but i would write briefly about deploying your model on GCP. 

Steps:
1) first export our trained model from our finalgrove file to pickle using.
import pickle
with open('model.pkl', 'wb') as model_file:
  pickle.dump(classifier, model_file)
