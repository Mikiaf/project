import React from "react";
import Dashbord from "./childcomponentes/bodydashbord";
import Branch from  "./childcomponentes/bodybranch"
import Delivery from  "./childcomponentes/bodydelivery"
import Bakery from "./childcomponentes/bodybakery"
import Business from "./childcomponentes/bodybusiness";
import Employe from "./childcomponentes/bodyemploye";
import Asset from "./childcomponentes/bodyasset";
import Company from "./childcomponentes/bodycompany";
import { useState, useEffect } from "react";
import "./componentes-style/body.css"

function Body(props){    
    return(
        <>
        <div className="body-container">
           <Branch
                active = {props.activebranch}
           />
           <Dashbord
                active = {props.activedashbord}
           />
           <Delivery
                active = {props.activedeliver}
           />
           <Bakery
                active = {props.activebakery}
            />
           <Business
                active = {props.activebusiness}
            />
            <Employe
                active = {props.activeemploye}
            />
            <Company
                active = {props.activecompany}
            />
            <Asset
                active = {props.activeasset}
            />
        </div>
        </>
    )
}
export default Body