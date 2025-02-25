import React from "react";
import { useState,useEffect } from "react";
import "./grandchildcomponetes-style/deletedatapopup.css"
import Popup from "../../popupcomponentes/popup1";


function Deletedata({active,handleclose,db,id,token,refresh}){
    const [password,setpassword] = useState('')
    const [activepopup, setactivepopup] = useState(false)
    const[popupMessage,setPopupMessage] = useState('')



    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    const togglePopup = async (e) =>{
        setactivepopup(!activepopup)
    }
    const handleSubmitData = async (e) =>{
          e.preventDefault();
          try {
              const response = await fetch('http://localhost:5000/api/deletedata', {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json',
                      'Authorization': `Bearer ${token}`
                  },
                  body: JSON.stringify({db,password,id}),
              });
  
              if (response.ok) {
                  const responsedata = await response.json();
                  setPopupMessage(responsedata['message']);
                  setactivepopup(true);
                  await sleep(1000);
                  refresh(token)
              } else {
                  const responsedata = await response.json();
                  setPopupMessage(`Error:${responsedata['message']}`);
                  setactivepopup(true);
              }
          } catch (error) {
              setPopupMessage(`Something went wrong.${error}`);
              setactivepopup(true);
          }
      }

    return active ?(
        <>
        <div className="deletemodal-container">
            <div className="deletemodal">
                <p>you are deleteing all data </p>
                <input 
                    type="password"
                    className="input-container"
                    placeholder="Enter admin password"
                    value={password}
                    onChange={(e)=> setpassword(e.target.value)}
                    />
                <button className="submit-btn" onClick={handleSubmitData}>Submit</button>
                <button className="close-btn" onClick={handleclose}>X</button>
            </div>
        </div>
        {activepopup && (
                <Popup
                    activepopup={activepopup}
                    handleClose={togglePopup}>
                    <p>{popupMessage}</p>
                </Popup>
            )}
        </>
    ):""
}

export default Deletedata;