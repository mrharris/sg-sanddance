## SG SandDance

Send the data on the current page for visualisation in Microsoft SandDance

### Developer

This repo consists of a react front end for sanddance explorer and a flask back end
for querying the data from shotgun and sending it to the front end

#### Set up react front end

 - `npm install` (install the stuff in package.json)
 - `npm start` (start a dev server, or - )
 - `npm run build` (compile the `src` and `public` data into a `build` folder)  


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
SG_URL="https://site.shotgunstudio.com"  
SG_SCRIPT_NAME="script_name"  
SG_SCRIPT_KEY="script_key"  
```

Run `flask run --host '0.0.0.0'`. It should load the built html from the front-end

Unlike default flask apps, this one expects to find the front end scripts in the
`build` folder (result of `npm run build`) rather than `/static` and `/templates`
since that is where react builds to. 