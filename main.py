from flask import Flask, jsonify
from NpcGenerator import NpcGenerator

app = Flask(__name__)

@app.route('/api/npc/')
def npcRandomizer():
    npc = NpcGenerator.generateNpc()
    return npc.toJSON()

if __name__ == '__main__':
    app.run(port=8081, debug=True)
