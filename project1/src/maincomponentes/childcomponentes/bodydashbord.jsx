import React from "react";
import { useState, useEffect } from "react";

function BranchStatus(props){
    return(
        <>
            <div className="branchstatus-container">

            </div>
        </>
    )
}
function DeliverStatus(props){
    return(
        <>
            <div className="deliverystatus-container">

            </div>
        </>
    )
}
function BakeryStatus(props){
    return(
        <>
            <div className="bakerystatus-container">

            </div>
        </>
    )
}
function EmployeStatus(props){
    return(
        <>
            <div className="employestatus-container">
                
            </div>
        </>
    )
}
function Dashbord(props){
    return props.active ?(
        <>
            <div>
                <p>test</p>
            </div>
        </>
    ):""
}

export default Dashbord;
