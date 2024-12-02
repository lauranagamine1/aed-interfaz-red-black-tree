from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from red_black_tree import RedBlackTree  # Asegúrate de tener esta clase definida
import random

app = Flask(__name__)
CORS(app)
matplotlib.use('Agg')

# utiliza la clase RedBlackTree de red_back_tree.py
# todavia no funciona, probar con postman primero

#para inciar:
# pip install flask, flask-cors, matplotlib, networkx
# python server.py

rbt = RedBlackTree()

def process_tree():
    # Crear el grafo visual del árbol
        G = nx.DiGraph()
        def add_edges(node):
            if node is not None and node != rbt.TNULL:
                G.add_node(node, label=str(node.key), color=node.color)
                if node.left != rbt.TNULL:
                    G.add_edge(node, node.left)
                    add_edges(node.left)
                if node.right != rbt.TNULL:
                    G.add_edge(node, node.right)
                    add_edges(node.right)
        add_edges(rbt.root)

        # Dibujar el árbol
        fig, ax = plt.subplots()
        pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')
        # Extraer colores de los nodos desde sus atributos
        node_colors = [data['color'] for _, data in G.nodes(data=True)]
        node_labels = {n: G.nodes[n]['label'] for n in G.nodes}
        nx.draw(
            G,
            pos,
            with_labels=True,
            labels=node_labels,
            node_size=700,
            node_color=node_colors,
            font_weight='bold',
            edge_color='black',
            font_color='white'
        )
        fig.patch.set_facecolor('#146C94')
        #plt.title("Red-Black Tree")
        output_path = "static/rbtree.png"
        plt.savefig(output_path)
        plt.close()

@app.route('/api/v1/rbtree/keys', methods=['POST'])
def insert_keys():
    try:
        # recibe datos del arbol, dado keys
        data = request.json
        keys = data.get("keys", [])

        for key in keys:
            rbt.insert(key)

        process_tree()

        return jsonify({"imageUrl": f"http://localhost:5000/static/rbtree.png"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/v1/rbtree/keys', methods=['DELETE'])
def delete_keys():
    try:
        # recibe datos del arbol, dado keys
        data = request.json
        keys = data.get("keys", [])

        for key in keys:
            rbt.delete(key)

        process_tree()

        return jsonify({"imageUrl": f"http://localhost:5000/static/rbtree.png"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/v1/rbtree/keys/random', methods=['POST'])
def insert_random_keys():
    try:
        # recibe datos del arbol, dado keys
        data = request.json
        min = data.get("keys", 0)
        max = data.get("max", 100)
        num = data.get("num", 1)

        for _ in range(num):
            rbt.insert(random.randint(min, max))

        process_tree()

        return jsonify({"imageUrl": f"http://localhost:5000/static/rbtree.png"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/v1/rbtree/clear', methods=['POST'])
def clear_tree():
    try:
        # recibe datos del arbol, dado keys
        rbt.clear()

        process_tree()

        return jsonify({"imageUrl": f"http://localhost:5000/static/rbtree.png"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
