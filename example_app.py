# ==== Copyright 2008 - 2025 S. Volkan Kücükbudak ====
# Example APP
# IT SHOWS YOU HOW YOU CAN USE ADI - MAYBE FOR YOUR AI TOOLS
# ==== IF YOU USE MY CODE READ LICENSE FILE PLEASE ====
# DONT STEAL FREE CODE FROM OTHERS! RESPECT FREE WORK OF DEVELOPERS AND THEIR CREDITS OR IN FUTURE YOU MUST PAY FOR CODE LIKE THIS!
# ==== Copyright 2008 - 2025 S. Volkan Kücükbudak ====
# =====================================================================================================
# HOW TO USE THIS EXAMPLE APP?
#
# Send a POST request to the /analyze route with a JSON body containing the input_text:
# Example: 
# curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"input_text": "Pls fix my code. Urgent!!!"}'
# =====================================================================================================
from flask import Flask, request, jsonify
from adi import DumpindexAnalyzer

app = Flask(__name__)

# Initialisiere  ADI-Analyzer
analyzer = DumpindexAnalyzer()

def chat_with_adi(input_text):
    result = analyzer.analyze_input(input_text)
    decision = result['decision']
    recommendations = result['recommendations']
    
    response = f"ADI: {result['adi']}\nEntscheidung: {decision}\nEmpfehlungen:\n"
    for rec in recommendations:
        response += f"- {rec}\n"
    
    return response

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    input_text = data.get('input_text', '')
    result = analyzer.analyze_input(input_text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
