# Shotgun-SandDance

Send the data on the current page in [Shotgun](https://www.shotgunsoftware.com) for visualisation in [Microsoft SandDance](https://sanddance.js.org)

## Usage

Create a Shotgun AMI with the url to the backend server (eg 127.0.0.1:5000). On any entity
list view page you display the columns for all the data you want to send to SandDance, the
more numerical and categorical fields the better!
Then send the current page to SandDance using the AMI.

### Developer

This repo consists of a react front end for sanddance explorer and a flask back end
for querying the data from shotgun and sending it to the front end

#### Set up react front end

- `npm install` (install the stuff in package.json)
- `npm start` (start a dev server, or - )
- `npm run build` (compile the `src` and `public` data into a `build` folder)

The npm react build process is really slow. It also is required for the flask backend since I don't
know how to make flask work with the npm dev server. So developing with flask and react is a pain -
at least when working with shotgun AMI style web pages like this one where the entry point is
a POST request. Since all the requested enitity ids and column names comes in via the POST request
to the python backend I do the shotgun api query there, and pass the resulting entities to the
front end via a html data-attribute with jinja. I would love to know if there is a better way to do
this since it doesn't seem very react-y...

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
