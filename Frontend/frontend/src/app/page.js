"use client";
import Image from 'next/image'
import styles from './page.module.css'
import { useEffect, useState } from "react";

function App(){
  useEffect(() => {
    fetch('http://localhost:8000/recommender')
    .then(response => response.json())
    .then(response => console.log(response))
  }, [])
  return (
    <h1>Frontend and backend App</h1>
  );
}

export default App;