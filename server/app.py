import os
import json

from flask import Flask, request, render_template
import shotgun_api3

app = Flask(__name__, static_folder="../build/static", template_folder="../build")

sg = shotgun_api3.Shotgun(
    os.environ.get("SG_URL"),
    script_name=os.environ.get("SG_SCRIPT_NAME"),
    api_key=os.environ.get("SG_SCRIPT_KEY"),
)


@app.route('/', methods=["POST"])
def route():
    post_dict = request.form.to_dict()
    entity_ids = post_dict["selected_ids"] or post_dict["ids"]
    entity_ids = [int(id_) for id_ in entity_ids.split(",")]
    entity_type = post_dict["entity_type"]
    entity_fields = [col for col in post_dict["cols"].split(",")]

    entities = sg.find(
        entity_type,
        [["id", "in", entity_ids]],
        entity_fields,
    )

    return render_template("index.html", entities=json.dumps(entities))
