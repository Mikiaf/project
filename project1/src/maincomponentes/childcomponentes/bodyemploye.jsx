import React from "react";
import { useState } from "react";
import "./childcomponent-style/bodyemploye.css"
import Modal from "./grandchildcomponetes/modal1";


function Employemainbar(props){
    return(
        <>
            <div className="employemainbar-container">
                <button onClick={props.funcmanageemploye}>manage Employe</button><br></br>
                <button onClick={props.funcfullemploye}>FullEmploye Info</button>
            </div>
        </>
    )
}

function Employesidebar(props){
    function Managemploye(props){
        function Employes(){
            return(
            <>
                <div className="generalinfoP-container">
                    <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                            width: "300px"
                    }}>All information about Employes and there sale status</p>
                </div>
                <div className="sbranches-container">
                    <div className="searche-container">
                        <input type="text" placeholder="searche"/>
                    </div>
                    <div className="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>EmployeFname</th>
                                    <th>EmployeLname</th>
                                    <th>StartingDate</th>
                                    <th>Salary</th>
                                    <th>workingPosition</th>
                                    <th>workingPositionId</th>
                                    <th>TotalWorkingHours</th>
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
        function EmployesMainInfo(){
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
                    <p>information about Employes</p>
                </div>
                <div className="maininfo-container">
                    <p>test maininfo</p>
                                <div className="manageemploye-buttoncontainer">
                                    <button className="manageemploye-button" onClick={()=> setactive(true)}>Manage employe</button>
                                </div>
                            <Modal active={active} func={nextbtn} close = {()=> setactive(false)}>
                            <div className="updatebranch-container">
                                        <div className="updatebranchinput-container">
                                            <p>update branch information or delete employe</p>
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
                </>
            )
       }
        return props.active ?(
            <>
                <div className="manageemploye-container">
                        <Employes/>
                        <EmployesMainInfo/>
                </div>
            </>
        ) : ""
    }
    function Fullemployeinfo(props){
        return props.active ?(
            <>
                <div className="generalinfoP-container">
                    <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                            width: "310px"
                    }}>Full information about Employes and there personal Info</p>
                </div>
                <div className="fullemployeinfo-container">
                    <div className="table-container">
                            <table>
                                <thead>
                                    <tr>
                                        <th>Id</th>
                                        <th>EmployeFirstName</th>
                                        <th>EmployeLastName</th>
                                        <th>StartingDate</th>
                                        <th>T.workingHours</th>
                                        <th>Salary</th>
                                        <th>T.SalaryPaid</th>
                                        <th>workingPosition</th>
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
        ) : ""
    }
    return(
        <>
            <div className="employesidebar-container">
                <Managemploye
                    active = {props.activemanageemploye}
                />
                <Fullemployeinfo
                    active = {props.activefullemployeinfo}
                />
            </div>
        </>
    )
}

function Employe(props){
    const [manageemploye, setmanageemploye] = useState(true)
    const [fullemployeinfo, setfullemployeinfo] = useState(false)

    function activemanageemploye(){
        setfullemployeinfo(false)
        return setmanageemploye(true)
    }
    function activefullemployeinfo(){
        setmanageemploye(false)
        return setfullemployeinfo(true)
    }
    return props.active ?(
        <>
            <div className="employe-container">
                <Employemainbar
                    funcmanageemploye = {activemanageemploye}
                    funcfullemploye = {activefullemployeinfo}
                />
                <Employesidebar
                    activemanageemploye = {manageemploye}
                    activefullemployeinfo = {fullemployeinfo}
                />
            </div>
        </>
    ) : ""
}
export default Employe;