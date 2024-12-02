import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { createNodes, deleteNodes, clearTree}  from './api/requests'

// https://colorhunt.co/palette/14285027496d0c7b9300a8cc

function App() {

  const [postKeys, setPostKeys] = useState("");

  const [imageUrl, setImageUrl] = useState(`http://localhost:5000/static/rbtree.png?timestamp=${new Date().getTime()}`);

  const updateImage = () => {
    setImageUrl(`http://localhost:5000/static/rbtree.png?timestamp=${new Date().getTime()}`)
  }

  const handleCreateNodes = async () => {
    if(postKeys === "" || postKeys.charAt(postKeys.length - 1) === "," || postKeys.charAt(postKeys.length - 1) === " " || postKeys.charAt(0) === "," || postKeys.charAt(0) === " ") {
      return;
    }

    const list = postKeys.split(/\s*,\s*|\s+/).map(Number);
    if(list.some(isNaN)) {
      return;
    }

    await createNodes(list);
    updateImage();
    setPostKeys("");
  }

  const handleDeleteNodes = async () => {
    const list = postKeys.split(', ').map(Number);
    await deleteNodes(list);
    updateImage();
    setPostKeys("");
  }

  const handleClearTree = async () => {
    await clearTree();
    updateImage();
  }

  const handleChange = (event) => {
    const value = event.target.value;
    setPostKeys(value);
  }

  return (
    <div style={{display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', width: '100vw'}}>
      <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', backgroundColor: '#27496D', 'width': '100%'}}>
        <h1 style={{color:'#F6F1F1'}}>
          Red-Black Tree
        </h1>
      </div>
      <div>
        <img src={imageUrl}/>
      </div>
      <div style={{padding: '10px'}}>
        <input value={postKeys} onChange={handleChange} style={{backgroundColor: '#146C94', border: '2px solid #27496D', padding: '8px 12px', borderRadius: '4px', margin: '0px 8px'}}/>
        <button onClick={handleCreateNodes} style={{margin: '0px 8px'}}>
          Insertar nodos
        </button>
        <button onClick={handleDeleteNodes} style={{margin: '0px 8px'}}>
          Eliminar nodos
        </button>
      </div>
      <div style={{padding: '10px'}}>
      <button onClick={handleClearTree}>
          Limpiar árbol
        </button>
      </div>
    </div>
  )
}

export default App
