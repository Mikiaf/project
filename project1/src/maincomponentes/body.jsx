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
    console.log(props.token)  
    return(
        <>
        <div className="body-container">
           <Branch
                active = {props.activebranch}
                branchdata = {props.branchdata}
                branchproductdata = {props.branchproductdata}
                branchdaydata={props.branchdaydata}
                branchmonthdata={props.branchmonthdata}
                branchyeardata={props.branchyeardata}
                productdata={props.productdata}
                refresh = {props.refresh}

                token = {props.token}
           />
           <Dashbord
                active = {props.activedashbord}
                transactiondata={props.transactiondata}
                connectiondata={props.connectiondata}
                accountdata = {props.accountdata}
                admindata={props.admindata}
                saledata={props.saledata}
                refresh = {props.refresh}

                token = {props.token}
           />
           <Delivery
                active = {props.activedeliver}
                deliverydata={props.deliverydata}
                deliveryproductdata={props.deliveryproductdata}
                deliverydaydata={props.deliverydaydata}
                deliverymonthdata={props.deliverymonthdata}
                deliveryyeardata={props.deliveryyeardata}
                productdata={props.productdata}
                refresh = {props.refresh}

                token = {props.token}
           />
           <Bakery
                active = {props.activebakery}
                bakerydata={props.bakerydata}
                bakeryproductdata={props.bakeryproductdata}
                bakerydaydata={props.bakerydaydata}
                bakerymonthdata={props.bakerymonthdata}
                bakeryyeardata={props.bakeryyeardata}
                productdata={props.productdata}
                refresh = {props.refresh}

                token = {props.token}
            />
           <Business
                active = {props.activebusiness}
                saledata={props.saledata}
                transactiondata={props.transactiondata}
                salarydata={props.salarydata}
                statusdata={props.statusdata}
                connectiondata={props.connectiondata}
                costdata={props.costdata}
                orderdata={props.orderdata}
                refresh = {props.refresh}

                token = {props.token}

            />
            <Employe
                active = {props.activeemploye}
                employeedata={props.employeedata}
                salarydata={props.salarydata}
                refresh = {props.refresh}

                token = {props.token}
            />
            <Company
                active = {props.activecompany}

                token = {props.token}
            />
            <Asset
                active = {props.activeasset}
                assetdata={props.assetdata}
                costdata={props.costdata}

                token = {props.token}
            />
        </div>
        </>
    )
}
export default Body