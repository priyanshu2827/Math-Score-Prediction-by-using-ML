End to End ML project 
- setup project with github
1.data ingestion
2.data transformation
3.madel trainer
4.model evaluation
5.model deployment

CI/CD Pipelines -Github Action
Deployment -aws

step 1: sabse phele u need to make github repo clone it in our pc open in vs code 
cd location
git clone 

step 2: after opening vs code 
conda create -p venv python==3.8 -y
cls - to clear

step 3: to activate the venv
conda activate venv/

step4: To clone the repository and sync with github

step5: create readme.md file 

step6: follow the step in the github repo
git config --global user.email "you@example.com"
git config --global user.name "youexample"
git commit -m "first commit"

if do not see mlproject.egg-info use 
pip install -e

WHOLE PROCESS : pushing eveything in repo
step 1: git add .
step 2: git status
step 3: git commit -m "setup" (use to commit everychanges in the by name )
step 4: git push -u origin main(push evrything from origin)
step 5: check 

thing in the component is data_ingestion, data_transformation, model_trainer (This components (are the module) is basically used for training purpose)

by using the train_pipeline we will try to trigger all the components