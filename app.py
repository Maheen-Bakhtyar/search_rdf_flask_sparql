from flask import Flask,render_template,request
import os
document_path = os.getcwd()+'/ESIP_People.rdf'

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    import rdflib
    if request.method =='GET':
        name = "Eugene Major"
        return render_template("index.html", showtable=0, name=name)
    else:  

        name = request.form.get("name")
        
        g = rdflib.Graph()
        g.parse(document_path)
        knows_query = "SELECT  *  WHERE   { ?text foaf:name ?name .  ?text foaf:mbox ?email .  FILTER regex(?name, '" + str(name) +"') .  }"
        # knows_query = str(name)
        
        qres = g.query(knows_query)
        return render_template("index.html", result = qres, showtable=1, name=name )

@app.route("/rdf_parser", methods=['POST', 'GET'])
def intro():
    import rdflib

    if request.method =='GET':
        return index()


    name = request.form.get("name")
    
    g = rdflib.Graph()
    g.parse(document_path)
    knows_query = "SELECT  *  WHERE   { ?text foaf:name ?name .  ?text foaf:mbox ?email .  FILTER regex(?name, '" + str(name) +"') .  }"
    # knows_query = str(name)
    
    qres = g.query(knows_query)
    return render_template("intro.html", result = qres  )
    # return "The Query is "+ str(name)




if __name__ == "__main__":
    app.run(debug=True)
