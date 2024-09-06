import React, { useState, useEffect } from "react";
import "./childcomponent-style/bodybranch.css"
import Modal from "./grandchildcomponetes/modal1"
///branch componentes


///mainbar access sidebar
function BranchMainbar(props){
    return(
        <>
            <div className="branchmainbar-container">
                <button onClick={props.funcmain}>Main</button><br></br>
                <button onClick={props.funcadd}>Add branch</button><br></br>
                <button onClick={props.funcbranchinfo}>FullBranch Info</button>
                <button onClick={props.funcacceptedpro}>Accepted Products</button>
            </div>
        </>
    )
}

///sidebar info telling component
function BranchSidebar(props){
                function Branchinfocomponentes(props){
                    function Branches(){
                        return(
                        <>
                            <div className="generalinfoP-container">
                                <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                            width: "300px"
                            }}>All information about branches and there sale status</p>
                            </div>
                            <div className="sbranches-container">
                                <div className="searche-container">
                                    <input type="text" placeholder="searche"/>
                                </div>
                                <div className="table-container">
                                    <table>
                                        <thead>
                                            <tr>
                                                <th>Id</th>
                                                <th>BranchName</th>
                                                <th>ControlersId</th>
                                                <th>TotalWorkers</th>
                                                <th>Location</th>
                                                <th>branchStartingDate</th>
                                                <th>TotalAcceptedProducts</th>
                                                <th>BranchTotalSaleIn$</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>tebasi barnch branch</td>
                                                <td>mikiyas afework afework</td>
                                                <td>test</td>
                                                <td>1</td>
                                                <td>1</td>
                                                <td>1</td>
                                            </tr>
                                            <tr>
                                                <td>tebasi barnch branch</td>
                                                <td>mikiyas afework afework</td>
                                                <td>test</td>
                                                <td>1</td>
                                                <td>1</td>
                                                <td></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </>
                        )
                    }
                    function BranchMainInfo(){
                        const images = [
                                {uri:"image.jpg",
                                 titel:"i1"
                                },
                                {uri:"OIP.jpg",
                                titel:"i1"
                               }
                        ]
                        const [active, setactive] = useState(false)
                        const [currentindex, setindex] = useState(0)
                        function nextbtn(){
                            currentindex == 0 ? setindex(1) : setindex(0)
                        }
                        console.log(images.length)
                        const slidestyle = {
                            backgroundImage:`url(${images[currentindex].uri})`,
                            width:'100%',
                            height:'100%',
                            backgroundPosition:'center',
                            backgroundSize:'cover',
                        }

                        return(
                            <>
                            <div className="generalinfoP-container">
                                <p>information about branches</p>
                            </div>
                            <div className="maininfo-container">
                                <p>test maininfo</p>
                                <div className="managebranch-buttoncontainer">
                                    <button className="managebranch-button" onClick={() =>setactive(true)}>Manage Branch</button>
                                    <Modal active={active}  func = {nextbtn} close = {()=> setactive(false)}>
                                        <div className="updatebranch-container">
                                        <div className="updatebranchinput-container">
                                            <p>update branch information or delete branch</p>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/>
                                        </div>
                                            <div className="updatebranchImg-container">
                                                <div className="slide" style={slidestyle}></div>
                                            </div>
                                            
                                        </div>
                                    </Modal>
                                </div>
                            </div>
                            </>
                        )
                   }
                    function BranchStatus(){
                        return(
                            <>
                            <div className="generalinfoP-container">
                                <p style={{backgroundColor: "rgba(211, 159, 224, 0.966)"}}>status about branches</p>
                            </div>
                                <div className="status-container">
                                    <p>test status</p>
                                </div>
                            </>
                        )
                    }
                    return props.active?(
                        <> 
                            <div className="fullbranchinfo-container">
                                <Branches/>
                                <BranchMainInfo/>
                                <BranchStatus/>
                            </div>
                        </>
                    ):""
                }
                function Addbranchcomponentes(props){
                    function Doneinfo(){
                        return(
                            <>
                                <div className="generalinfoP-container">
                                    <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)"}}>user submited branch information</p>
                                </div>
                                <div className="doneinfo-contaner">
                                    <div className="submitedinfo-container">
                                        <p>test</p>
                                    </div>
                                </div>
                            </>
                        )
                    }
                    function Forminfo(){
                        return(
                            <>
                                <div className="generalinfoP-container">
                                    <p>submit information about branch</p>
                                </div>
                                <div className="forminfo-container">
                                    <form className="forminput-container">
                                            <input type="text" placeholder="Enter branch name"/><br/>
                                            <input type="text" placeholder="Enter branch location"/><br/>
                                            <input type="text" placeholder="Enter branch controler"/><br/>
                                            <input type="number" placeholder="Enter delivery id"/><br/>
                                            <input type="text" placeholder="Enter Branch type"/><br/>
                                            <input type="text" placeholder="Enter Branch sell goal"/><br/>
                                            <button>submit</button>
                                    </form>
                                </div>
                            </>
                        )
                    }

                    return props.active ?(
                        <>
                            <div className="addbranch-container">
                                <Doneinfo/>
                                <Forminfo/>
                            </div>
                        </>
                    ):""
                }
                function SidebarMaincomponentes(props){
                    function GeneralInfoTable(){
                        return(
                            <>
                                <div className="generalinfoP-container">
                                    <p style={{width:"240px"}}>Mothly and yearly status about branches</p>
                                </div>
                                <div className="generalinfoTable-container">
                                <table>
                                        <thead>
                                            <tr>
                                                <th>BranchName</th>
                                                <th>M.ProductQuantity</th>
                                                <th>M.TotalWorkingHour</th>
                                                <th>M.TotalSale</th>
                                                <th>M.TotalSaleGoal</th>
                                                <th>y.TotalWorkingHour</th>
                                                <th>y.TotalSale</th>
                                                <th>y.TotalSaleGoal</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>tebasi branch branch</td>
                                                <td>1</td>
                                                <td>1</td>
                                                <td>1</td>
                                                <td>1</td>
                                                <td>a=5 b=7 c=8 d=8 e=6 f=8 g=9 h=5</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </>
                        )
                    }

                    function TodayInfoTable(){
                        return(
                            <>
                                <div className="todayinfoP-container">
                                    <p>Today status about branches</p>
                                </div>
                                 <div className="todayinfoTable-container">
                                <table>
                                        <thead>
                                            <tr>
                                                <th>BranchName</th>
                                                <th>Deliver'sVicalPlate</th>
                                                <th>TimeOfDelivery</th>
                                                <th>ProductQuantity</th>
                                                <th>DayWorkingHour</th>
                                                <th>DaySale</th>
                                                <th>DaySaleGoal</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>tebasi branch barnch</td>
                                                <td>{props.data}</td>
                                                <td>1</td>
                                                <td>1</td>
                                                <td>1</td>
                                                <td>1</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </>
                        )
                    }
                    return props.active ?(
                       <>
                            <div className="mainbranchinfo-container">
                                <GeneralInfoTable/>
                                <TodayInfoTable/>
                            </div>
                       </>
                    ):""
                }
                function AcceptedProducts(props){
                    function ProductsGraph(props){
                        return(
                            <>
                            <div className="generalinfoP-container">
                                <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                            width: "330px"
                            }}>All information about accepted products status with graph</p>
                            </div>
                                <div className="productsgraph-container">

                                </div>
                            </>
                        )
                    }
                    function ProductsTable(props){
                        return(
                            <>
                            <div className="generalinfoP-container">
                                <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                            width: "290px"
                            }}>All information about Accepted  products with tables</p>
                            </div>
                                <div className="productstable-container">
                                <table>
                                        <thead>
                                            <tr>
                                                <th>ProductName</th>
                                                <th>BranchName</th>
                                                <th>TotalProductAccepted</th>
                                                <th>TotalProductSelled</th>
                                                <th>AcceptedTime</th>
                                                <th>DeliveryId</th>
                                                <th>BranchSaleIn$</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td>tebasi barnch branch</td>
                                                <td>mikiyas afework afework</td>
                                                <td>test</td>
                                                <td>1</td>
                                                <td>1</td>
                                                <td>1</td>
                                            </tr>
                                            <tr>
                                                <td>tebasi barnch branch</td>
                                                <td>mikiyas afework afework</td>
                                                <td>test</td>
                                                <td>1</td>
                                                <td>1</td>
                                                <td></td>
                                            </tr>
                                        </tbody>
                                    </table>    
                                </div>
                            </>
                        )
                    }
                    return props.active ?(
                        <>
                            <div className="acceptedproducts-container">
                                <ProductsGraph/>
                                <ProductsTable/>
                            </div>
                        </>
                    ) : ""
                }
    return(
        <>
        <div className="branchsidebar-container">
            <SidebarMaincomponentes
                active = {props.activemain}
            />
            <Addbranchcomponentes
                active = {props.activeadd}
            />
            <Branchinfocomponentes 
                active = {props.activebranchinfo}
            />
            <AcceptedProducts
                active = {props.activeacctedpro}
            />
        </div> 
        </>
    )
}



function Branch(props){
   const [main, setmain] = useState(true)
   const [add, setadd] = useState(false)
   const [branchinfo, setbranchinfo] = useState(false)
   const [accetedpro, setaccetedpro] = useState(false)

   function activemainsidebar(){
        setadd(false)
        setbranchinfo(false)
        setaccetedpro(false)
        return setmain(true)
   }
   function activeaddbranch(){
            setmain(false)
            setbranchinfo(false)
            setaccetedpro(false)
            return setadd(true)

   }
   function activebranchinfo(){
            setmain(false)
            setadd(false)
            setaccetedpro(false)
            return setbranchinfo(true)
   }
   function activeacctedpro(){
            setmain(false)
            setadd(false)
            setbranchinfo(false)
            return setaccetedpro(true)
    }
    return props.active ?(
        <>
            <div className="branch-container">
                <BranchMainbar
                    funcmain = {activemainsidebar}
                    funcadd = {activeaddbranch}
                    funcbranchinfo= {activebranchinfo}
                    funcacceptedpro = {activeacctedpro}
                />
                <BranchSidebar
                    activemain = {main}
                    activeadd = {add}
                    activebranchinfo = {branchinfo}
                    activeacctedpro = {accetedpro}
                />
            </div>
        </>
    ):""
}

export default Branch;