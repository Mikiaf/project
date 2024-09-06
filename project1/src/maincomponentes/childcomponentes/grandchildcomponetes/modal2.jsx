import React from "react";
import { useState,useEffect } from "react";
import "./grandchildcomponetes-style/modal2.css"



function Modal({children,active,close,func}){

    return active ?(
        <>
        <div className="modal-container">
            <div className="modal">
                {children}
                <div className="modalbutton-container">
                    <button   className="modalbutton" onClick={close}>Delete</button>
                    <button   className="modalbutton" onClick={close}>update</button>
                    <button   className="modalbutton" onClick={close}>Add Asset</button>
                    <button className="modalbutton" onClick={close}>close</button>
                </div>
                <div className="nextbtn-container">
                    <button onClick={func}>next</button>
                </div>
            </div>
        </div>
        </>
    ):""
}

export default Modal;