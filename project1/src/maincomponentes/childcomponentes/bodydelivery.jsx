import React from "react";
import { useState,useEffect } from "react";
import './childcomponent-style/bodydelivery.css'
import Modal from "./grandchildcomponetes/modal1";

function DeliveryMainbar(props){
    return(
        <>
            <div className="deliverymainbar-container">
                <button onClick={props.funcmain}>Main</button><br></br>
                <button onClick={props.funcadd}>Add delivery</button><br></br>
                <button onClick={props.funcdeliverinfo}>FullDelivery Info</button>
                <button onClick={props.funcdeliveredpro}>Deliverd Products</button>
            </div>
        </>
    )
}
function DeliverySidebar(props){
    
        function SidebarMainComponente(props){
            function GenearalInfoTable(props){
                return(
                    <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgba(158, 167, 132, 0.966)", width:'220px'}}>Mothly and yearly status about delivery</p>
                    </div>
                    <div className="generalinfotable-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>DriversName</th>
                                    <th>Vical'sPlate</th>
                                    <th>VicalType</th>
                                    <th>BakeryName</th>
                                    <th>M.TotalAcceptedProductIn$</th>
                                    <th>M.TotaldeliveredProductIn$</th>
                                    <th>M.workingHour</th>
                                    <th>y.TotalAcceptedProduct</th>
                                    <th>y.TotalDeliveredProduct</th>
                                    <th>y.workingHour</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>22</td>
                                    <td>22</td>
                                    <td>22</td>
                                    <td>22</td>
                                    <td>22</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    </>
                )
            }
            function TodayinfoTable(props){
                return(
                    <>
                        <div className="infoP-container">
                            <p style={{backgroundColor:"rgba(172, 203, 185, 0.966)"}}>Today status about delivery</p>
                        </div>
                        <div className="todayinfotable-container">
                        <table>
                                            <thead>
                                                <tr>
                                                    <th>DriversName</th>
                                                    <th>Vical'sPlate</th>
                                                    <th>DayAccpetedProductIn$</th>
                                                    <th>DayDeliveredProductsIn$</th>
                                                    <th>TimeofDelivery</th>
                                                    <th>BranchID</th>
                                                    <th>BakeryID</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                <tr>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                </tr>
                                                <tr>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                </tr> <tr>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                </tr> <tr>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                    <td>1</td>
                                                </tr> <tr>
                                                    <td>1</td>
                                                    <td>1</td>
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
                    <div className="maindeliverinfo-container">
                        <GenearalInfoTable/>
                        <TodayinfoTable/>
                    </div>
                </>
            ):""
        }
        function AddDeliverComponente(props){
            function DoneInfo(props){
                return(
                    <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)", width:"250px"}}>user submited delivery information</p>
                    </div>
                    <div className="doneinfo-container">
                        <div className="submitedforminfo-container">
                            <p>test</p>
                        </div>
                    </div>
                    </>
                )
            }
            function FormInfo(props){
                return(
                    <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgba(155, 179, 224, 0.555)", width:"250px"}}>submit information about the new delivery</p>
                    </div>
                    <div className="forminfo-container">
                        <div className="forminput-container">
                            <input type="text" placeholder="Enter driver name"/><br/>
                            <input type="text" placeholder="Enter driver name"/><br/>
                            <input type="text" placeholder="Enter vical type"/><br/>
                            <input type="number" placeholder="Enter bekery id"/><br/>
                            <button>submit</button>
                        </div>
                    </div>
                    </>
                )
            }
            return props.active ?(
                <>
                <div className="adddeliver-container">
                        <DoneInfo/>
                        <FormInfo/>
                </div>
                </>
            ) : ""
        }
        function FullDeliverInfoComponente(props){
            function Delivery(props){
                return(
                <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgb(205, 170, 207)", width:"300px"}}>All information about delivery and there delivery status</p>
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
                                        <th>DriverName</th>
                                        <th>Vical'sPlate</th>
                                        <th>Vical'sType</th>
                                        <th>WorkingBekeryName</th>
                                        <th>TotalAccpetedProductIn$</th>
                                        <th>TotaldeliverdProductIn$</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                    </tr>
                                    <tr>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                    </tr>
                                    <tr>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                    </tr>
                                    <tr>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                    </tr>
                                    <tr>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                    </tr> 
                                    <tr>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                        <td>1</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </>
                )
            }
            function DeliveryMainInfo(){
                const images = [
                    {uri:"image.jpg",
                     titel:"i1"
                    },
                    {uri:"OIP.jpg",
                    titel:"i1"
                   }
            ]
                const [active, setactive] = useState(false)
                const [currentindex, setindex] = useState(1)
                function nextbtn(){
                    currentindex === 0 ? setindex(1) : setindex(0)
                }
                const slidestyle = {
                    backgroundImage:`url(${images[currentindex].uri})`,
                    width:'100%',
                    height:'100%',
                    backgroundPosition:'center',
                    backgroundSize:'cover',
                }
                return(
                    <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgba(178, 206, 216, 0.966)", width:"200px"}}>information about delivery</p>
                    </div>
                    <div className="maininfo-container">
                        <p>test maininfo</p>
                                <div className="managedelivery-buttoncontainer">
                                    <button className="managedelivery-button"onClick={()=> setactive(true)}>Manage Delivery</button>
                                </div>
                                <Modal active={active} func ={nextbtn} close = {()=> setactive(false)}>
                                <div className="updatedelivery-container">
                                        <div className="updatedeliveryinput-container">
                                            <p>update branch information or delete delivery</p>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/>
                                        </div>
                                            <div className="updatedeliveryImg-container">
                                                <div className="slide" style={slidestyle}></div>
                                            </div>
                                        </div>
                                </Modal>
                    </div>
                    </>
                )
           }
           function DeliveryStatus(){
            return (
                <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgba(178, 206, 216, 0.966)", width:"250px"}}> delivery status about delivered Products</p>
                    </div>
                    <div className="status-container">
                        <p>test status</p>
                    </div>
                </>
            )
        }
            return props.active ?(
                <>
                    <div className="fulldeliverinfo-container">
                        <Delivery/>
                        <DeliveryMainInfo/>
                        <DeliveryStatus/>
                    </div>
                </>
            ) : ""
        }
        function DeliveredProducts(props){
            function Productsgraph(props){
                return(
                    <>
                        <div className="infoP-container">
                            <p style={{backgroundColor:"rgba(172, 203, 185, 0.966)", width:"280px"}}>all information about delivered products in graph</p>
                        </div>
                        <div className="productsgraph-container">

                        </div>
                    </>
                )
            }
            function ProductsTable(props){
                return(
                    <>
                        <div className="infoP-container">
                            <p style={{backgroundColor:"rgba(172, 203, 185, 0.966)",width:"280px"}}>all information about delivered products in table</p>
                        </div>
                        <div className="productstable-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>ProductName</th>
                                    <th>ProductAccepted</th>
                                    <th>ProductDelivered</th>
                                    <th>DeliveresVical'sPlate</th>
                                    <th>AcceptedFrom</th>
                                    <th>DeliveredTo</th>
                                    <th>TimeOfDelivery</th>

                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>22</td>
                                    <td>22</td>
                                    <td>22</td>
                                    <td>22</td>
                                    <td>22</td>
                                </tr>
                            </tbody>
                        </table>
                        </div>
                    </>
                )
            }
            return props.active ?(
                <>
                    <div className="deliveredproducts-container">
                        <Productsgraph/>
                        <ProductsTable/>
                    </div>
                </>
            ):""
        }
    return (
        <>
            <div className="deliverysidebar-container">
                <SidebarMainComponente
                    active = {props.activemain}
                />
                <AddDeliverComponente
                    active = {props.activeadd}
                />
                <FullDeliverInfoComponente
                    active = {props.activedeliverinfo}
                />
                <DeliveredProducts
                    active = {props.activedeliveredpro}
                />
            </div>
        </>
    )
}
function Delivery(props){
    const [main, setmain] = useState(true)
    const [add, setadd] = useState(false)
    const [deliverinfo, setdeliverinfo] = useState(false)
    const [deliveredpro, setdeliveredpro] = useState(false)

    function activemain(){
        setadd(false)
        setdeliverinfo(false)
        setdeliveredpro(false)
        return setmain(true)
    }
    function activeadd(){
        setmain(false)
        setdeliverinfo(false)
        setdeliveredpro(false)
        return setadd(true)
    }
    function activedeliverinfo(){
        setmain(false)
        setadd(false)
        setdeliveredpro(false)
        return setdeliverinfo(true)
    }
    function activedeliveredpro(){
        setmain(false)
        setadd(false)
        setdeliverinfo(false)
        return setdeliveredpro(true)
    }
    return props.active ?(
        <>
            <div className="delivery-container">
                <DeliveryMainbar
                    funcmain = {activemain}
                    funcadd = {activeadd}
                    funcdeliverinfo = {activedeliverinfo}
                    funcdeliveredpro = {activedeliveredpro}
                />
                <DeliverySidebar
                    activemain = {main}
                    activeadd = {add}
                    activedeliverinfo = {deliverinfo}
                    activedeliveredpro = {deliveredpro}
                />
            </div>
        </>
    ):""
}

export default Delivery;