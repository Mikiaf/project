import React from 'react';
import './popupstyle/popup1.css'// Add some styling for the popup

function Popup(props){
  return props.activepopup ? (
    <div className={`popup ${props.activepopup ? 'show' : ''}`}>
      <div className="popup-content">
        <button className="close-btn" onClick={props.handleClose}>X</button>
        {props.children}
      </div>
    </div>
  ):"";
};

export default Popup;