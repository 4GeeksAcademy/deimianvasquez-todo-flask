from flask import Flask, jsonify, request


# api que guarda personas
# /person --> trae todas las personas --> GET------> listo
# /person/id --> trae una persona por id -->GET ----> listo
# /person  --> registrar una persona --> POST { "name":"Deimian", "lastname":"Vásquez"} --> listo
# /person --> elimina usuario completo --> "DELETE"
# /person/id --> elimina un usuario especifico --> DELETE
# /person/id --> actualizamos el usuario --> PUT
# el almacenamiento va a ser local, se guarda en el archivo y se borra a actualizar --> de momento

people =[
    {
        "id":1,
        "name":"Deimian",
        "lastname":"Vásquez"
    },
    {
        "id":2,
        "name":"Daniel",
        "lastname":"Moret"
    },
     {
        "id":3,
        "name":"Juan",
        "lastname":"Guerrero"
    }
]

app = Flask(__name__)

#decoradores
#Mi primer endpoint
@app.route("/health-check", methods=["GET"])
def health_check():
    return "ok"


@app.route("/person", methods=["GET"])
@app.route("/person/<int:theid>", methods=["GET"])
def get_people(theid=None):
    if theid is None:
        return jsonify(people), 200
    if theid is not None:
        person = list(filter(lambda item: item.get("id") == theid, people ))

        if len(person) > 0:
            return jsonify(person[0]), 200
        else:
            return jsonify({"message":"The user no found"}), 404
        


# @app.route("/person/<int:theid>", methods=["GET"])
# def get_one_person(theid=None):
#     # Así se hace con for 
#     # for person in people:
#     #     if person.get("id") == theid:
#     #         return jsonify(person)
    
#     # return jsonify({"message":"The user no found"}), 404
    
#     #Así lo hacemos con filter
#     if request.method == "GET":
#         person = list(filter(lambda i201 CRtem: item.get("id") == theid, people ))

#         if len(person) > 0:
#             return jsonify(person[0]), 200
#         else:
#             return jsonify({"message":"The user no found"}), 404
        

@app.route("/person", methods=["POST"])
def add_person():
    body = request.json

    if body.get("name") is None:
        return jsonify({"message":"wrong property"}),400
    if body.get("lastname") is None:
         return jsonify({"message":"wrong property"}),400

    body.update({"id":len(people) +1})

    people.append(body)
    return jsonify(body), 201



@app.route("/person/<int:theid>", methods=["PUT"])
def update_person(theid=None):
    body = request.json

    if body.get("name") is None:
        return jsonify({"message":"wrong property"}),400
    if body.get("lastname") is None:
         return jsonify({"message":"wrong property"}),400

    new_person = list(filter(lambda item: item.get("id") == theid, people))
    new_person = new_person[0]
    new_person["name"] = body.get("name")
    new_person["lastname"] = body["lastname"] 

    print(new_person)
    return jsonify(new_person), 201





@app.route("/person/<int:theid>", methods=["DELETE"])
def delete_all_person(theid=None):
    global people

    if theid is None:
        return jsonify({"message":"the id is necesary"}), 400

    # for person in people:
    #     if person.get("id") == theid:
    #         print("Debo eliminar este user")
    #         return jsonify([]), 201

    result = list(filter(lambda item: item.get("id") != theid, people))
    people = result
    
    people = result
    if result:
        return jsonify("todo bien"), 201

    return jsonify({"message":"user not found"}), 404



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3001", debug=True)