from flask import Flask,request,jsonify
from transaction_count import MRFraudTransactionCount
from io import StringIO
import json

app = Flask(__name__)

@app.route('/process', methods =['POST'])
def process_data():
#get the transaction data from request
    data = request.get_json()
# converr the data into a formatsuitable for mrjob 
    transactions = '\n'.join(data['transactions'])
# Assuming JSON format {'transactions': [...]}   
    transactions_io = StringIO(transactions)
#Run the mapreduce job
    mr_job = MRFraudTransactionCount(args=[])
    with mr_job.make_runner()as runner:
        runner.run()
        fraud_count =None
        for key , value in mr_job.parse_output(runner.cat_output()):
            if key == 'fraud':
                fraud_couut= value
        #return the fraud count as json response
    return jsonify({'fraudulent_transactions':fraud_count})
if __name__ == '__main__':
    app.run(debug= False)
