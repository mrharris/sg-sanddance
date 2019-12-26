## SG SandDance
Send the data on the current page for visualisation in Microsoft SandDance

### Developer
This repo consists of a react front end for sanddance explorer and a flask back end
for querying the data from shotgun and sending it to the front end

#### Set up react front end
```bash
npm install
npm start
```

#### Set up python back end
```bash
# set up a virtual env in the "server/" folder
cd server
python3 -m venv venv

# activate it
./venv/Scripts/activate (windows)
source ./venv/bin/activate (linux)

# install the requirements
pip install -r requirements.txt
```
In the server folder, create a .env file (not to be commited to git!) with the following contents
```bash
FLASK_ENV=development  
SG_URL="https://site.shotgunstudio.com"  
SG_SCRIPT_NAME="script_name"  
SG_SCRIPT_KEY="script_key"  
```
Run `flask run --host '0.0.0.0'`