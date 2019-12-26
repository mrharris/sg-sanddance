import json
import os
from datetime import datetime

import shotgun_api3
from flask import Flask, request, render_template

# react builds the html and static assets into a folder called "build" rather
# than "templates" so tell flask to search for them under "build" instead
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

    # massage the sg entity data into something more compatible with sanddance
    for entity in entities:
        traverse(entity)

    return render_template("index.html", entities=json.dumps(entities))


def traverse(entity):
    # recurse through any linked entities
    for field, value in entity.items():
        if not isinstance(value, list):
            value = [value]
        for v in value:
            if isinstance(v, dict) and "id" in v:
                # value is another entity
                traverse(v)
    conform(entity)


def conform(entity):
    # process the entity fields
    rename_fields = []
    for field, value in entity.items():
        # convert entities into just their "name" value
        if isinstance(value, list):
            value = ",".join([v["name"] for v in value])
        elif isinstance(value, dict):
            value = value["name"]
        # datetime object is not serialisable
        elif isinstance(value, datetime):
            value = str(value)
        if isinstance(value, str):
            # truncate long strings
            value = value[:80] + (value[80:] and '..')

        entity[field] = value

        # sanddance doesn't support field names with "."
        # so convert those field names to "-"
        if "." in field:
            rename_fields.append(field)

    for rename_field in rename_fields:
        entity[rename_field.replace(".", "-")] = entity.pop(rename_field)
