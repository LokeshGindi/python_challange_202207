******************
Pre-requisites:
******************

Step 1: Download the attached project folder.

Step 2: Navigate to the project root folder

Step 3: Build the image using below command

        docker build -t etl_proj_name:latest .

Step 4: Login to docker container

        docker run -ti etl_proj_name:latest bash

Step 5: Switch to virtual env:

        export SHELL=`which bash`
        pipenv shell

Step 6:  Run the below commands sequentially to install all the dependencies.
         Make sure all the etl project dependencies in place
        
         pipenv install --dev

Step 7: Run the command
     
        `pip list ` to verify.



************************************
How to Run the program?
************************************

1. Run the python program using cli:

Usage:

python fetch_sport_api_data.py --event_type <provide_input_event_names" --locale_conf <property_name=value>

WARNING:
It's bad idea to call the locale, since as a side effect it affects the entire program. Saving and restoring it is almost as bad it is expensive and affects other threads that happen to run before the settings have been restored.

Ex:

python fetch_sport_api_data.py --event_type "f1Results" "Tennis"
