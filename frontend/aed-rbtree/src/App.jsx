import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { createNodes, deleteNodes, clearTree}  from './api/requests'

// https://colorhunt.co/palette/f6f1f1afd3e219a7ce146c94

function App() {

  const [postKeys, setPostKeys] = useState("");

  const [imageUrl, setImageUrl] = useState(`http://localhost:5000/static/rbtree.png?timestamp=${new Date().getTime()}`);

  const [min, setMin] = useState(0);
  const [max, setMax] = useState(100);
  const [num, setNum] = useState(10);

  const updateImage = () => {
    setImageUrl(`http://localhost:5000/static/rbtree.png?timestamp=${new Date().getTime()}`)
  }

  const handleGenerateRandom = async () => {
    const list = [];
    for(let i = 0; i < num; i++) {
      list.push(Math.floor(Math.random() * (max - min + 1)) + min);
    }
    setPostKeys(list.join(" "));
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
    if(postKeys === "" || postKeys.charAt(postKeys.length - 1) === "," || postKeys.charAt(postKeys.length - 1) === " " || postKeys.charAt(0) === "," || postKeys.charAt(0) === " ") {
      return;
    }

    const list = postKeys.split(/\s*,\s*|\s+/).map(Number);
    if(list.some(isNaN)) {
      return;
    }

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

  const handleChangeMin = (event) => {
    const value = event.target.value;
    setMin(value);
  }

  const handleChangeMax = (event) => {
    const value = event.target.value;
    setMax(value);
  }

  const handleChangeNum = (event) => {
    const value = event.target.value;
    setNum(value);
  }

  return (
    <div style={{display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', width: '100vw'}}>
      <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', backgroundColor: '#27496D', 'width': '100%'}}>
        <h1 style={{color:'#F6F1F1'}}>
          Red-Black Tree
        </h1>
      </div>
      <div>
        <img style={{width: '100%', objectFit: 'cover'}} src={imageUrl}/>
      </div>
      <div style={{padding: '10px', display: 'flex', alignItems: 'end'}}>
        <div style={{margin: '0px 8px', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center'}}>
          <p style={{margin: '0px 0px'}}>Mín</p>
          <input value={min} onChange={handleChangeMin} style={{backgroundColor: '#146C94', border: '2px solid #27496D', borderRadius: '4px', width:'30px', height:'20px', padding: '8px 12px'}}/>
        </div>
        <div style={{margin: '0px 8px', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center'}}>
          <p style={{margin: '0px 0px'}}>Máx</p>
          <input value={max} onChange={handleChangeMax} style={{backgroundColor: '#146C94', border: '2px solid #27496D', borderRadius: '4px', width:'30px', height:'20px', padding: '8px 12px'}}/>
        </div>
        <div style={{margin: '0px 8px', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center'}}>
          <p style={{margin: '0px 0px'}}>Num</p>
          <input value={num} onChange={handleChangeNum} style={{backgroundColor: '#146C94', border: '2px solid #27496D', borderRadius: '4px', width:'30px', height:'20px', padding: '8px 12px'}}/>
        </div>
        <button onClick={handleGenerateRandom} style={{margin: '0px 8px'}}>
          Generar aleatorios
        </button>
        <div style={{border: '1px solid #27496D'}}/>
        <div style={{margin: '0px 8px', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center'}}>
          <p style={{margin: '0px 0px'}}>Nodos</p>
          <input value={postKeys} onChange={handleChange} style={{backgroundColor: '#146C94', border: '2px solid #27496D', borderRadius: '4px', width:'300px', height:'20px', padding: '8px 12px'}}/>
        </div>
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
