from flask import Flask, render_template, request, jsonify
from rag import retrieve_information

app = Flask(__name__, template_folder=".", static_folder=".", static_url_path="")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()
    waste = data.get("waste", "").lower()

    if "cloth" in waste or "clothes" in waste or "shirt" in waste or "jeans" in waste:
        result = {
            "category": "Textile Waste",
            "action": "Donate wearable clothes or send unusable textiles to an appropriate textile recycling facility.",
            "recycling": "Old clothes can be reused, repaired, upcycled, or recycled into new textile products.",
            "safety": "Do not burn clothes, especially synthetic fabrics, because they may release harmful fumes."
        }

    elif "plastic" in waste or "bottle" in waste:
        result = {
            "category": "Plastic Waste",
            "action": "Clean suitable plastic items and place them in recyclable waste collection.",
            "recycling": "Suitable plastic items can be recycled through authorized collection systems.",
            "safety": "Keep plastic waste away from fire and do not burn plastic."
        }

    elif "battery" in waste:
        result = {
            "category": "Hazardous / E-Waste",
            "action": "Take batteries to an authorized battery or e-waste collection point.",
            "recycling": "Batteries should be handled through proper recycling facilities.",
            "safety": "Do not burn, puncture, crush, or open batteries."
        }

    elif "mobile" in waste or "phone" in waste or "charger" in waste:
        result = {
            "category": "E-Waste",
            "action": "Take the electronic item to an authorized e-waste collection center.",
            "recycling": "Electronic components can be recovered through proper e-waste recycling.",
            "safety": "Do not burn or dismantle electronic devices."
        }

    elif "food" in waste or "banana" in waste or "vegetable" in waste:
        result = {
            "category": "Organic Waste",
            "action": "Put organic waste in the appropriate wet/organic waste collection.",
            "recycling": "Organic waste can be composted where suitable.",
            "safety": "Keep organic waste separate from electronic and hazardous waste."
        }

    elif "paper" in waste or "newspaper" in waste or "cardboard" in waste:
        result = {
            "category": "Paper Waste",
            "action": "Keep paper clean and dry and place it in recyclable waste collection.",
            "recycling": "Paper and cardboard can usually be recycled.",
            "safety": "Keep paper dry and free from food contamination."
        }

    else:
        result = {
            "category": "Needs AI Analysis",
            "action": "No matching waste information was found.",
            "recycling": "Please check local waste-management guidelines.",
            "safety": "For hazardous items, follow authorized disposal guidance."
        }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
