
import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import System from './maincomponentes/system'
import Login  from './maincomponentes/login'
import './maincomponentes/componentes-style/index.css'
import { AuthProvider } from './AuthContext';



ReactDOM.createRoot(document.getElementById('root')).render(
  <AuthProvider>
    <React.StrictMode>
      <Router>
        <Routes>
          <Route path="/" element={<Login/>} />
        </Routes>
      </Router>
    </React.StrictMode>
  </AuthProvider>
);
