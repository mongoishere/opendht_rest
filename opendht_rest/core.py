import connexion
from flask import Flask, render_template, request

# Create app instance and specify specification dir for Swagger
app = connexion.App(__name__, specification_dir='./')

# Provide Swagger specification YAML or JSON file
app.add_api('swagger.yml')

# Route '/' to home.html
@app.route('/api', methods=['GET', 'POST', 'PUT'])
def homeA():
    return render_template('home.html')

@app.route('/', methods=['GET', 'POST', 'PUT'])
def homeB():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)