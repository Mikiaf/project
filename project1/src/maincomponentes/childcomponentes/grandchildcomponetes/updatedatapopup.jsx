import React, { useState } from "react";
import Popup from "../../popupcomponentes/popup1";
import "./grandchildcomponetes-style/updatedatapopup.css";

function Updatedata({ children, active, handlclose, db, type, accept, token, id, selectedcolumn, refresh }) {
    const [activepopup, setactivepopup] = useState(false);
    const [popupMessage, setPopupMessage] = useState('');
    const [password, setpassword] = useState('');
    const [data, setData] = useState(type === 'text' ? '' : undefined);
    const [file, setFile] = useState(null);
    const [selectedvalue, setselectedvalue] = useState('')
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    const togglePopup = async (e) => {
        setactivepopup(!activepopup);
    };

    const handleSubmitData = async (e) => {
        e.preventDefault();
        try {
            const formData = new FormData();
            formData.append('type', db);
            formData.append('id', id);
            formData.append('password', password);
            formData.append('selectedcolumn', selectedcolumn);
            if (type === "file") {
                if (file) {
                    formData.append('image', file);
                } else {
                    throw new Error("No file selected");
                }
            } else {
                formData.append('data', JSON.stringify(data));
            }

            const response = await fetch('http://localhost:5000/api/updatedata', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`
                },
                body: formData
            });
            if (response.ok) {
                const responseData = await response.json();
                setPopupMessage(responseData['message']);
                setactivepopup(true);
                await sleep(1000);
                refresh(token);
            } else {
                const responseData = await response.json();
                setPopupMessage(`Error:${responseData["message"]}`);
                setactivepopup(true);
            }
        } catch (error) {
            setPopupMessage(`Something went wrong.${error}`);
            setactivepopup(true);
        }
    };

    const handleFileChange = (e) => {
        if (type === "file") {
            setFile(e.target.files[0]);
        }
    };
    const handleChange = (event) => {
        const value = event.target.value;
        setselectedvalue(value);
    };
    return active ? (
        <>
            <div className="modal-container">
                <div className="modal">
                    <button className="close-btn" onClick={handlclose}>X</button>
                    {children}
                    <div className="input-container">
                        {type !== "file" && type !== "select" && (
                            <><input
                                type={type}
                                accept={accept}
                                placeholder="Enter new Info"
                                onChange={(e) => setData(e.target.value)}
                                value={data} /><br /></>
                        )}
                        {type === "file" && (
                           <><input
                           type="file"
                           onChange={handleFileChange}
                           className="file-input"
                            /><br/>
                            </> 
                        )}
                        {type === "select" && (
                            <>
                            <select className="wokingpostion-conatiner"value={selectedvalue} onChange={handleChange}>
                                <option value="">Select...</option>
                                <option value="branch">branch</option>
                                <option value="bakery">bakery</option>
                                <option value="delivery">delivery</option>
                                <option value="admin">admin</option>
                            </select><br/>
                            </>
                        )}
                        <input
                            type="password"
                            placeholder="Enter admin password"
                            onChange={(e) => setpassword(e.target.value)}
                            value={password}
                        />
                    </div><br />
                    <button className="submit-btn" onClick={handleSubmitData}>Submit</button>
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
    ) : "";
}

export default Updatedata;
