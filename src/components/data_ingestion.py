# reading data from dataset then split the data 
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    """
    This class is used to define the configuration for data ingestion.
    It contains the paths for the raw data, train data, and test data.
    """
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')
    #  Due to path they know where to save the data
    
class DataIngestion:
    """
    This class is responsible for data ingestion.
    It reads the data from a CSV file, splits it into training and testing sets,
    and saves the split data to specified paths.
    """
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()  # Initializing the DataIngestionConfig class

    def initiate_data_ingestion(self):
        """
        This method initiates the data ingestion process.
        It reads the data from a CSV file, splits it into training and testing sets,
        and saves the split data to specified paths.
        """
        logging.info("Data Ingestion started")  # Logging the start of the data ingestion process
        try:
            df=pd.read_csv('notebook/data/stud.csv')  # Reading the data from a CSV file (here u can read it using mongdb or any other source)
            logging.info("Data read successfully")  # Logging successful data reading
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)  # Creating directories if they don't exist
            df.to_csv(self.ingestion_config.raw_data_path,index=False)  # Saving the raw data to a CSV file

            logging.info("Train test split initiated")  # Logging the initiation of train-test split
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)  # Splitting the data into training and testing sets

            train_set.to_csv(self.ingestion_config.train_data_path,index=False)  # Saving the training set to a CSV file
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)  # Saving the testing set to a CSV file

            logging.info("Data ingestion completed")  # Logging the completion of data ingestion
            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)  # Returning the paths of the training and testing sets

        except Exception as e:
            raise CustomException(e,sys)  # Raising a custom exception in case of an error

            """
             step 1: Read the data from the source (CSV file in this case)
             (from any source like mongodb, mysql, api etc.)
            
             step 2: Split the data into training and testing sets (80% train, 20% test) and converted raw data set into the csv file

             step 3: Save the training and testing sets to specified paths (artifacts/train.csv and artifacts/test.csv)
             (here we have used the artifacts folder to save the data but u can use any folder)

             step 4: Return the paths of the training and testing sets for further processing
             (this will be used in the next step for data transformation and model training)

             step 5: Handle any exceptions that may occur during the process and log the error message
             (this will help us to debug the code if any error occurs)

             step 6: Create the artifacts folder if it doesn't exist (this will help us to save the data in the specified folder)
             (this will help us to save the data in the specified folder)

             step 7: Save the raw data to a CSV file (this will help us to keep the original data intact)
             (this will help us to keep the original data intact)

             step 8: Log the successful completion of data ingestion (this will help us to debug the code if any error occurs)
        
              """
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()  # Initiating the data ingestion process by calling the method