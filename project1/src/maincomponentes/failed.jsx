import React, { useState } from 'react';
import "./componentes-style/login.css";
import Popup from './popupcomponentes/popup1';
import { useAuth } from '../AuthContext';

const Login = () => {
    const [dename, setdename] = useState('');
    const [adminid, setadminid] = useState('');
    const [password, setPassword] = useState('');
    const [active, setActive] = useState(false);
    const [popupMessage, setPopupMessage] = useState('');
    const { token ,setToken } = useAuth();

    const togglePopup = () => {
        setActive(!active);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://localhost:5000/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ dename, adminid, password }),
            });
                
            if (response.ok) {
                const data = await response.json();
                setToken(data.token); // Save the token
                console.log(`Token received: ${data.token}`); // Debugging print statement
                setPopupMessage('Login successful');
                setActive(true);
                //window.location.href = '/system'; // Redirect on success
            } else {
                const data = await response.json();
                setPopupMessage('Something went wrong. Check dename, deid, and password.');
                setActive(true);
                console.error('Login failed:', data);
            }
        } catch (error) {
            setPopupMessage('Something went wrong.');
            setActive(true);
            console.error('Error:', error);
        }
    };

    return (
        <div className='login_container'>
            <h2>Login Page</h2>
            <form onSubmit={handleSubmit}>
                <div className='field_contaienr'>
                    <label>dename:</label>
                    <input
                        type="text"
                        value={dename}
                        onChange={(e) => setdename(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>admin id:</label>
                    <input
                        type="number"
                        value={adminid}
                        onChange={(e) => setadminid(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Login</button>
            </form>

            {active && (
                <Popup
                    active={active}
                    handleClose={togglePopup}>
                    <p>{popupMessage}</p>
                </Popup>
            )}
        </div>
    );
};

export default Login;
