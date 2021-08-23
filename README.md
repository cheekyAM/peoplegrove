# peoplegrove
**Assignment**

finalgrove is the notebook with final experiments.

Note1: If you want to recreate the experiments in finalgrove notebook. First download the data to your google drive. (because downloading from link has limits)
So, first download to data to your drive and connect your drive, then execute the cells in notebook sequentially.

Note2: For testing any new data of same csv format,you can see the guide at the end section of finalgrove. But remember for testing, you need to train the model first. beacuse model, labels and dicionary will be used in testing new data.

**Deployment**

Attaching a sample main.py to show how to create rest api to get predictions on the new data (its not deployable, because the data is not stored from colab notebook). However it will look like that.

**step1: first install the required libraries**
$ pip install fastapi uvicorn

Install Heroku
$sudo snap install --classic heroku

**Step2: Create our ML model, model.py:**
write the code which we have written in our colab file and save the model as pkl file.

**Step 3: Creating a REST API using FAST API**
For this I have written sample file main.py.

At last, we can run the app using
$ uvicorn app:app --reload

Note: If you want full working deployment, please let me know. As from problem file itseems you require colab file of experiment and just sample on how to deploy and interation through apis.


