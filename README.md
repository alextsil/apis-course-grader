## PSPI automatic grader
- Pull this repository locally
### Install required libraries
##### Use python 3
- (Optional) [Create a virtual environment](https://github.com/vasisouv/social-networks-analysis-pms#python-installation)
- Run cmd as an Administrator (or use sudo for linux users)
- Execute `pip install pymongo`
- Execute `pip install requests`
### Configuration
##### Default config:
- Web service: `http://127.0.0.1:5110`
- MongoDB: `mongodb://127.0.0.1:27017`
- Db name: `apis`
- Db collection: `apis`

(modify settings.py if needed)

##### Run main.py
`python main.py`