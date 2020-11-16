from service import Service   	  
from flask import Flask, request, make_response, json

my_server=Service()
app = Flask(__name__)

@app.route("/storage/<filename>")
def get_req(filename):
	if my_server.get(filename):
		res = make_response(my_server.get(filename), 200)
		return res
	res = make_response("", 404)
	return res

@app.route("/storage/<filename>", methods=["PUT"])
def put_req(filename):
	req = json.dumps(request.get_json())
	if request.is_json:
		my_server.put(filename,req)
		return make_response("", 201) 
	return make_response("",400)

@app.route("/storage/<filename>",methods=["DELETE"])                         
def delete_req(filename):
	my_server.delete(filename)                                    
	return make_response("", 204)                                                                                         
if __name__ == '__main__':                                                      
    app.run(host= '0.0.0.0', port = 8080, debug=True)
