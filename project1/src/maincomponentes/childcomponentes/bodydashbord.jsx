import React from "react";
import { useState, useEffect } from "react";
import './childcomponent-style/bodydashbord.css'
import DashbordAccount from "./grandchildcomponetes/dashbordaccountpopup";
import DashbordAdmin from "./grandchildcomponetes/dashbordadminpopup";


function DashbordSidebar(props){


    function LiveActionStatus(props){
        function ActionStatus(props){
            const [activetransaction, setactivetransaction] = useState(true)
            const [activesales, setactivesales] = useState(false)

            const handletransaction = async (e) => {
                setactivetransaction(true);
                setactivesales(false);
              }
            const handlesale = async (e) => {
                setactivetransaction(false);
                setactivesales(true);
              }
                return(
                    <>
                        <div className="actionstatus-container">
                                <button className= "transaction-btn"onClick={handletransaction}>Transaction</button>
                                <button className="sales-btn" onClick={handlesale}>Sales</button>
                            
                            {activetransaction &&                 
                                <div className="transactiontable-container">
                                <table>
                                        <thead>
                                            <tr>
                                                <th>TransactionId</th>
                                                <th>BakeryName</th>
                                                <th>DeliverName</th>
                                                <th>BranchName</th>
                                                <th>StageName</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>tebasi branch</td>
                                                <td>{props.branchdata}</td>
                                                <td>tebasi branch</td>
                                                <td>tebasi branch</td>
                                                <td>tebasi branch</td>
                                            </tr>
                                        </tbody>
                                    </table>
                            </div>
                            }
                            {activesales &&                             
                                <div className="salestable-container">
                                <table>
                                        <thead>
                                            <tr>
                                                <th>TransactionId</th>
                                                <th>BakeryName</th>
                                                <th>DeliverName</th>
                                                <th>BranchName</th>
                                                <th>StageName</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>tebasi branch brach</td>
                                                <td>{props.branchdata}</td>
                                                <td>tebasi branch</td>
                                                <td>1</td>
                                                <td>1</td>
                                            </tr>
                                        </tbody>
                                    </table>
                            </div>}
                        </div>
                    </>
                )
        }
        function NotificationStatus(props){
            return(
                <>
                    <div className="notification-container">
                        
                    </div>
                </>
            )
        }
        return(
            <>
                <div className="liveactionstatus-container">
                    <NotificationStatus/>
                    <ActionStatus/>
                </div>
            </>
        )
    }
    function BussinessStatus(props){
                function Graph(props){
                    return(
                        <>
                            <div className="graph-container">

                            </div>
                        </>
                    )
                }
                function DepartmentStatus(props){
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
                    return(
                        <>
                            <div className="departmentstatus-container">
                                <BranchStatus/>
                                <DeliverStatus/>
                                <BakeryStatus/>
                            </div>
                        </>
                    )
                }
                return(
                    <>
                        <div className="bussinessstatus-container">
                            <Graph/>
                            <DepartmentStatus/>
                        </div>
                    </>
                )
            }
    return(
        <>
            <div className="dashbordsidebar-container">
                <LiveActionStatus/>
                <BussinessStatus/>
            </div>
        </>
    )
}
function Dashbord(props){
    const [activedashbordaccount, setactivedashbordacount] =  useState(false)
    const [activedashbordadmin, setactivedashbordadmin] =  useState(false)
    const handlecloseaccount = async (e) => {
        setactivedashbordacount(!activedashbordaccount);
      };
    const handlecloseadmin = async (e) => {
        setactivedashbordadmin(!activedashbordadmin);
      };
    return props.active ?(
        <>
            <div className="dashbord-container">
                <div className="mainbarbutton-container">
                        <button className="admin-btn" onClick={() => setactivedashbordadmin(true)}>Admin</button>
                        <button className="account-btn"onClick={() => setactivedashbordacount(true)}>Account</button>
                </div>
                <div className="sidebarbutton-container">
                        <button onClick={props.funcasset}>Day</button>
                        <button onClick={props.funcasset}>Month</button>
                        <button onClick={props.funcasset}>6month</button>
                        <button onClick={props.funcasset}>Year</button>
                </div>
                <DashbordSidebar/>

                <DashbordAccount
                    active={activedashbordaccount}
                    accountdata={props.accountdata}
                    refresh = {props.refresh}
                    token = {props.token}
                    handleclose={handlecloseaccount}
                />
                <DashbordAdmin
                    active={activedashbordadmin}
                    admindata={props.admindata}
                    refresh = {props.refresh}
                    token = {props.token}
                    handleclose={handlecloseadmin}
                />
            </div>
        </>
    ):""
}

export default Dashbord;
