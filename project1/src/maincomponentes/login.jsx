import React, { useState } from 'react';
import Header from './header';
import Body from "./body";
import "./componentes-style/login.css";
import './componentes-style/system.css';
import Popup from './popupcomponentes/popup1';
import { useAuth } from '../AuthContext';

const Login = () => {
    const [branch, setbranch] = useState(false);
    const [dashbord, setdashbord] = useState(true);
    const [delivery, setdelivery] = useState(false);
    const [bakery, setbakery] = useState(false);
    const [business, setbusiness] = useState(false);
    const [employe, setemploye] = useState(false);
    const [company, setcompany] = useState(false);
    const [asset, setasset] = useState(false);


    const [outputdata, setoutputdata] = useState({});
    const [dename, setdename] = useState('');
    const [adminid, setadminid] = useState('');
    const [password, setPassword] = useState('');
    const [activepopup, setactivepopup] = useState(false);
    const [activesystem, setactivesystem] = useState(false)
    const [popupMessage, setPopupMessage] = useState('');
    const [token, setToken] = useState('');


    const [loading, setloading] = useState(false);
    const [error, seterror] = useState(null);
    const togglePopup = () => {
        setactivepopup(!activepopup);
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
                //setToken(data.token); // Save the token
                //console.log(`Token received: ${data.token}`); // Debugging print statement
                setPopupMessage('Login successful');
                setactivepopup(true);
                setToken(data.token)
                console.log(token)
                handleOutputData(data.token)
            } else {
                const data = await response.json();
                setPopupMessage(`Error:${data['message']}`);
                setactivepopup(true);
                console.error('Login failed:', data);
            }
        } catch (error) {
            setPopupMessage('Something went wrong.');
            setactivepopup(true);
            console.error('Error:', error);
        }
    };

    const handleOutputData = async (token) => {
        setloading(true);
        try {
            console.log("Token:", token);
            const response = await fetch('http://localhost:5000/api/outputdata', {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${token}`, // Include the token in the Authorization header
                    'Content-Type': 'application/json'
                },
            });

            if (response.ok) {
                const data = await response.json();
                setoutputdata(data)
                setactivesystem(true)
                //setloading(false);
                console.log('Output data:', data);
            } else {
                const data = await response.json();
                setPopupMessage('Failed to retrieve data.');
                setactivepopup(true);
                seterror(data);
                console.error('Failed to retrieve data:', data);
            }
        } catch (error) {
            setPopupMessage('Error retrieving data.');
            setactivepopup(true);
            console.error('Error:', error);
        } finally {
            setloading(false);
        }
    };
//////////////////////////////////////////////
    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }
//////////////////////////////////////////
    function activebranch() {
        setdashbord(false);
        setdelivery(false);
        setemploye(false);
        setbakery(false);
        setbusiness(false);
        setcompany(false);
        setasset(false);
        return setbranch(true);
    }

    function activedashbord() {
        setbranch(false);
        setdelivery(false);
        setbakery(false);
        setemploye(false);
        setbusiness(false);
        setcompany(false);
        setasset(false);
        return setdashbord(true);
    }

    function activedelivery() {
        setbranch(false);
        setdashbord(false);
        setbakery(false);
        setemploye(false);
        setbusiness(false);
        setcompany(false);
        setasset(false);
        return setdelivery(true);
    }

    function activebakery() {
        setbranch(false);
        setdashbord(false);
        setdelivery(false);
        setemploye(false);
        setbusiness(false);
        setcompany(false);
        setasset(false);
        return setbakery(true);
    }

    function activebusiness() {
        setbranch(false);
        setdashbord(false);
        setdelivery(false);
        setbakery(false);
        setemploye(false);
        setcompany(false);
        setasset(false);
        return setbusiness(true);
    }

    function activeemploye() {
        setdashbord(false);
        setdelivery(false);
        setbakery(false);
        setbusiness(false);
        setbranch(false);
        setcompany(false);
        setasset(false);
        return setemploye(true);
    }

    function activecompany() {
        setdashbord(false);
        setdelivery(false);
        setbakery(false);
        setbusiness(false);
        setbranch(false);
        setemploye(false);
        setasset(false);
        return setcompany(true);
    }

    function activeasset() {
        setdashbord(false);
        setdelivery(false);
        setbakery(false);
        setbusiness(false);
        setbranch(false);
        setemploye(false);
        setcompany(false);
        return setasset(true)
    }
    return (
        <>
          {!activesystem &&(  
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

            {activepopup && (
                <Popup
                    activepopup={activepopup}
                    handleClose={togglePopup}>
                    <p>{popupMessage}</p>
                </Popup>
            )}
            </div>
        )}
        
            {activesystem && (
                        <div className="system-container">
                            <Header
                                funcbranch={activebranch}
                                funcdashbord={activedashbord}
                                funcdelivery={activedelivery}
                                funcbakery={activebakery}
                                funcbusiness={activebusiness}
                                funcemploye={activeemploye}
                                funccompany={activecompany}
                                funcasset={activeasset}
                            />
                            <Body
                                branchdata={outputdata['branchdata']}
                                branchproductdata={outputdata['branchproductdata']}
                                branchdaydata={outputdata['branchdaydata']}
                                branchmonthdata={outputdata['branchmonthdata']}
                                branchyeardata={outputdata['branchyeardata']}
                                deliverydata={outputdata['deliverydata']}
                                deliveryproductdata={outputdata['deliveryproductdata']}
                                deliverydaydata={outputdata['deliverydaydata']}
                                deliverymonthdata={outputdata['deliverymonthdata']}
                                deliveryyeardata={outputdata['deliveryyeardata']}
                                bakerydata={outputdata['bakerydata']}
                                bakeryproductdata={outputdata['bakeryproductdata']}
                                bakerydaydata={outputdata['bakerydaydata']}
                                bakerymonthdata={outputdata['bakerymonthdata']}
                                bakeryyeardata={outputdata['bakeryyeardata']}
                                productdata={outputdata['productdata']}
                                employeedata={outputdata['employeedata']}
                                salarydata={outputdata['salarydata']}
                                transactiondata={outputdata['transactiondata']}
                                accountdata={outputdata['accountdata']}
                                assetdata={outputdata['assetdata']}
                                connectiondata={outputdata['connectiondata']}
                                costdata={outputdata['costdata']}
                                orderdata={outputdata['orderdata']}
                                saledata={outputdata['saledata']}
                                statusdata={outputdata['statusdata']}
                                admindata={outputdata['admindata']}
                                
                                activebranch={branch}
                                activedashbord={dashbord}
                                activedeliver={delivery}
                                activebakery={bakery}
                                activebusiness={business}
                                activeemploye={employe}
                                activecompany={company}
                                activeasset={asset}
                                
                                refresh = {handleOutputData}

                                token={token}
                            />
                    </div>
            )}
    </>
    );
};

export default Login;
