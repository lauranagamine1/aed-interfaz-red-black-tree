from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import networkx as nx
import matplotlib.pyplot as plt
from red_black_tree import RedBlackTree  # Asegúrate de tener esta clase definida

app = Flask(__name__)
CORS(app)

# utiliza la clase RedBlackTree de red_back_tree.py
# todavia no funciona

@app.route('/api/v1/rbtree', methods=['POST'])
def process_tree():
    try:
        # recibe datos del arbol, dado keys
        data = request.json
        keys = data.get("keys", [])

        rbt = RedBlackTree()
        for key in keys:
            rbt.insert(key)

        # Crear el grafo visual del árbol
        G = nx.DiGraph()
        def add_edges(node):
            if node is not None:
                if node.left:
                    G.add_edge(node.val, node.left.val, color='red' if node.left.color == 'red' else 'black')
                    add_edges(node.left)
                if node.right:
                    G.add_edge(node.val, node.right.val, color='red' if node.right.color == 'red' else 'black')
                    add_edges(node.right)
        add_edges(rbt.root)

        # Dibujar el árbol
        pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')
        edge_colors = nx.get_edge_attributes(G, 'color').values()
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_weight='bold', edge_color=edge_colors)
        plt.title("Red-Black Tree")
        output_path = "rb_backend/static/rbtree.png"
        plt.savefig(output_path)
        plt.close()

        return jsonify({"imageUrl": f"http://localhost:5000/static/rbtree.png"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
