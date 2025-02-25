import React, { useState,useMemo } from "react";
import InsertData from "./insertdatapopup";
import Updatedata from "./updatedatapopup";
import Deletedata from "./deletedatapopup";
import "./grandchildcomponetes-style/dashbordaccountpopup.css";

function DashbordAccount(props) {
  const accounttoken = props.token
  const accountdata = props.accountdata
  const [dename, setdename] = useState('');
  const [de_id, setde_id] = useState(null);
  const [employee_id, setemployee_id] = useState(null);
  const [password, setpassword] = useState(null);
  const [phonenumber, setphonenumber] = useState('');
  const [activeinsertdata, setactiveinsertdata] = useState(false);
  const [activeupdatedata, setactiveupdatedata] = useState(false);
  const [activedeletedata, setactivedeletedata] = useState(false);
  const [id,setid]=useState()
  const [selectedcolumn, setselectedcolumn] = useState('')
  const [type,settype] = useState('')
  const [accept,setaccept] = useState('')

  const generateRandomNumber = async (e) => {
    const min = 100000;
    const max = 999999;
    const pass = Math.floor(Math.random() * (max - min + 1)) + min;
    setpassword(pass);
  }


  const handleclose = async (e) => {
    setactiveinsertdata(!activeinsertdata);
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    setactiveinsertdata(true);
  };
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
    let inputaccept;
    switch (value) {
        case 'DeName':
        case 'PhoneNumber':
        case 'Status':
            inputType = 'text';
            break;
        case 'PasswordHash':
            inputType = 'password';
            break;
        default:
            inputType = 'number';
            break;
    }

    if (inputType !== type) {
        settype(inputType);
    }
    if (inputaccept !== accept) {
        setaccept(inputaccept);
    }
};
const [searchTerm, setSearchTerm] = useState("");
const handleRowClick = (data) => {
    // Perform any action with the clicked row deliverydata
    setid(data.accountid)
    console.log("Row clicked:", data);
    //alert(`You clicked on ${item.name} from ${item.city}`);
  };
  const filteredData = useMemo(() =>accountdata.filter(
    (item) =>
      (item.dename && item.dename.toLowerCase().includes(searchTerm.toLowerCase())) ||
      (item.accountid && item.accountid.toString().includes(searchTerm)) ||
      (item.deid && item.deid.toString().includes(searchTerm)) ||
      (item.employeeid && item.employeeid.toString().includes(searchTerm)) ||
      (item.status && item.status.toLowerCase().includes(searchTerm.toLowerCase()))||
      (item.phonenumber && item.phonenumber.toLowerCase().includes(searchTerm.toLowerCase()))
  ),
  [accountdata,searchTerm]
  )
  return (
    <div className={`dashbordaccount-popup ${props.active ? 'show' : ''}`}>
      <div className="dashbordaccount-content">
          <button className="close-btn" onClick={props.handleclose}>X</button>
        <div className="forminfo-container">
          <p>Insert account information</p>
          <form className="forminput-container" onSubmit={handleSubmit}>
            <select value={dename} onChange={(e) => setdename(e.target.value)}>
              <option value="">Select department name</option>
              <option value="branch">branch</option>
              <option value="delivery">bakery</option>
              <option value="bakery">delivery</option>
              <option value="admin">admin</option>
              <option value="totaladmin">totaladmin</option>
            </select><br/>
            <input
              type="number"
              placeholder="Enter department id"
              value={de_id}
              onChange={(e) => setde_id(e.target.value)}
            /><br/>
            <input
              type="text"
              placeholder={password}
              disabled={true}
            /><br/>
            <button type="button"className="generate-btn" onClick={generateRandomNumber}>Generate</button>
            <input
              type="text"
              placeholder="Enter phone number"
              value={phonenumber}
              onChange={(e) => setphonenumber(e.target.value)}
            /><br/>
            <button type="submit" className = "submitacc-btn"onClick={handleSubmit}>Submit</button><br/>
          </form><br/>
        </div><br/>
        <div className="table-container">
        <p>account information</p>
        <input type="text" className="searche-input"placeholder="Searche" value={searchTerm} onChange={(e)=>setSearchTerm(e.target.value)}/>
        <div className="accounttable-container">
        <table>
                            <thead>
                                <tr>
                                    <th>AccountId</th>
                                    <th>DeName</th>
                                    <th>DeId</th>
                                    <th>EmployeeId</th>
                                    <th>AccountCreatedDate</th>
                                    <th>AccountUpdateDate</th>
                                    <th>Status</th>
                                    <th>PhoneNumber</th>
                                    <th>Role</th>
                                </tr>
                            </thead>
                            <tbody>
                              {filteredData.map((data,index) =>(
                                <tr key={index} onClick={()=>handleRowClick(data)}>
                                    <td>{data.accountid}</td>
                                    <td>{data.dename}</td>
                                    <td>{data.deid}</td>
                                    <td>{data.employeeid}</td>
                                    <td>{data.createddate}</td>
                                    <td>{data.updateddate}</td>
                                    <td>{data.status}</td>
                                    <td>{data.phonenumber}</td>
                                    <td>{data.role}</td>
                                </tr>
                              ))}
                            </tbody>
                        </table>
        </div>
        <button className="updateaccount-btn" onClick={()=>setactiveupdatedata(true)}>Update Account</button>
        <button className="deleteaccount-btn" onClick={()=>setactivedeletedata(true)}>Delete Account</button>
        </div>
        <Deletedata
          refresh={props.refresh}
          token={accounttoken}
          id={id}
          db="account"
          active={activedeletedata}
          handleclose={handleclosedeletedata}
        ></Deletedata>
        <Updatedata
          refresh={props.refresh}
          token={accounttoken}
          id={id}
          type={type}
          accept={accept}
          db="account"
          active={activeupdatedata}
          handlclose={handlecloseupdatedata}
          selectedcolumn={selectedcolumn}
        >
            <div>
                <label>
                 <p>Choose an option:</p>
                    <select className="column-container" value={selectedcolumn} onChange={handleChange}>
                        <option value="">Select...</option>
                        <option value="PasswordHash">password</option>
                        <option value="Status">status</option>
                        <option value="PhoneNumber">phonenumber</option>
                      </select>
                </label>
            </div>
        </Updatedata>
        {activeinsertdata && (
          <InsertData
            refresh={props.refresh}
            token={accounttoken}
            activeinsertdata={activeinsertdata}
            db='account'
            data={{
              dename,
              de_id,
              password,
              phonenumber
            }}
            handleclose={handleclose}
          />
        )}
      </div>
    </div>
  );
}

export default DashbordAccount;
