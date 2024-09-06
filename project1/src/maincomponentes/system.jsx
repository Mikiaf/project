import React from "react";
import { useState, useEffect } from "react";
import Header from './header'
import Body from "./body";
import data from "./data";
import './componentes-style/system.css'

 //bodybarnche function
function System(){

   const [branch, setbranch] = useState(false)
   const [dashbord, setdashbord] = useState(true)
   const [delivery, setdelivery] = useState(false)
   const [bakery, setbakery] = useState(false)
   const [business, setbusiness] = useState(false)
   const [employe, setemploye] = useState(false)
   const [company, setcompany] = useState(false)
   const [asset, setasset] = useState(false)


   function activebranch(){
        setdashbord(false)
        setdelivery(false)
        setemploye(false)
        setbakery(false)
        setbusiness(false)
        setcompany(false)
        setasset(false)
        return setbranch(true)
   }
   function activedashbord(){
        setbranch(false)
        setdelivery(false)
        setbakery(false)
        setemploye(false)
        setbusiness(false)
        setcompany(false)
        setasset(false)
        return setdashbord(true)
   }
   function activedelivery(){
    setbranch(false)
    setdashbord(false)
    setbakery(false)
        setemploye(false)
        setbusiness(false)
        setcompany(false)
        setasset(false)
    return  setdelivery(true)
}
    function activebakery(){
        setbranch(false)
        setdashbord(false)
        setdelivery(false)
        setemploye(false)
        setbusiness(false)
        setcompany(false)
        setasset(false)
        return  setbakery(true)
    }
    function activebusiness(){
        setbranch(false)
        setdashbord(false)
        setdelivery(false)
        setbakery(false)
        setemploye(false)
        setcompany(false)
        setasset(false)
        return  setbusiness(true)
    }
    function activeemploye(){
        setdashbord(false)
        setdelivery(false)
        setbakery(false)
        setbusiness(false)
        setbranch(false)
        setcompany(false)
        setasset(false)
        return setemploye(true)
   }
   function activecompany(){
        setdashbord(false)
        setdelivery(false)
        setbakery(false)
        setbusiness(false)
        setbranch(false)
        setemploye(false)
        setasset(false)
        return setcompany(true)
   }
   function activeasset(){
    setdashbord(false)
    setdelivery(false)
    setbakery(false)
    setbusiness(false)
    setbranch(false)
    setemploye(false)
    setcompany(false)
    return setasset(true)
}
    return(
        <div className="system-container">
            <Header
                funcbranch = {activebranch}
                funcdashbord = {activedashbord}
                funcdelivery = {activedelivery}
                funcbakery = {activebakery}
                funcbusiness = {activebusiness}
                funcemploye = {activeemploye}
                funccompany = {activecompany}
                funcasset = {activeasset}
            />
            <Body 
                activebranch = {branch}
                activedashbord = {dashbord}
                activedeliver = {delivery}
                activebakery = {bakery}
                activebusiness = {business}
                activeemploye = {employe}
                activecompany = {company}
                activeasset = {asset}
            />
        </div>
    )
}

export default System;