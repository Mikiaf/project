import React, { useState,useMemo } from "react";
import InsertData from "./insertdatapopup";
import Deletedata from "./deletedatapopup";
import Updatedata from "./updatedatapopup";
import "./grandchildcomponetes-style/dashbordadminpopup.css";

function DashbordAdmin(props) {
  const admintoken = props.token
  const admindata= props.admindata
  const [adminname, setadminname] = useState('');
  const [controlers_id, setcontrolers_id] = useState(null);
  const [admintype, setadmintype] = useState('');
  const [activeinsertdata, setactiveinsertdata] = useState(false);
  const [activeupdatedata, setactiveupdatedata] = useState(false);
  const [activedeletedata, setactivedeletedata] = useState(false);
  const [id,setid]=useState()
  const [selectedcolumn, setselectedcolumn] = useState('')


  const handleSubmit = async (e) => {
    e.preventDefault();
    setactiveinsertdata(true);
  };

  const handleclose = async (e) => {
    setactiveinsertdata(!activeinsertdata);
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
        case 'AdminName':
        case 'AdminType':
            inputType = 'text';
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
    setid(data.adminid)
    console.log("Row clicked:", data);
    //alert(`You clicked on ${data.name} from ${item.city}`);
  };
  const filteredData = useMemo(() =>admindata.filter(
    (item) =>
      (item.admintype && item.admintype.toLowerCase().includes(searchTerm.toLowerCase())) ||
      (item.adminid && item.adminid.toString().includes(searchTerm)) ||
      (item.controlerid && item.controlerid.toString().includes(searchTerm)) ||
      (item.adminname && item.adminname.toLowerCase().includes(searchTerm.toLowerCase()))
  ),
  [admindata,searchTerm]
  )
  console.log(filteredData)
  console.log(admindata)
  console.log(searchTerm)
  return (
    <div className={`dashbordadmin-popup ${props.active ? 'show' : ''}`}>
      <div className="dashbordadmin-content">
        <button className="close-btn" onClick={props.handleclose}>X</button>
        <div className="forminfo-container">
        <p>insert admin information</p>
          <form className="forminput-container" onSubmit={handleSubmit}>
            <input
              type="text"
              placeholder="Enter admin name"
              value={adminname}
              onChange={(e) => setadminname(e.target.value)}
            /><br/>
            <input
              type="text"
              placeholder="Enter admin type"
              value={admintype}
              onChange={(e) => setadmintype(e.target.value)}
            /><br/>
            <input
              type="number"
              placeholder="Enter controler id"
              value={controlers_id}
              onChange={(e) => setcontrolers_id(e.target.value)}
            /><br/>
            <button type="submit" className="submitacc-btn"onClick={handleSubmit}>Submit</button>
          </form>
        </div>
        <div className="table-container">
        <p>admin information</p>
        <input type="text" className="searche-input"placeholder="Searche" value={searchTerm} onChange={(e)=> setSearchTerm(e.target.value)}/>
        <div className="admintable-container">
        <table>
          <thead>
            <tr>
                <th>AdminId</th>
                <th>AdminName</th>
                <th>AdminType</th>
                <th>ControlerId </th>
                <th>AdminCreatedDate</th>
            </tr>
          </thead>
          <tbody>
            {filteredData.map((data,index)=>(
            <tr key={index} onClick={()=>handleRowClick(data)}>
                <td>{data.adminid}</td>
                <td>{data.adminname}</td>
                <td>{data.admintype}</td>
                <td>{data.controlerid}</td>
                <td>{data.createddate}</td>
            </tr>
            ))}
          </tbody>
      </table>
        </div>
        <button className="updateadmin-btn" onClick={()=>setactiveupdatedata(true)}>Update Admin</button>
        <button className="deleteadmin-btn" onClick={()=>setactivedeletedata(true)}>Delete Admin</button>
        </div>
        <Deletedata
          refresh={props.refresh}
          token={admintoken}
          id={id}
          db="admin"
          active={activedeletedata}
          handleclose={handleclosedeletedata}
        ></Deletedata>
        <Updatedata
          refresh={props.refresh}
          token={admintoken}
          id={id}
          db="admin"
          active={activeupdatedata}
          handlclose={handlecloseupdatedata}
        >
            <div>
                <label>
                 <p>Choose an option:</p>
                    <select className="column-container" value={selectedcolumn} onChange={handleChange}>
                        <option value="">Select...</option>
                        <option value="AdminName">adminname</option>
                        <option value="AdminType">admintype</option>
                        <option value="ControlerId">controlerid</option>
                      </select>
                </label>
            </div>
        </Updatedata>
        {activeinsertdata && (
          <InsertData
          refresh={props.refresh}
          token={admintoken}
            activeinsertdata={activeinsertdata}
            db='admin'
            data={{
              adminname,
              admintype,
              controlers_id
            }}
            handleclose={handleclose}
          />
        )}
      </div>
    </div>
  );
}

export default DashbordAdmin;
