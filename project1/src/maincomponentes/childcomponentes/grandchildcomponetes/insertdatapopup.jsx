import React from 'react';
import { useState } from 'react';
import Popup from '../../popupcomponentes/popup1';
import "./grandchildcomponetes-style/insertdatapopup.css"

function InsertData(props){
    const [activepopup, setactivepopup] = useState(false)
    const[popupMessage,setPopupMessage] = useState('')
    const [password,setPassword] = useState('')

    function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }


    const togglePopup = async (e) =>{
      setactivepopup(!activepopup)
    }

    const handleSubmitData = async (e) =>{
        e.preventDefault();
        try {
            const formData = new FormData();
            formData.append('type', props.db);
            formData.append('data', JSON.stringify(props.data));
            formData.append('password', password);
            if (props.selectedImage) {
                formData.append('image', props.selectedImage);
            }
            const response = await fetch('http://localhost:5000/api/insertdata', {
                method: 'POST',
                headers: {
                    //'Content-Type': 'application/json',
                    'Authorization': `Bearer ${props.token}`
                },
                body: formData
            });

            if (response.ok) {
                const responsedata = await response.json();
                setPopupMessage(responsedata['message']);
                setactivepopup(true);
                await sleep(1000);
                props.refresh(props.token)
            } else {
                const data = await response.json();
                setPopupMessage(`Error:${data['message']}`);
                setactivepopup(true);
            }
        } catch (error) {
            setPopupMessage(`Something went wrong.${error}`);
            setactivepopup(true);
        }
    }
  return props.activeinsertdata ? (
    <div className={`insertdata ${props.activeinsertdata ? 'show' : ''}`}>
      <div className="insertdatapopup-content">
      <button className="close-btn" onClick={props.handleclose}>X</button>
      <div>
          {Object.entries(props.data).map(([key, value]) => (
            <p key={key}>{`${key}: ${value}`}</p>
          ))}
        </div>
        <input type='password' placeholder='Enter admin password' onChange={(e) => setPassword(e.target.value)}/>
        <button className='submit-btn'onClick={handleSubmitData}>Submit</button>
        {activepopup && (
                <Popup
                    activepopup={activepopup}
                    handleClose={togglePopup}>
                    <p>{popupMessage}</p>
                </Popup>
            )}
      </div>
    </div>
  ):"";
};

export default InsertData;