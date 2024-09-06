import React from "react";
import './componentes-style/header.css'
import { useState } from "react";


function Header(props){
    
    return(
        <>
        <div className="header-container">
            <nav className="nav-container">
                <ul>
                    <li><button onClick={props.funcdashbord} >Dashbord</button></li>
                    <li><button onClick={props.funcbranch}>Branch</button></li>
                    <li><button onClick={props.funcdelivery}>delivery</button></li>
                    <li><button onClick={props.funcbakery}>bakery</button></li>
                    <li><button onClick={props.funcemploye}>employe</button></li>
                    <li><button onClick={props.funcbusiness}>business</button></li>
                    <li><button onClick={props.funcasset}>Asset</button></li>
                    <li><button onClick={props.funccompany}>company</button></li>
                </ul>
            </nav>
        </div>
        </>
    )
}
export default Header;