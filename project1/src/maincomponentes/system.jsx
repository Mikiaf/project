import React from "react";
import { useState, useEffect } from "react";
import Header from './header';
import Body from "./body";
import './componentes-style/system.css';
import { useAuth } from '../AuthContext';


function System() {
    const [branch, setbranch] = useState(false);
    const [dashbord, setdashbord] = useState(true);
    const [delivery, setdelivery] = useState(false);
    const [bakery, setbakery] = useState(false);
    const [business, setbusiness] = useState(false);
    const [employe, setemploye] = useState(false);
    const [company, setcompany] = useState(false);
    const [asset, setasset] = useState(false);

    const [data, setdata] = useState({});
    const [loading, setloading] = useState(true);
    const [error, seterror] = useState(null);
    const { token } = useAuth();

    useEffect(() => {
        const fetchData = async () => {
            try {
                console.log(`Sending token: Bearer ${token}`); // Debugging print statement
                const response = await fetch('http://localhost:5000/api/outputdata', {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${token}` // Include the token in the Authorization header
                    },
                });

                if (response.ok) {
                    const data = await response.json();
                    setdata(data);
                    setloading(false);
                    console.log('Output data:', data);
                } else {
                    const data = await response.json();
                    seterror(data);
                    console.error('Failed to retrieve data:', data);
                }
            } catch (error) {
                seterror(error);
                setloading(false);
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, [token]); // The empty array ensures the effect runs only once

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

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
        return setasset(true);
    }

    return (
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
                branchdata={data['branchdata']}
                branchproductdata={data['branchproductdata']}
                deliverydata={data['deliverydata']}
                deliveryproductdata={data['deliveryproductdata']}
                bakerydata={data['bakerydata']}
                bakeryproductdata={data['bakeryproductdata']}
                productdata={data['productdata']}
                employeedata={data['employeedata']}
                salarydata={data['salarydata']}
                transactiondata={data['transactiondata']}
                accountdata={data['accountdata']}
                assetdata={data['assetdata']}
                connectiondata={data['connectiondata']}
                costdata={data['costdata']}
                orderdata={data['orderdata']}
                saledata={data['saledata']}
                statusdata={data['statusdata']}
                admindata={data['admindata']}
                
                activebranch={branch}
                activedashbord={dashbord}
                activedeliver={delivery}
                activebakery={bakery}
                activebusiness={business}
                activeemploye={employe}
                activecompany={company}
                activeasset={asset}
            />
        </div>
    )
}

export default System;
