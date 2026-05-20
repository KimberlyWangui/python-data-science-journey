from flask import Flask, request, jsonify
from transaction_count import MRFraudTransactionCount
import tempfile
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    data = request.get_json()
    transactions = '\n'.join(data['transactions'])

    # Write transactions to a temp file — mrjob reads from files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(transactions)
        temp_path = f.name

    try:
        # Pass the temp file path as the input argument
        mr_job = MRFraudTransactionCount(args=[temp_path, '--no-conf'])
        with mr_job.make_runner() as runner:
            runner.run()
            fraud_count = 0
            for key, value in mr_job.parse_output(runner.cat_output()):
                if key == 'fraud':
                    fraud_count = value
    finally:
        os.unlink(temp_path)  # Clean up the temp file

    return jsonify({'fraudulent_transactions': fraud_count})

if __name__ == '__main__':
    app.run(debug=True)