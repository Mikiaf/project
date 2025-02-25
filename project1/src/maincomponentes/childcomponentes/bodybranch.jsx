import React, { useState, useEffect,useMemo } from "react";
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';
import "./childcomponent-style/bodybranch.css";
import Updatedata from "./grandchildcomponetes/updatedatapopup";
import InsertData from "./grandchildcomponetes/insertdatapopup";
import Deletedata from "./grandchildcomponetes/deletedatapopup";
///branch componentes


///mainbar access sidebar
function BranchMainbar(props){
    return(
        <>
            <div className="branchmainbar-container">
                <button onClick={props.funcbranchinfo}>FullBranch Info</button>
                <button onClick={props.funcmain}>Main</button><br></br>
                <button onClick={props.funcadd}>Add branch</button><br></br>
                <button onClick={props.funcacceptedpro}>Accepted Products</button>
            </div>
        </>
    )
}

///sidebar info telling component
function BranchSidebar(props){
    const [id,setid] = useState()
    const [item,setitem] = useState({})
    const branchdata = props.branchdata
    const branchdaydata = props.branchdaydata
    const branchmonthdata = props.branchmonthdata
    const branchyeardata = props.branchyeardata
    const productdata = props.productdata
    const branchproductdata = props.branchproductdata
    const branchtoken = props.token
                function Branchinfocomponentes(props){
                    function Branches(){
                        const [searchTerm, setSearchTerm] = useState("");
                        const handleRowClick = (item) => {
                            // Perform any action with the clicked row branchdata
                            setid(item.branchid)
                            setitem(item)
                            console.log("Row clicked:", item);
                            //alert(`You clicked on ${item.name} from ${item.city}`);
                          };
                          const filteredData = useMemo(() => branchdata.filter(
                            (item) =>
                              (item.branchname && item.branchname.toLowerCase().includes(searchTerm.toLowerCase())) ||
                              (item.branchid && item.branchid.toString().includes(searchTerm)) ||
                              (item.controllerid && item.controllerid.toString().includes(searchTerm)) ||
                              (item.location && item.location.toLowerCase().includes(searchTerm.toLowerCase()))
                          ),
                          [branchdata,searchTerm]
                          )
                          console.log(filteredData)
                          console.log(branchdata)
                        return(
                        <>
                            <div className="generalinfoP-container">
                                <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                            width: "300px"
                            }}>All information about branches and there sale status</p>
                            </div>
                            <div className="sbranches-container">
                                <div className="searche-container">
                                    <input type="text" placeholder="searche" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
                                </div>
                                <div className="table-container">
                                    <table>
                                        <thead>
                                            <tr>
                                                <th>BranchId</th>
                                                <th>BranchName</th>
                                                <th>BranchType</th>
                                                <th>Location</th>
                                                <th>ControlersId</th>
                                                <th>TotalWorkers</th>
                                                <th>BranchStartingDate</th>
                                                <th>TotalAcceptedProducts</th>
                                                <th>BranchTotalSaleInMoney</th>
                                                <th>BranchYearSaleGoalInMoney</th>
                                                <th>BranchMonthSaleGoalInMoney</th>
                                                <th>BranchDaySaleGoalInMoney</th>
                                                <th>BranchDayWorikingHoureGoal</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {filteredData.map((item,index) =>(
                                               <tr key={index} onClick={()=>handleRowClick(item)}>
                                                    <td>{item.branchid}</td>
                                                    <td>{item.branchname}</td>
                                                    <td>{item.branchtype}</td>
                                                    <td>{item.location}</td>
                                                    <td>{item.controllerid}</td>
                                                    <td>{item.totalworkers}</td>
                                                    <td>{item.branchstartingdate}</td>
                                                    <td>{item.totalacceptedproducts}</td>
                                                    <td>{item.branchtotalsaleinmoney}</td>
                                                    <td>{item.branchyearsalegoalinmoney}</td>
                                                    <td>{item.branchmonthsalegoalinmoney}</td>
                                                    <td>{item.branchdaysalegoalinmoney}</td>
                                                    <td>{item.branchdayworikinghouregoal}</td>
                                           </tr> 
                                            ))}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </>
                        )
                        
                    }
                    function BranchMainInfo(){
                        const [selectedcolumn, setselectedcolumn] = useState('')
                        const [activeupdatedata, setactiveupdatedata] = useState(false)
                        const [activedeletdata, setactivedeletedata] = useState(false)
                        const [type,settype] = useState('')
                        const [accept,setaccept] = useState('')

                        const handlecloseupdatedata = async (e) => {
                            setactiveupdatedata(!activeupdatedata);                           
                        };

                        const handleclosedeletedata = async (e) => {
                            setactivedeletedata(!activedeletdata);                           
                        };

                        const handleChange = (event) => {
                            const value = event.target.value;
                            setselectedcolumn(value);
                            let inputType;
                            let inputaccept;
                            switch (value) {
                                case 'ControlersId':
                                case 'TotalWorkers':
                                case 'BranchYearSaleGoal':
                                case 'BranchMonthSaleGoal':
                                case 'BranchDaySaleGoal':
                                case 'BranchDayWorkingHourGoal':
                                    inputType = 'number';
                                    break;
                                case 'BranchImage':
                                    inputType = 'file';
                                    inputaccept = 'image/*'
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
                        
                        return(
                            <>
                            <div className="generalinfoP-container">
                                <p>information about branches</p>
                            </div>
                            <div className="maininfo-container">
                            <div className="branchinfo-conatiner">
                                    <div className="branchcharinfo-conatiner">
                                            <input disabled={true} placeholder={`Branch Id=${item.branchid}`}/><br/>
                                            <input disabled={true} placeholder={`Branch Name=${item.branchname}`}/><br/>
                                            <input disabled={true} placeholder={`Location=${item.location}`}/><br/>
                                            <input disabled={true} placeholder={`Branch Type=${item.branchtype}`}/><br/>
                                            <input disabled={true} placeholder={`Controler Id=${item.ControllerId}`}/>
                                        </div>
                                        <div className="branchimage-container">
                                            <p>
                                                <strong>Delivery Image:</strong>
                                                {item.branchimage ? (
                                                <img src={`http://127.0.0.1:5000//static/image/employees/branch${item.branchname.replace(/\s+/g, '')}.png`} alt="Employee" />
                                                ) : (
                                                <span> No Image Available</span>
                                                )}
                                            </p>
                                        </div>
                                </div>
                                <div className="managebranch-buttoncontainer">
                                    <button className="updatebranch-btn" onClick={() =>setactiveupdatedata(true)}>Update Branch</button>
                                    <button className="deletebranch-btn" onClick={() =>setactivedeletedata(true)}>Delete Branch</button>
                                </div>
                                    <Deletedata
                                        refresh={props.refresh}
                                        token={branchtoken}
                                        id={id}
                                        db='branch'
                                        active={activedeletdata}
                                        handleclose={handleclosedeletedata}
                                    ></Deletedata>
                                    <Updatedata
                                        refresh={props.refresh}
                                        token={branchtoken}
                                        id={id}
                                        db='branch'
                                        type={type}
                                        accept={accept}
                                        active={activeupdatedata}
                                        handlclose={handlecloseupdatedata}
                                        selectedcolumn={selectedcolumn}
                                    >
                                    <div>
                                        <label>
                                            <p>Choose an option:</p>
                                            <select className="column-container" value={selectedcolumn} onChange={handleChange}>
                                                <option value="">Select...</option>
                                                <option value="BranchName">branchname</option>
                                                <option value="BranchType">branchtype</option>
                                                <option value="Location">location</option>
                                                <option value="ControlersId">controlers_id</option>
                                                <option value="TotalWorkers">totalworkers</option>
                                                <option value="BranchYearSaleGoal">branchyearsalegoal</option>
                                                <option value="BranchMonthSaleGoal">branchmonthsalegoal</option>
                                                <option value="BranchDaySaleGoal">branchdaysalegoal</option>
                                                <option value="BranchDayWorkingHourGoal">branchdayworkinghourgoal</option>
                                                <option value="BranchImage">branchimage</option>
                                            </select>
                                        </label>
                                    </div>
                                    </Updatedata>
                            </div>
                            </>
                        )
                   }
                    function BranchStatus(){
                        
                        const [daydata,setdaydata] = useState(false)
                        const [monthdata,setmonthdata] = useState(true)
                        const [yeardata,setyeardata] = useState(false)
                        const [labels,setlabels] = useState()
                        const [graphdata,setgraphdata] = useState()
                        const [title,settitle] = useState("Month sales data")

                        useEffect(() => { 
                            if (daydata){
                                settitle("Day sales data")
                                if(id){
                                    const newLabels = [];
                                    const newGraphData = [];
                                    for(let i=0; i<branchdaydata.length;i++) {
                                        if (item.branchid == branchdaydata[i]['branchid']){
                                            newLabels.push(branchdaydata[i]["date"]);
                                            newGraphData.push(branchdaydata[i]["totaldaysoldproductsinmoney"]);
                                        }
                                    }
                                    setlabels(newLabels)
                                    setgraphdata(newGraphData)
                                }
                             }
                             if (monthdata){
                                 settitle("Month sales data")
                                 if(id){
                                    const newLabels = [];
                                    const newGraphData = [];
                                    for(let i=0; i< branchmonthdata.length;i++) {
                                        if (item.branchid == branchmonthdata[i]['branchid']){
                                            newLabels.push(branchmonthdata[i]["date"]);
                                            newGraphData.push(branchmonthdata[i]["totalmonthsoldproductsInmoney"]);
                                        }
                                    }
                                    setlabels(newLabels)
                                    setgraphdata(newGraphData)
                                 }
                             }
                             if (yeardata){
                                 settitle("Year sales data")
                                 if(id){
                                    const newLabels = [];
                                    const newGraphData = [];
                                    for(let i=0; i< branchyeardata.length;i++) {
                                        if (item.branchid == branchyeardata[i]['branchid']){
                                            newLabels.push(branchyeardata[i]["date"])
                                            newGraphData.push(branchyeardata[i]["totalyearsoldproductsInmoney"])
                                        }
                                    }
                                    setlabels(newLabels)
                                    setgraphdata(newGraphData)
                                }
                              }
                          }, [daydata, monthdata, yeardata,id,branchdaydata, branchmonthdata, branchyeardata, item]);

                        const chartStyles = {
                            container: {
                              padding: '10px',
                              transition: 'all 0.3s ease',
                            },
                            containerHover: {
                                width: "680px",
                                height: "550px",
                            },
                            title: {
                              fontSize: '1.5em',
                              textAlign: 'center',
                              color: '#333',
                              marginBottom: '10px',
                            },
                          };
                        const data = {
                            labels: labels,
                            datasets: [
                              {
                                label: 'Sales',
                                data: graphdata,
                                backgroundColor: 'rgba(75,192,192,0.6)',
                              },
                            ],
                          };
                          const options = {
                            scales: {
                              y: {
                                beginAtZero: true,
                                grid: {
                                  color: 'rgba(200, 200, 200, 0.5)', // Grid line color
                                },
                                ticks: {
                                  color: '#4CAF50', // Y-axis label color
                                },
                              },
                              x: {
                                ticks: {
                                  color: '#FF5722', // X-axis label color
                                },
                              },
                            },
                            plugins: {
                              legend: {
                                labels: {
                                  color: '#3F51B5', // Legend label color
                                },
                              },
                            },
                          };
                        return(
                            <>
                            <div className="generalinfoP-container">
                                <p style={{backgroundColor: "rgba(211, 159, 224, 0.966)"}}>status about branches</p>
                            </div>
                                <div className="status-container">
                                    <div className="btn-container">
                                        <button className="day-btn" 
                                        onClick={
                                            ()=>{setdaydata(true);
                                            setmonthdata(false);
                                            setyeardata(false);
                                        }}
                                            >Day</button>
                                        <button className="month-btn" 
                                            onClick={
                                            ()=>{setmonthdata(true);
                                            setdaydata(false);
                                            setyeardata(false);
                                        }
                                            }>Month</button>
                                        <button className="year-btn"
                                            onClick={
                                            ()=>{setmonthdata(false);
                                            setdaydata(false);
                                            setyeardata(true);
                                        }
                                            }
                                        >Year</button>
                                    </div>
                                <div
                                        style={{ ...chartStyles.container, ...chartStyles.containerHover }}
                                        onMouseEnter={() => (chartStyles.containerHover.boxShadow = '0 8px 16px rgba(0, 0, 0, 0.2)')}
                                        onMouseLeave={() => (chartStyles.containerHover.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)')}
                                        >
                                <div style={chartStyles.title}>{title}</div>
                                <Bar data={data} options={options} />
                                </div>
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
                    function Forminfo(){
                      const [branchname, setbranchname] = useState('');
                      const [branchtype, setbranchtype] = useState('');
                      const [location, setlocation] = useState('');
                      const [controlers_id, setcontroler_id] = useState(null);
                      const [totalworkers, settotalworkers] = useState(null);
                      const [branchyearsalegoal, setbranchyearsalegoal] = useState(null);
                      const [branchmonthsalegoal, setbranchmonthsalegoal] = useState(null);
                      const [branchdaysalegoal, setbranchdaysalegoal] = useState(null);
                      const [branchdayworkinghourgoal, setbranchdayworkinghourgoal] = useState(null);
                      const [activeinsertdata, setactiveinsertdata] = useState(false);
                      const [selectedImage, setSelectedImage] = useState(null);
                    
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
                            <p>submit information about branch</p>
                          </div>
                          <div className="forminfo-container">
                            <div className="imageinfo-container">
                                <label>Enter branch's image</label><br/>
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
                            <form className="forminput-container" >
                              <input 
                                type="text" 
                                placeholder="Enter branch name"
                                value={branchname}
                                onChange={(e) => setbranchname(e.target.value)}
                              /><br/>
                              <input 
                                type="text" 
                                placeholder="Enter branch location"
                                value={location}
                                onChange={(e) => setlocation(e.target.value)}
                              /><br/>
                              <input 
                                type="number" 
                                placeholder="Enter branch controler"
                                value={controlers_id}
                                onChange={(e) => setcontroler_id(e.target.value)}
                              /><br/>
                              <input 
                                type="number" 
                                placeholder="Enter total workers"
                                value={totalworkers}
                                onChange={(e) => settotalworkers(e.target.value)}
                              /><br/>
                              <input 
                                type="text" 
                                placeholder="Enter Branch type"
                                value={branchtype}
                                onChange={(e) => setbranchtype(e.target.value)}
                              /><br/>
                              <input 
                                type="number" 
                                placeholder="Enter Branch day sell goal"
                                value={branchdaysalegoal}
                                onChange={(e) => setbranchdaysalegoal(e.target.value)}
                              /><br/>
                              <input 
                                type="number" 
                                placeholder="Enter Branch month sell goal"
                                value={branchmonthsalegoal}
                                onChange={(e) => setbranchmonthsalegoal(e.target.value)}
                              /><br/>
                              <input 
                                type="number" 
                                placeholder="Enter Branch year sell goal"
                                value={branchyearsalegoal}
                                onChange={(e) => setbranchyearsalegoal(e.target.value)}
                              /><br/>
                              <input 
                                type="number" 
                                placeholder="Enter Branch day working hour goal"
                                value={branchdayworkinghourgoal}
                                onChange={(e) => setbranchdayworkinghourgoal(e.target.value)}
                              /><br/>
                              <button type="submit" onClick={handleSubmit}>Submit</button>
                            </form>
                          </div>
                          {activeinsertdata && (
                            <InsertData
                              refresh={props.refresh}
                              token={branchtoken}
                              activeinsertdata={activeinsertdata}
                              db='branch'
                              data={{
                                branchname,
                                branchtype,
                                location,
                                controlers_id,
                                totalworkers,
                                branchyearsalegoal,
                                branchmonthsalegoal,
                                branchdaysalegoal,
                                branchdayworkinghourgoal,
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
                            <div className="addbranch-container">
                                <Forminfo/>
                            </div>
                        </>
                    ):""
                }
                function SidebarMaincomponentes(props){
                    const [searchTerm, setSearchTerm] = useState("");
                    const combinedMonthYearData = branchdata.map(branchData => {
                        const yearData = branchyeardata.find(y => y.branchid === branchData.branchid);
                        const monthData = branchmonthdata.find(w => w.branchid === branchData.branchid);
                        return { ...branchData, ...yearData, ...monthData };
                    });
                    const combinedDayData = branchdata.map(branchData => {
                        const dayData = branchdaydata.find(y => y.branchid === branchData.branchid);
                        return { ...branchData, ...dayData};
                    });
                    const filteredMonthYearData = useMemo(() => combinedMonthYearData.filter(
                        (item) => 
                          (item.branchid && item.branchid.toString().includes(searchTerm.toLowerCase()))
                      ), [combinedMonthYearData, searchTerm]);
                    const filteredDayData = useMemo(() => combinedDayData.filter(
                        (item) => 
                          (item.branchid && item.branchid.toString().includes(searchTerm.toLowerCase()))
                      ), [combinedDayData, searchTerm]);
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
                                                <th>Date</th>
                                                <th>BranchId</th>
                                                <th>BranchName</th>
                                                <th>ControllerId</th>
                                                <th>M.SoldProductsInMoney</th>
                                                <th>M.AcceptedProductsValue</th>
                                                <th>MonthSaleGoal</th>
                                                <th>Y.SoldProductsInMoney</th>
                                                <th>Y.AcceptedProductsValue</th>
                                                <th>YearSaleGoal</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {filteredMonthYearData.map((data,index) =>(
                                            <tr key={index}>
                                                <td>{data.date}</td>
                                                <td>{data.branchid}</td>
                                                <td>{data.branchname}</td>
                                                <td>{data.controllerid}</td>
                                                <td>{data.totalmonthsoldproductsInmoney}</td>
                                                <td>{data.totalmonthacceptedproductsvalue}</td>
                                                <td>{data.monthsalegoal}</td>
                                                <td>{data.totalyearsoldproductsInmoney}</td>
                                                <td>{data.totalyearacceptedproductsvalue}</td>
                                                <td>{data.yearsalegoal}</td>
                                            </tr>
                                            ))}
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
                                                <th>Date</th>
                                                <th>BranchId</th>
                                                <th>BranchName</th>
                                                <th>ControllerId</th>
                                                <th>D.SoldProductsInMoney</th>
                                                <th>D.AcceptedProductsInMoney</th>
                                                <th>DaySaleGoal</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {filteredDayData.map((data,index) =>(
                                            <tr key={index}>
                                                <td>{data.date}</td>
                                                <td>{data.branchid}</td>
                                                <td>{data.branchname}</td>
                                                <td>{data.controllerid}</td>
                                                <td>{data.totaldaysoldproductsinmoney}</td>
                                                <td>{data.totaldayacceptedproductsinmoney}</td>
                                                <td>{data.daysalegoal}</td>
                                            </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                </div>
                            </>
                        )
                    }
                    return props.active ?(
                       <>
                            <div className="mainbranchinfo-container">
                                <div className="searche-container">
                                     <input type="text" placeholder="searche" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
                                </div>
                                <GeneralInfoTable/>
                                <TodayInfoTable/>
                            </div>
                       </>
                    ):""
                }
                function AcceptedProducts(props){
                    const handleRowClick = (item) => {
                        // Perform any action with the clicked row branchdata
                        setid(item.branchid)
                        setitem(item)
                        console.log("Row clicked:", item);
                        //alert(`You clicked on ${item.name} from ${item.city}`);
                      };
                    const [searchTerm, setSearchTerm] = useState("");
                    const combinedProductData = branchdata.map(branchData => {
                        const productData = productdata.find(y => y.branchid === branchData.branchid);
                        const bakeryproductData = branchproductdata.find(x => x.branchid === branchData.branchid);
                        return { ...branchData, ...productData, ...bakeryproductData};
                    });
                    const filteredProductData = useMemo(() => combinedProductData.filter(
                        (item) => 
                          (item.branchid && item.branchid.toString().includes(searchTerm.toLowerCase()))
                      ), [combinedProductData, searchTerm]);
                    function ProductsGraph(){
                        const [labels,setlabels] = useState([])
                        const [graphdata,setgraphdata] = useState([])
                        const [title,settitle] = useState("Product data")
                        
                        useEffect(() => {
                            if (id) {
                              const newLabels = [];
                              const newGraphData = [];
                              for (let i = 0; i < productdata.length; i++) {
                                if (item.branchid === productdata[i]['branchid']) {
                                  newLabels.push(productdata[i]["date"]);
                                  newGraphData.push(productdata[i]["totaldaysoldproductsinmoney"]);
                                }
                              }
                              setlabels(newLabels);
                              setgraphdata(newGraphData);
                            }
                          }, [id, productdata, item]);
                        
                        const chartStyles = {
                            container: {
                              padding: '10px',
                              transition: 'all 0.3s ease',
                            },
                            containerHover: {
                                width: "400px",
                                height: "220px",
                            },
                            title: {
                              fontSize: '1.5em',
                              textAlign: 'center',
                              color: '#333',
                              marginBottom: '10px',
                            },
                          };
                        const data = {
                            labels: labels,
                            datasets: [
                              {
                                label: 'Sales',
                                data: graphdata,
                                backgroundColor: 'rgba(75,192,192,0.6)',
                              },
                            ],
                          };
                          const options = {
                            scales: {
                              y: {
                                beginAtZero: true,
                                grid: {
                                  color: 'rgba(200, 200, 200, 0.5)', // Grid line color
                                },
                                ticks: {
                                  color: '#4CAF50', // Y-axis label color
                                },
                              },
                              x: {
                                ticks: {
                                  color: '#FF5722', // X-axis label color
                                },
                              },
                            },
                            plugins: {
                              legend: {
                                labels: {
                                  color: '#3F51B5', // Legend label color
                                },
                              },
                            },
                          };
                        return(
                            <>
                            <div className="generalinfoP-container">
                                <p style={{backgroundColor: "rgba(211, 159, 224, 0.966)"}}>status about branches</p>
                            </div>
                                <div className="productsgraph-container">
                                <div
                                        style={{ ...chartStyles.container, ...chartStyles.containerHover }}
                                        onMouseEnter={() => (chartStyles.containerHover.boxShadow = '0 8px 16px rgba(0, 0, 0, 0.2)')}
                                        onMouseLeave={() => (chartStyles.containerHover.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)')}
                                        >
                                <div style={chartStyles.title}>{title}</div>
                                <Bar data={data} options={options} />
                                </div>
                                </div>
                            </>
                        )
                    }
                    function ProductsTable(){
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
                                                <th>Time</th>
                                                <th>BranchId</th>
                                                <th>BranchName</th>
                                                <th>ProductId</th>
                                                <th>ProductName</th>
                                                <th>ProductQuantityAccepted</th>
                                                <th>D.ProductSelledInMoney</th>
                                                <th>AcceptedTime</th>
                                                <th>DeliveryId</th>
                                                <th>BranchSaleInMoney</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {filteredProductData.map((data,index) =>(
                                            <tr key={index} onClick={() => handleRowClick(data)}>
                                                <td>{data.time}</td>
                                                <td>{data.branchid}</td>
                                                <td>{data.branchname}</td>
                                                <td>{data.productid}</td>
                                                <td>{data.productname}</td>
                                                <td>{data.productquantityaccepted}</td>
                                                <td>{data.totaldayproductselledIn$}</td>
                                                <td>{data.acceptedtime}</td>
                                                <td>{data.deliveryid}</td>
                                                <td>{data.branchSalein$}</td>
                                            </tr>
                                            ))}
                                        </tbody>
                                    </table>    
                                </div>
                            </>
                        )
                    }
                    return props.active ?(
                        <>
                            <div className="acceptedproducts-container">
                                <div className="searche-container">
                                    <input type="text" placeholder="searche" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
                                </div>
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
                refresh={props.refresh}
            />
            <Addbranchcomponentes
                active = {props.activeadd}
                refresh={props.refresh}
            />
            <Branchinfocomponentes 
                active = {props.activebranchinfo}
                refresh={props.refresh}
            />
            <AcceptedProducts
                active = {props.activeacctedpro}
                refresh={props.refresh}
            />
        </div> 
        </>
    )
}



function Branch(props){
   const [main, setmain] = useState(false)
   const [add, setadd] = useState(false)
   const [branchinfo, setbranchinfo] = useState(true)
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
                    branchdata={props.branchdata}
                    branchproductdata={props.branchproductdata}
                    branchdaydata={props.branchdaydata}
                    branchmonthdata={props.branchmonthdata}
                    branchyeardata={props.branchyeardata}
                    productdata={props.productdata}
                    activemain = {main}
                    activeadd = {add}
                    activebranchinfo = {branchinfo}
                    activeacctedpro = {accetedpro}


                    refresh={props.refresh}
                    token={props.token}
                />
            </div>
        </>
    ):""
}

export default Branch;