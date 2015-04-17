# Copyright 2015 Globo.com. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import json

from flask import abort, Flask, request

app = Flask(__name__)

if not app.debug:
    import logging
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

instances = []


@app.route("/resources/plans", methods=["GET"])
def plans():
    plans = [{"name": "small", "description": "small instance"},
             {"name": "medium", "description": "medium instance"},
             {"name": "big", "description": "big instance"},
             {"name": "giant", "description": "giant instance"}]
    return json.dumps(plans)


@app.route("/resources", methods=["POST"])
def add_instance():
    name = request.form.get("name")
    plan = request.form.get("plan")
    team = request.form.get("team")
    instances.append({"name": name, "plan": plan, "team": team, "binds": [], "units": []})
    return "", 201


@app.route("/resources/<name>/bind-app", methods=["POST"])
def bind_app(name):
    app_host = request.form.get("app-host")
    index, instance = _get_instance(name)
    instance["binds"].append(app_host)
    instances[index] = instance
    envs = {"SOMEVAR": "somevalue"}
    return json.dumps(envs), 201


@app.route("/resources/<name>/bind-app", methods=["DELETE"])
def unbind_app(name):
    app_host = request.form.get("app-host")
    index, instance = _get_instance(name)
    try:
        instance["binds"].remove(app_host)
    except ValueError:
        abort(404)
    instances[index] = instance
    return "", 200


@app.route("/resources/<name>/bind", methods=["POST"])
def bind_unit(name):
    unit_host = request.form.get("unit-host")
    index, instance = _get_instance(name)
    instance["units"].append(unit_host)
    instances[index] = instance
    return "", 201


@app.route("/resources/<name>/bind", methods=["DELETE"])
def unbind_unit(name):
    unit_host = request.form.get("unit-host")
    index, instance = _get_instance(name)
    try:
        instance["units"].remove(unit_host)
    except ValueError:
        pass
    instances[index] = instance
    return "", 200


@app.route("/resources/<name>", methods=["DELETE"])
def remove_instance(name):
    global instances
    _get_instance(name)
    instances = filter(lambda i: i["name"] != name, instances)
    return "", 200


@app.route("/resources/<name>/status", methods=["GET"])
def status(name):
    _get_instance(name)
    return "", 204


@app.route("/list-instances", methods=["GET"])
def instances():
    return json.dumps(instances), 200


def _get_instance(name):
    for i, instance in enumerate(instances):
        if instance["name"] == name:
            return i, instance
    abort(404)

if __name__ == "__main__":
    app.run()
