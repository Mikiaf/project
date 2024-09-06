import React from "react";
import { useState } from "react";
import "./childcomponent-style/bodycompany.css"

function CompanyFullbar(props){
    return(
        <>
            <div className="companyfullbar-container">
                <p>test</p>
            </div>
        </>
    )
}

function Company(props){

    return props.active ?(
       <div className="company-container">
            <CompanyFullbar/>
       </div>
    ) : ""
}

export default Company