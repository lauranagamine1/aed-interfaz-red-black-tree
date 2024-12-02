const URL = "http://localhost:5000/api/v1"

export async function createNodes(keys) {

    const data = {
        "keys": keys
    }

    await fetch(`${URL}/rbtree/keys`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }, body: JSON.stringify(data)

    });
}

export async function deleteNodes(keys) {

    const data = {
        "keys": keys
    }

    await fetch(`${URL}/rbtree/keys`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }, body: JSON.stringify(data)

    });
}

export async function clearTree() {
    await fetch(`${URL}/rbtree/clear`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    });
}