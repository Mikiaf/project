import React from "react"
import { useState } from "react"
import './childcomponent-style/bodybakery.css'
import Modal from "./grandchildcomponetes/modal1"

function BakeryMainbar(props){
    return(
        <>
            <div className="bekerymainbar-container">
                <button onClick={props.funcmain}>Main</button><br></br>
                <button onClick={props.funcadd}>Add bekery</button><br></br>
                <button onClick={props.funcbekeryinfo}>FullBakery Info</button>
                <button onClick={props.funcbakedproducts}>Baked Products</button>
            </div>
        </>
    )
}
function BakerySidebar(props){
    function Sidebarmaincomponentes(props){
        function GeneralInfoTable(){
            return(
                <>
                    <div className="generalinfoP-container">
                                <p>Mothly status about bekery</p>
                    </div>
                    <div className="generalinfotable-container">
                    <table>
                            <thead>
                                <tr>
                                    <th>BakeryName</th>
                                    <th>StartedDate</th>
                                    <th>M.Workers</th>
                                    <th>M.SendOutProductes</th>
                                    <th>M.BakedProductes</th>
                                    <th>M.WorkingHour</th>
                                    <th>Y.Workers</th>
                                    <th>Y.SendoutProductes</th>
                                    <th>Y.BakedProductes</th>
                                    <th>Y.WorkingHour</th>
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
                </>
            )
        }
    
        function TodayInfoTable(){
            return(
                <>
                    <div className="todayinfoP-container">
                            <p>Today status about bakery</p>
                    </div>
                     <div className="todayinfotable-container">
                    <table>
                            <thead>
                                <tr>
                                    <th>BakeryName</th>
                                    <th>DayBakedProducts</th>
                                    <th>DaySendouts</th>
                                    <th>DayBakeryGoal</th>
                                    <th>Dayworkinghour</th>
                                    <th>DeliveryId</th>
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
              <div className="mainbekeryinfo-container">
                    <GeneralInfoTable/>
                    <TodayInfoTable/>  
              </div>  
            </>
        ) : ""
    }
    function Addbakerycomponentes(props){
        function Doneinfo(){
            return(
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)"}}>user submited bekery information</p>
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
                        <p>submit information about bekery</p>
                    </div>
                    <div className="forminfo-container">
                        <form className="forminput-container">
                                <input type="text" placeholder="Enter bekery name"/><br/>
                                <input type="text" placeholder="Enter bekery location"/><br/>
                                <input type="text" placeholder="Enter bekery controler"/><br/>
                                <input type="number" placeholder="Enter delivery id"/><br/>
                                <input type="text" placeholder="Enter bekery type"/><br/>
                                <button>submit</button>
                        </form>
                    </div>
                </>
            )
        }
        return props.active ?(
            <>
                <div className="addbekery-container">
                    <Doneinfo/>
                    <Forminfo/>
                </div>
            </>
        ) : ""
    }
    function Fullbakeryinfocomponentes(props){
        function Bekery(){
            return(
            <>
                <div className="generalinfoP-container">
                    <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                    width: "300px"
                    }}>All information about bekery and there send out status</p>
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
                                    <th>BakeryName</th>
                                    <th>ManagersId</th>
                                    <th>Location</th>
                                    <th>Totalworkers</th>
                                    <th>Totalworkinghours</th>
                                    <th>TotalBekedProducts</th>
                                    <th>TotalBekedProductsIn$</th>
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
        function BekeryMainInfo(){
            const [active, setactive] = useState(false)
            const [currentindex, setindex] = useState(0)

            function nextbtn(){
                currentindex === 1 ? setindex(0) : setindex(1);
            }
            const images = [
                {uri:"image.jpg",
                 titel:"i1"
                },
                {uri:"OIP.jpg",
                titel:"i1"
               }
        ]
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
                    <p>information about bekery</p>
                </div>
                <div className="maininfo-container">
                    <p>test maininfo</p>
                                <div className="managebekery-buttoncontainer">
                                    <button className="managebekery-button" onClick={() =>setactive(true)}>Manage Bekery</button>
                                </div>
                                <Modal active={active} func ={nextbtn} close = {()=> setactive(false)}>
                                <div className="updatebekery-container">
                                        <div className="updatebekeryinput-container">
                                            <p>update branch information or delete bakery</p>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/><br/>
                                            <input placeholder="teste"/>
                                        </div>
                                            <div className="updatebekeryImg-container">
                                                <div className="slides" style={slidestyle}></div>
                                            </div>
                                        </div>
                                </Modal>
                </div>
                </>
            )
       }
       function BekeryStatus(){
        return(
            <>
                <div className="generalinfoP-container">
                    <p style={{backgroundColor: "rgba(211, 159, 224, 0.966)"}}>status about bekery</p>
                </div>
                <div className="status-container">
                    <p>test status</p>
                </div>
            </>
        )
    }
        return props.active ?(
            <>
               <div className="fullbekeryinfo-container">
                    <Bekery/>
                    <BekeryMainInfo/>
                    <BekeryStatus/>
                </div> 
            </>
        ) : ""
    }
    function BakedProducts(props){
        function ProductsGraph(props){
            return(
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(206, 178, 216, 0.966)",width:"260px"}}>all information about bakery prodyct sin graph</p>
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
                            <p style={{width:"260px"}}>all information about bakery products in table</p>
                    </div>
                    <div className="productstable-container">
                    <table>
                            <thead>
                                <tr>
                                    <th>BakedProductName</th>
                                    <th>NumberOfProductBaked</th>
                                    <th>TimeOfBakery</th>
                                    <th>BakedProductSendOut</th>
                                    <th>UsedProductsForBakery</th>
                                    <th>BakedProductValue</th>
                                    <th>DeliveryId</th>
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
                </>
            )
        }
        return props.active ?(
            <>
                <div className="bakedproducts-container">
                    <ProductsGraph/>
                    <ProductsTable/>
                </div>
            </>
        ):""
    }
    return (
        <>
            <div className="bekerysidebar-container">
                <Sidebarmaincomponentes
                    active = {props.activemain}
                />
                <Addbakerycomponentes
                    active = {props.ativeadd}
                />
                <Fullbakeryinfocomponentes
                    active = {props.activebekeryinfo}
                />
                <BakedProducts
                    active = {props.activebakedproducts}
                />
            </div>
        </>
    )
}
function Bakery(props){
    const [main, setmain] = useState(true)
    const [add, setadd] = useState(false)
    const [fullbekeryinfo, setfullbekeryinfo] = useState(false)
    const [bakedproducts, setbakedproducts] = useState(false)

    function activemainsidebar(){
        setadd(false)
        setfullbekeryinfo(false)
        setbakedproducts(false)
        return setmain(true)
   }
   function activeaddbekery(){
            setmain(false)
            setfullbekeryinfo(false)
            setbakedproducts(false)
            return setadd(true)

   }
   function activebekeryinfo(){
            setmain(false)
            setadd(false)
            setbakedproducts(false)
            return setfullbekeryinfo(true)
   }
   function activebakedproducts(){
    setadd(false)
    setfullbekeryinfo(false)
    setmain(false)
    return setbakedproducts(true)
    }
    return props.active ?(
        <>
        <div className="bekery-container">
            <BakeryMainbar
                funcmain = {activemainsidebar}
                funcadd =  {activeaddbekery}
                funcbekeryinfo = {activebekeryinfo}
                funcbakedproducts = {activebakedproducts}
            />
            <BakerySidebar
                activemain = {main}
                ativeadd = {add}
                activebekeryinfo = {fullbekeryinfo}
                activebakedproducts = {bakedproducts}
            />
        </div>
        </>
    ): ""
}

export default Bakery;