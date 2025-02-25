import React from "react";
import { useState,useEffect,useMemo } from "react";
import "./childcomponent-style/bodyemploye.css"
import InsertData from "./grandchildcomponetes/insertdatapopup";
import Updatedata from "./grandchildcomponetes/updatedatapopup";
import Deletedata from "./grandchildcomponetes/deletedatapopup";


function Employemainbar(props){
    return(
        <>
            <div className="employemainbar-container">
                <button onClick={props.funcmanageemploye}>manage Employe</button><br></br>
                <button onClick={props.funcaddemployee}>AddEmployee</button>
            </div>
        </>
    )
}

function Employesidebar(props){
    console.log(props.token)
    const [id,setid] = useState()
    const [item,setitem] = useState({})
    const employeedata = props.employeedata
    const employeetoken = props.token
    function Managemploye(props){
        function Employes(){
            const [searchTerm, setSearchTerm] = useState("");
            const handleRowClick = (item) => {
                // Perform any action with the clicked row employeedata
                setid(item.employeeid)
                setitem(item)
                //alert(`You clicked on ${item.name} from ${item.city}`);
              };
              const filteredData = useMemo(() => employeedata.filter(
                (item) => 
                  (item.employeelname && item.employeelname.toLowerCase().includes(searchTerm.toLowerCase())) ||
                  (item.employeemname && item.employeemname.toLowerCase().includes(searchTerm.toLowerCase())) ||
                  (item.employeefname && item.employeefname.toLowerCase().includes(searchTerm.toLowerCase())) ||
                  (item.employeeid && item.employeeid.toString().includes(searchTerm)) ||
                  (item.workingposition && item.workingposition.toLowerCase().includes(searchTerm.toLowerCase()))
              ), [employeedata, searchTerm]);
            return(
            <>
                <div className="generalinfoP-container">
                    <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                            width: "300px"
                    }}>All information about Employes and there sale status</p>
                </div>
                <div className="sbranches-container">
                    <div className="searche-container">
                        <input type="text" placeholder="searche" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
                    </div>
                    <div className="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>EmployeeId</th>
                                    <th>EmployeeFname</th>
                                    <th>EmployeeMname</th>
                                    <th>EmployeeLname</th>
                                    <th>EmployeeStartingDate</th>
                                    <th>Salary</th>
                                    <th>workingPosition</th>
                                    <th>workingPositionName</th>
                                    <th>Role</th>
                                    <th>UnderId</th>
                                    <th>TotalWorkingHours</th>
                                    <th>TotalPaidSalaryForEmployee</th>
                                    <th>DayWorkingHourGoal</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredData.map((item,index)=>(
                                    <tr key={index} onClick={()=>handleRowClick(item)}>
                                                <td>{item.employeeid}</td>
                                                <td>{item.employeefname}</td>
                                                <td>{item.employeemname}</td>
                                                <td>{item.employeelname}</td>
                                                <td>{item.startingdate}</td>
                                                <td>####</td>
                                                <td>{item.workingposition}</td>
                                                <td>{item.workingpositionname}</td>
                                                <td>{item.role}</td>
                                                <td>{item.underid}</td>
                                                <td>{item.totalworkinghours}</td>
                                                <td>{item.totalpaidsalaryforemployee}</td>
                                                <td>{item.dayworkinghourgoal}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </>
            )
        }
        function EmployesMainInfo(){
            const [selectedcolumn, setselectedcolumn] = useState('')
            const [activeupdatedata, setactiveupdatedata] = useState(false)
            const [activedeletedata, setactivedeletedata] = useState(false)
            const [type,settype] = useState('')
            const [accept, setaccept] = useState('')


            const handlecloseupdatedata = async (e) => {
                setactiveupdatedata(!activeupdatedata);                           
            };

            const handleclosedeletedata = async (e) => {
                setactivedeletedata(!activedeletedata);                           
            };
            const handleChange = (event) => {
                const value = event.target.value;
                setselectedcolumn(value);
                let inputType;
                let inputaccept
                switch (value) {
                    case 'DayWorkingHourGoal':
                        inputType = 'number';
                        break;
                    case 'EmployeeImage':
                        inputType = 'file';
                        break;
                    case 'WorkingPosition':
                        inputType = 'select';
                        break;
                    default:
                        inputType = 'text';
                        break;
                }
        
                if (inputType !== type) {
                    settype(inputType);
                }
                if (inputaccept !== accept) {
                    setaccept(inputaccept);
                }
            };
            console.log(item.employeeimage)
            return(
                <>
                <div className="generalinfoP-container">
                    <p>information about Employes</p>
                </div>
                <div className="maininfo-container">
                    <div className="einfo-container">
                        <div className="employecharinfo-conatiner">
                            <input disabled={true} placeholder={`Employe id=${item.employeeid}`}/><br/>
                            <input disabled={true} placeholder={`First name=${item.employeefname}`}/><br/>
                            <input disabled={true} placeholder={`Last name=${item.employeelname}`}/><br/>
                            <input disabled={true} placeholder={`Working postion=${item.workingposition}`}/><br/>
                            <input disabled={true} placeholder={`Working postion name=${item.workingpositionname}`}/>
                        </div>
                        <div className="employeeimage-container">
                            <p>
                                <strong>Employee Image:</strong>
                                {item.employeeimage ? (
                                <img src={`http://127.0.0.1:5000//static/image/employees/employee${item.employeefname.replace(/\s+/g, '')}${item.employeemname.replace(/\s+/g, '')}${item.employeelname.replace(/\s+/g, '')}.png`} alt="Employee" />
                                ) : (
                                <span> No Image Available</span>
                                )}
                            </p>
                        </div>
                    </div>
                                <div className="manageemployee-buttoncontainer">
                                    <button className="updateemployee-btn" onClick={()=> setactiveupdatedata(true)}>Update employee</button>
                                    <button className="deleteemployee-btn" onClick={()=> setactivedeletedata(true)}>Delete employee</button>
                                </div>
                            <Deletedata
                                refresh={props.refresh}
                                token={employeetoken}
                                id={id}
                                db='employee'
                                active={activedeletedata}
                                handleclose={handleclosedeletedata}
                            ></Deletedata>
                            <Updatedata
                                refresh={props.refresh}
                                token = {employeetoken}
                                id={id}
                                selectedcolumn={selectedcolumn}
                                db='employee'
                                active={activeupdatedata}  
                                handlclose= {handlecloseupdatedata}
                                type={type}
                                accept={accept}
                                >                        
                            <div>
                                        <label>
                                            <p>Choose an option:</p>
                                            <select className="column-container" value={selectedcolumn} onChange={handleChange}>
                                                <option value="">Select...</option>
                                                <option value="EmployeeFname">employeefname</option>
                                                <option value="EmployeeMname">employeemname</option>
                                                <option value="EmployeeLname">employeelname</option>
                                                <option value="WorkingPosition">workingposition</option>
                                                <option value="WorkingPositionName">workingpositionname</option>
                                                <option value="DayWorkingHourGoal">dayworkinghourgoal</option>
                                                <option value="EmployeeImage">employeeimage</option>
                                            </select>
                                        </label>
                                    </div>
                            </Updatedata>
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

    function Addemployeecomponentes(props){
        function Forminfo(){
            const [employeefname, setemployeefname] = useState('');
            const [employeemname, setemployeemname] = useState('');
            const [employeelname, setemployeelname] = useState('');
            const [workingposition, setworkingposition] = useState(null);
            const [workingpositionname, setworkingpositionname] = useState('');
            const [role,setrole] = useState(null);
            const [underid,setunderid] = useState(null);
            const [dayworkinghourgoal, setdayworkinghourgoal] = useState(null);
            const [activeinsertdata, setactiveinsertdata] = useState(false);
            const [selectedImage, setSelectedImage] = useState(null);
            const [isDisabled, setIsDisabled] = useState(true);
            const formData = new FormData();


            const handlerole = (event) =>{
                const value = event.target.value
                setrole(value)
                if ( value === 'under'){
                    setIsDisabled(false)
                }
                else{
                    setIsDisabled(true)
                }
            }

            const handleclose = async (e) => {
                setactiveinsertdata(!activeinsertdata);                           
              }
            
              const handleSubmit = async (e) => {
                e.preventDefault();
                setactiveinsertdata(true);
              };
            
              const handleImageChange = (event) => {
                const file = event.target.files[0];
                if (file) {
                  setSelectedImage(file);
                  // Preview the image (optional)
                  const reader = new FileReader();
                  reader.onloadend = () => {
                    const preview = document.getElementById('image-preview');
                    preview.src = reader.result;
                  };
                  reader.readAsDataURL(file);
                }
              };
            return(
                <>
                    <div className="generalinfoP-container">
                        <p>submit information about employee</p>
                    </div>
                    <div className="forminfo-container">
                    <div className="imageinfo-container">
                                <label>Enter employee's image</label><br/>
                                <input 
                                        type="file"
                                        className="image-input" 
                                        accept="image/*"
                                        onChange={handleImageChange} 
                                    /><br/>
                                    <div className="image-container"> 
                                    {selectedImage && (
                                        <div>
                                        <h2>Image Preview:</h2>
                                        <img id="image-preview" alt="Image Preview" />
                                        <p>Selected File: {selectedImage.name}</p>
                                        </div>
                                    )}
                                    </div>
                            </div>
                        <form className="forminput-container">
                                <input 
                                    type="text" 
                                    placeholder="Enter employee first name"
                                    value={employeefname}
                                    onChange={(e) => setemployeefname(e.target.value)}
                                    /><br/>
                                <input 
                                    type="text" 
                                    placeholder="Enter employee middle name"
                                    value={employeemname}
                                    onChange={(e) => setemployeemname(e.target.value)}
                                    /><br/>
                                <input 
                                    type="text" 
                                    placeholder="Enter employee last name"
                                    value={employeelname}
                                    onChange={(e) => setemployeelname(e.target.value)}
                                    /><br/>
                                        <label>
                                            <select value={workingposition} onChange={(e)=>setworkingposition(e.target.value)}>
                                                <option value="">Select working position</option>
                                                <option value="branch">branch</option>
                                                <option value="delivery">delivery</option>
                                                <option value="bakery">bakery</option>
                                                <option value="admin">admin</option>
                                            </select>
                                        </label><br/>
                                    <input 
                                        type="text" 
                                        placeholder="Enter employee working position name or vehicle plate"
                                        value={workingpositionname}
                                        onChange={(e) => setworkingpositionname(e.target.value)}
                                    /><br/>
                                        <label>
                                            <select value={role} onChange={handlerole}>
                                                <option value="">Select employee working role</option>
                                                <option value="controller">controller</option>
                                                <option value="manager">manager</option>
                                                <option value="driver">driver</option>
                                                <option value="under">under</option>
                                            </select>
                                        </label><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter woking employee  id"
                                    value={underid}
                                    onChange={(e) => setunderid(e.target.value)}
                                    disabled={isDisabled}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter employee day working hour goal"
                                    value={dayworkinghourgoal}
                                    onChange={(e) => setdayworkinghourgoal(e.target.value)}
                                    /><br/>
                                <button onClick={handleSubmit}>submit</button>
                        </form>
                    </div>
                    {activeinsertdata && (
                            <InsertData
                              refresh={props.refresh}
                              token={employeetoken}
                              activeinsertdata={activeinsertdata}
                              db='employee'
                              data={{
                                employeefname,
                                employeemname,
                                employeelname,
                                workingposition,
                                workingpositionname,
                                role,
                                underid,
                                dayworkinghourgoal,
                              }}
                              selectedImage={selectedImage}
                              handleclose={handleclose}
                            />
                          )}
                </>
            )
        }
        return props.active ?(
            <>
                <div className="addemployee-container">
                    <Forminfo/>
                </div>
            </>
        ) : ""
    }




    return(
        <>
            <div className="employesidebar-container">
                <Managemploye
                    active = {props.activemanageemploye}
                    refresh={props.refresh}
                />
                <Addemployeecomponentes
                    active = {props.activeaddemployee}
                    refresh={props.refresh}
                />
            </div>
        </>
    )
}

function Employe(props){
    const [manageemploye, setmanageemploye] = useState(true)
    const [addemployee, setaddemployee] = useState(false)

    function activemanageemploye(){
        setaddemployee(false)
        return setmanageemploye(true)
    }

    function activeaddemployee(){
        setmanageemploye(false)
        return setaddemployee(true)
    }
    return props.active ?(
        <>
            <div className="employe-container">
                <Employemainbar
                    funcmanageemploye = {activemanageemploye}
                    funcaddemployee = {activeaddemployee}
                />
                <Employesidebar
                    activemanageemploye = {manageemploye}
                    activeaddemployee={addemployee}
                    employeedata={props.employeedata}
                    salarydata={props.salarydata}

                    refresh={props.refresh}
                    token={props.token}
                />
            </div>
        </>
    ) : ""
}
export default Employe;