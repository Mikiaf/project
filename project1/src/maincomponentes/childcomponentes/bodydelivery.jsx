import React from "react";
import { useState,useEffect ,useMemo} from "react";
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';
import './childcomponent-style/bodydelivery.css'
import Updatedata from "./grandchildcomponetes/updatedatapopup";
import Deletedata from "./grandchildcomponetes/deletedatapopup";
import InsertData from "./grandchildcomponetes/insertdatapopup";

function DeliveryMainbar(props){
    return(
        <>
            <div className="deliverymainbar-container">
                <button onClick={props.funcdeliverinfo}>FullDelivery Info</button>
                <button onClick={props.funcmain}>Main</button><br></br>
                <button onClick={props.funcadd}>Add delivery</button><br></br>
                <button onClick={props.funcdeliveredpro}>Deliverd Products</button>
            </div>
        </>
    )
}
function DeliverySidebar(props){
    const [id,setid] = useState()
    const [item,setitem] = useState({})
    const deliverydata = props.deliverydata
    const deliverydaydata = props.deliverydaydata
    const deliverymonthdata = props.deliverymonthdata
    const deliveryyeardata = props.deliveryyeardata
    const productdata = props.productdata
    const deliveryproductdata = props.deliveryproductdata

    const deliverytoken = props.token
        function SidebarMainComponente(props){
            const [searchTerm, setSearchTerm] = useState("");
            const combinedMonthYearData = deliverydata.map(deliveryData => {
                const yearData = deliveryyeardata.find(y => y.deliveryid === deliveryData.deliveryid);
                const monthData = deliverymonthdata.find(w => w.deliveryid === deliveryData.deliveryid);
                return { ...deliveryData, ...yearData, ...monthData };
            });
            const combinedDayData = deliverydata.map(deliveryData => {
                const dayData = deliverydaydata.find(y => y.deliveryid === deliveryData.deliveryid);
                return { ...deliveryData, ...dayData};
            });
            const filteredMonthYearData = useMemo(() => combinedMonthYearData.filter(
                (item) => 
                  (item.deliveryid && item.deliveryid.toString().includes(searchTerm.toLowerCase()))
              ), [combinedMonthYearData, searchTerm]);
            const filteredDayData = useMemo(() => combinedDayData.filter(
                (item) => 
                  (item.deliveryid && item.deliveryid.toString().includes(searchTerm.toLowerCase()))
              ), [combinedDayData, searchTerm]);
            function GenearalInfoTable(){
                return(
                    <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgba(158, 167, 132, 0.966)", width:'220px'}}>Mothly and yearly status about delivery</p>
                    </div>
                    <div className="generalinfotable-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Date</th>
                                    <th>DriverId</th>
                                    <th>VicalPlateNo</th>
                                    <th>WorkingBakeryId</th>
                                    <th>BakeryName</th>
                                    <th>M.AcceptedProductsInmonye</th>
                                    <th>M.DeliveredProductsInmonye</th>
                                    <th>M.BranchesDelivered</th>
                                    <th>MonthAcceptedGoal</th>
                                    <th>MonthDeliveredGoal</th>
                                    <th>Y.AcceptedProductsInmonye</th>
                                    <th>Y.DeliveredProductsInmonye</th>
                                    <th>Y.BranchesDelivered</th>
                                    <th>YearAcceptedGoal</th>
                                    <th>YearDeliveredGoal</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredMonthYearData.map((data,index) =>(
                                <tr key={index}>
                                    <td>{data.driverid}</td>
                                    <td>{data.driverid}</td>
                                    <td>{data.vicalplateno}</td>
                                    <td>{data.workingbakeryid}</td>
                                    <td>{data.totalmonthacceptedproductsInmonye}</td>
                                    <td>{data.totalmonthdeliveredproductsInmonye}</td>
                                    <td>{data.totalmonthbranchesdelivered}</td>
                                    <td>{data.monthacceptedgoal}</td>
                                    <td>{data.monthdeliveredgoal}</td>
                                    <td>{data.totalyearacceptedproductsInmonye}</td>
                                    <td>{data.totalyeardeliveredproductsInmonye}</td>
                                    <td>{data.totalyearbranchesdelivered}</td>
                                    <td>{data.yearacceptedgoal}</td>
                                    <td>{data.yeardeliveredgoal}</td>
                                </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                    </>
                )
            }
            function TodayinfoTable(){
                return(
                    <>
                        <div className="infoP-container">
                            <p style={{backgroundColor:"rgba(172, 203, 185, 0.966)"}}>Today status about delivery</p>
                        </div>
                        <div className="todayinfotable-container">
                        <table>
                                            <thead>
                                                <tr>
                                                    <th>Date</th>
                                                    <th>DriverId</th>
                                                    <th>VicalPlateNo</th>
                                                    <th>Vical'sPlate</th>
                                                    <th>WorkingBakeryId</th>
                                                    <th>DayAcceptedProductsInmonye</th>
                                                    <th>DayDeliveredProductsInmonye</th>
                                                    <th>TotalBranchesDelivered</th>
                                                    <th>DayAcceptedGoal</th>
                                                    <th>DayDeliverdGoal</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {filteredDayData.map((data,index) =>(
                                                <tr key={index}>
                                                    <td>{data.date}</td>
                                                    <td>{data.driverid}</td>
                                                    <td>{data.vicalplateNo}</td>
                                                    <td>{data.workingbakeryid}</td>
                                                    <td>{data.dayacceptedproductsinmonye}</td>
                                                    <td>{data.daydeliveredproductsinmonye}</td>
                                                    <td>{data.totalbranchesdelivered}</td>
                                                    <td>{data.dayacceptedgoal}</td>
                                                    <td>{data.daydeliverdgoal}</td>
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
                    <div className="maindeliverinfo-container">
                        <div className="searche-container">
                            <input type="text" placeholder="searche" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
                        </div>
                        <GenearalInfoTable/>
                        <TodayinfoTable/>
                    </div>
                </>
            ):""
        }
        function AddDeliverComponente(props){
            function FormInfo(){
                const [driver_id, setdriver_id] = useState();
                const [vehicleplateno, setvehicleplateno] = useState('');
                const [vehicletype, setvehicletype] = useState('');
                const [workingbakery_id, setworkingbakery_id] = useState();
                const [totalworkers, settotalworkers] = useState(null);
                const [totalyearacceptedproductsgoal, settotalyearacceptedproductsgoal] = useState(null);
                const [totalmonthacceptedproductsgoal, settotalmonthacceptedproductsgoal] = useState(null);
                const [totaldayacceptedproductsgoal, settotaldayacceptedproductsgoal] = useState(null);
                const [totaldaydeliverdproductsgoal, settotaldaydeliverdproductsgoal] = useState(null);
                const [totalmonthdeliverdproductsgoal, settotalmonthdeliverdproductsgoal] = useState(null);
                const [totalyeardeliverdproductsgoal, settotalyeardeliverdproductsgoal] = useState(null);
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
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgba(155, 179, 224, 0.555)", width:"250px"}}>submit information about the new delivery</p>
                    </div>
                    <div className="forminfo-container">
                            <div className="imageinfo-container">
                                <label>Enter vehicle's  image</label><br/>
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
                        <div className="forminput-container">
                            <input 
                                type="number" 
                                placeholder="Enter driver Id"
                                value={driver_id}
                                onChange={(e) => setdriver_id(e.target.value)}
                                /><br/>
                            <input 
                                type="text" 
                                placeholder="Enter vehicle plate number"
                                value={vehicleplateno}
                                onChange={(e) => setvehicleplateno(e.target.value)}
                                /><br/>
                            <input 
                                type="text" 
                                placeholder="Enter vehicle type"
                                value={vehicletype}
                                onChange={(e) => setvehicletype(e.target.value)}
                                /><br/>
                            <input 
                                type="number" 
                                placeholder="Enter working bakery id"
                                value={workingbakery_id}
                                onChange={(e) => setworkingbakery_id(e.target.value)}
                                /><br/>
                            <input 
                                type="number" 
                                placeholder="Enter total workers"
                                value={totalworkers}
                                onChange={(e) => settotalworkers(e.target.value)}
                                /><br/>
                            <input 
                                type="number" 
                                placeholder="Enter total day to accepted products goal"
                                value={totaldayacceptedproductsgoal}
                                onChange={(e) => settotaldayacceptedproductsgoal(e.target.value)}
                                /><br/>
                            <input 
                                type="number" 
                                placeholder="Enter total month to accepted products goal"
                                value={totalmonthacceptedproductsgoal}
                                onChange={(e) => settotalmonthacceptedproductsgoal(e.target.value)}
                                /><br/>
                            <input 
                                type="number" 
                                placeholder="Enter total year to accepted products goal"
                                value={totalyearacceptedproductsgoal}
                                onChange={(e) => settotalyearacceptedproductsgoal(e.target.value)}
                                /><br/>
                            <input 
                                type="number" 
                                placeholder="Enter total day to deliverd products goal"
                                value={totaldaydeliverdproductsgoal}
                                onChange={(e) => settotaldaydeliverdproductsgoal(e.target.value)}
                                /><br/>
                            <input 
                                type="number" 
                                placeholder="Enter total month to deliverd products goal"
                                value={totalmonthdeliverdproductsgoal}
                                onChange={(e) => settotalmonthdeliverdproductsgoal(e.target.value)}
                                /><br/>
                            <input 
                                type="number" 
                                placeholder="Enter total year to deliverd products goal"
                                value={totalyeardeliverdproductsgoal}
                                onChange={(e) => settotalyeardeliverdproductsgoal(e.target.value)}
                                /><br/>
                            <button onClick={handleSubmit}>submit</button>
                        </div>
                    </div>
                    {activeinsertdata && (
                            <InsertData
                              refresh={props.refresh}
                              token={deliverytoken}
                              activeinsertdata={activeinsertdata}
                              db='delivery'
                              data={{
                                driver_id,
                                vehicleplateno,
                                vehicletype,
                                workingbakery_id,
                                totalworkers,
                                totaldayacceptedproductsgoal,
                                totalmonthacceptedproductsgoal,
                                totalyearacceptedproductsgoal,
                                totalmonthdeliverdproductsgoal,
                                totaldaydeliverdproductsgoal,
                                totalyeardeliverdproductsgoal,
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
                <div className="adddeliver-container">
                        <FormInfo/>
                </div>
                </>
            ) : ""
        }
        function FullDeliverInfoComponente(props){
            function Delivery(){
                const [searchTerm, setSearchTerm] = useState("");
                const handleRowClick = (item) => {
                    // Perform any action with the clicked row deliverydata
                    setid(item.deliveryid)
                    setitem(item)
                    console.log("Row clicked:", item);
                    //alert(`You clicked on ${item.name} from ${item.city}`);
                  };
                  const filteredData = useMemo(() =>deliverydata.filter(
                    (item) =>
                      (item.vicalplateno && item.vicalplateno.toLowerCase().includes(searchTerm.toLowerCase())) ||
                      (item.deliveryid && item.deliveryid.toString().includes(searchTerm)) ||
                      (item.driverid && item.driverid.toString().includes(searchTerm)) ||
                      (item.workingbakeryid && item.workingbakeryid.toString().includes(searchTerm)) ||
                      (item.vicaltype && item.vicaltype.toLowerCase().includes(searchTerm.toLowerCase()))
                  ),
                  [deliverydata,searchTerm]
                  )
                return(
                <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgb(205, 170, 207)", width:"300px"}}>All information about delivery and there delivery status</p>
                    </div>
                    <div className="sbranches-container">
                        <div className="searche-container">
                            <input type="text" placeholder="searche" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
                        </div>
                        <div className="table-container">
                            <table>
                                <thead>
                                    <tr>
                                        <th>DeliveryId</th>
                                        <th>DriverId</th>
                                        <th>VicalPlateNo</th>
                                        <th>VicalType</th>
                                        <th>WorkingBakeryId</th>
                                        <th>TotalWorkingHours</th>
                                        <th>TotalAcceptedProducts</th>
                                        <th>TotalDeliveredProducts</th>
                                        <th>TotalBranchesDelivered</th>
                                        <th>DeliveryStartingDate</th>
                                        <th>TotalWorkers</th>
                                        <th>TotalDayAcceptedProductsGoal</th>
                                        <th>TotalMonthAcceptedProductsGoal</th>
                                        <th>TotalYearAcceptedProductsGoal</th>
                                        <th>TotalDayDeliveredProductsGoal</th>
                                        <th>TotalMonthDeliveredProductsGoal</th>
                                        <th>TotalYearDeliveredProductsGoal</th>
                                    </tr>
                                </thead>
                                <tbody>
                                        {filteredData.map((item,index) =>(
                                         <tr key={index} onClick={()=>handleRowClick(item)}>
                                                <td>{item.deliveryid}</td>
                                                <td>{item.driverid}</td>
                                                <td>{item.vicalplateno}</td>
                                                <td>{item.vicaltype}</td>
                                                <td>{item.workingbakeryid}</td>
                                                <td>{item.totalworkinghours}</td>
                                                <td>{item.totalacceptedproducts}</td>
                                                <td>{item.totaldeliveredproducts}</td>
                                                <td>{item.totalbranchesdelivered}</td>
                                                <td>{item.deliverystartingdate}</td>
                                                <td>{item.totalworkers}</td>
                                                <td>{item.totaldayacceptedproductsgoal}</td>
                                                <td>{item.totalmonthacceptedproductsgoal}</td>
                                                <td>{item.totalyearacceptedproductsgoal}</td>
                                                <td>{item.totaldaydeliveredproductsgoal}</td>
                                                <td>{item.totalmonthdeliveredproductsgoal}</td>
                                                <td>{item.totalyeardeliveredproductsgoal}</td>
                                         </tr> 
                                        ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </>
                )
            }
            function DeliveryMainInfo(){
                const [selectedcolumn, setselectedcolumn] = useState('')
                const [activeupdatedata, setactiveupdatedata] = useState(false)
                const [activedeletedata, setactivedeletedata] = useState(false)
                const [type,settype] = useState('')
                const [accept,setaccept] = useState('')

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
                        case 'VicalPlateNo':
                        case 'VicalType':
                            inputType = 'text';
                            break;
                        case 'DeliveryImage':
                            inputType = 'file';
                            inputaccept = 'image/*'
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
                return(
                    <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgba(178, 206, 216, 0.966)", width:"200px"}}>information about delivery</p>
                    </div>
                    <div className="maininfo-container">
                                <div className="deliveryinfo-conatiner">
                                    <div className="deliverycharinfo-conatiner">
                                            <input disabled={true} placeholder={`Delivery id=${item.deliveryid}`}/><br/>
                                            <input disabled={true} placeholder={`Driver Id=${item.driverid}`}/><br/>
                                            <input disabled={true} placeholder={`Palte number=${item.vicalplateno}`}/><br/>
                                            <input disabled={true} placeholder={`Vechal Type=${item.vicaltype}`}/><br/>
                                            <input disabled={true} placeholder={`Working Bakery Id=${item.workingbakeryid}`}/>
                                        </div>
                                        <div className="deliveryimage-container">
                                            <p>
                                                <strong>Delivery Image:</strong>
                                                {item.vicalimage ? (
                                                <img src={`http://127.0.0.1:5000//static/image/employees/delivery${item.vicalplateno.replace(/\s+/g, '')}.png`} alt="Employee" />
                                                ) : (
                                                <span> No Image Available</span>
                                                )}
                                            </p>
                                        </div>
                                </div>
                                <div className="managedelivery-buttoncontainer">
                                    <button className="updatedelivery-btn"onClick={()=> setactiveupdatedata(true)}>Update Delivery</button>
                                    <button className="deletedelivery-btn"onClick={()=> setactivedeletedata(true)}>Delete Delivery</button>
                                </div>
                                <Deletedata
                                    refresh={props.refresh}
                                    token={deliverytoken}
                                    id={id}
                                    db='delivery'
                                    active={activedeletedata}
                                    handleclose={handleclosedeletedata}
                                ></Deletedata>
                                <Updatedata 
                                    refresh={props.refresh}
                                    token={deliverytoken}
                                    id={id}
                                    db="delivery"
                                    active={activeupdatedata} 
                                    selectedcolumn={selectedcolumn} 
                                    type={type}
                                    accept={accept}
                                    handlclose = {handlecloseupdatedata}>
                                <div>
                                        <label>
                                            <p>Choose an option:</p>
                                            <select className="column-container" value={selectedcolumn} onChange={handleChange}>
                                                <option value="">Select...</option>
                                                <option value="DriverId">DriverId</option>
                                                <option value="VicalPlateNo">vicalplateNo</option>
                                                <option value="VicalType">vicaltype</option>
                                                <option value="WorkingBakeryId">workingbakeryid</option>
                                                <option value="TotalWorkers">totalworkers</option>
                                                <option value="TotalDayAcceptedProductsGoal">totaldayacceptedproductsgoal</option>
                                                <option value="TotalMonthAcceptedProductsGoal">totalmonthacceptedproductsgoal</option>
                                                <option value="TotalYearAcceptedProductsGoal">totalyearacceptedproductsgoal</option>
                                                <option value="TotalDayDeliverdProductsGoal">totaldaydeliverdproductsgoal</option>
                                                <option value="TotalMonthDeliverdProductsGoal">totalmonthdeliverdproductsgoal</option>
                                                <option value="TotalYearDeliverdProductsGoal">totalyeardeliverdproductsgoal</option>
                                                <option value="DeliveryImage">deliveryimage</option>
                                            </select>
                                        </label>
                                    </div>
                                </Updatedata>
                    </div>
                    </>
                )
           }
           function DeliveryStatus(){

            const [daydata,setdaydata] = useState(false)
            const [monthdata,setmonthdata] = useState(true)
            const [yeardata,setyeardata] = useState(false)
            const [labels,setlabels] = useState()
            const [acceptedgraphdata,setacceptedgraphdata] = useState()
            const [deliveredgraphdata,setdeliveredgraphdata] = useState()
            const [acceptedtitle,setacceptedtitle] = useState("Month accepted data")
            const [deliveredtitle,setdeliveredtitle] = useState("Month delivery data")

            useEffect(() => {
                  
                if (daydata){
                    setacceptedtitle("Day accepted data")
                    setdeliveredtitle("Day delivery data")
                    if (id){
                        const newLabels = [];
                        const newacceptedGraphData = [];
                        const newdeliveredGraphData = [];
                        for(let i=0; i< deliverydaydata.length;i++) {
                            if (item.deliveryid == deliverydaydata[i]['deliveryid']){
                                newLabels.push(deliverydaydata[i]["date"]);
                                newacceptedGraphData.push(deliverydaydata[i]["dayacceptedproductsinmonye"]);
                                newdeliveredGraphData.push(deliverydaydata[i]["daydeliveredproductsinmonye"]);
                            }
                        }
                        setlabels(newLabels)
                        setacceptedgraphdata(newacceptedGraphData)
                        setdeliveredgraphdata(newdeliveredGraphData)
                    }
                 }
                 if (monthdata){
                    setacceptedtitle("Month accepted data")
                    setdeliveredtitle("Month delivery data")
                     if (id){
                        const newLabels = [];
                        const newacceptedGraphData = [];
                        const newdeliveredGraphData = [];
                        for(let i=0; i< deliverymonthdata.length;i++) {
                            if (item.deliveryid == deliverymonthdata[i]['deliveryid']){
                                newLabels.push(deliverymonthdata[i]["date"]);
                                newacceptedGraphData.push(deliverymonthdata[i]["totalmonthacceptedproductsInmonye"]);
                                newdeliveredGraphData.push(deliverymonthdata[i]["totalmonthdeliveredproductsInmonye"]);
                            }
                        }
                        setlabels(newLabels)
                        setacceptedgraphdata(newacceptedGraphData)
                        setdeliveredgraphdata(newdeliveredGraphData)
                    }
                 }
                 if (yeardata){
                    setacceptedtitle("Year accepted data")
                    setdeliveredtitle("Year delivery data")
                     if (id){
                        const newLabels = [];
                        const newacceptedGraphData = [];
                        const newdeliveredGraphData = [];
                        for(let i=0; i< deliveryyeardata.length;i++) {
                            if (item.branchid == deliveryyeardata[i]['branchid']){
                                newLabels.push(deliveryyeardata[i]["date"])
                                newacceptedGraphData.push(deliveryyeardata[i]["totalyearacceptedproductsInmonye"])
                                newdeliveredGraphData.push(deliveryyeardata[i]["totalyeardeliveredproductsInmonye"])
                            }
                        }
                        setlabels(newLabels)
                        setacceptedgraphdata(newacceptedGraphData)
                        setdeliveredgraphdata(newdeliveredGraphData)
                    }
                  }
              }, [daydata, monthdata, yeardata,id,deliverydaydata, deliverymonthdata, deliveryyeardata, item]);

            const chartStyles = {
                container: {
                  padding: '10px',
                  transition: 'all 0.3s ease',
                },
                containerHover: {
                    width: "380px",
                    height: "550px",
                },
                title: {
                  fontSize: '1.5em',
                  textAlign: 'center',
                  color: '#333',
                  marginBottom: '10px',
                },
              };
            const accepteddata = {
                labels:labels,
                datasets: [
                  {
                    label: 'Sales',
                    data: acceptedgraphdata,
                    backgroundColor: 'rgba(75,192,192,0.6)',
                  },
                ],
              };
              const deliveredddata = {
                labels:labels,
                datasets: [
                  {
                    label: 'Sales',
                    data: deliveredgraphdata,
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
                    <div style={chartStyles.title}>{acceptedtitle}</div>
                    <Bar data={accepteddata} options={options} />
                    <div style={chartStyles.title}>{deliveredtitle}</div>
                    <Bar data={deliveredddata} options={options} />
                    </div>
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
            const [searchTerm, setSearchTerm] = useState("");
            const combinedProductData = deliverydata.map(deliveryData => {
                const productData = productdata.find(y => y.deliveryid === deliveryData.deliveryid);
                const bakeryproductData = deliveryproductdata.find(x => x.deliveryid === deliveryData.deliveryid);
                return { ...deliveryData, ...productData, ...bakeryproductData};
            });
            const filteredProductData = useMemo(() => combinedProductData.filter(
                (item) => 
                  (item.deliveryid && item.deliveryid.toString().includes(searchTerm.toLowerCase()))
              ), [combinedProductData, searchTerm]);
            function Productsgraph(){
                const [labels,setlabels] = useState([])
                const [acceptedgraphdata,setacceptedgraphdata] = useState()
                const [deliveredgraphdata,setdeliveredgraphdata] = useState()
                const [acceptedtitle,setacceptedtitle] = useState("accepted data")
                const [deliveredtitle,setdeliveredtitle] = useState("delivery data")
                
                useEffect(() => {
                    if (id) {
                      const newLabels = [];
                      const newacceptedGraphData = [];
                      const newdeliveredGraphData = [];
                      for (let i = 0; i < productdata.length; i++) {
                        if (item.branchid === productdata[i]['branchid']) {
                          newLabels.push(productdata[i]["date"]);
                          newacceptedGraphData.push(productdata[i]["totalproductaccepted"]);
                          newdeliveredGraphData.push(productdata[i]["totalproductdeliverd"]);
                        }
                      }
                      setlabels(newLabels);
                      setacceptedgraphdata(newacceptedGraphData);
                      setdeliveredgraphdata(newdeliveredGraphData);
                    }
                  }, [id, productdata, item]);
                
                const chartStyles = {
                    container: {
                      padding: '10px',
                      transition: 'all 0.3s ease',
                    },
                    containerHover: {
                        width: "380px",
                        height: "550px",
                    },
                    title: {
                      fontSize: '1.5em',
                      textAlign: 'center',
                      color: '#333',
                      marginBottom: '10px',
                    },
                  };
                const delivereddata = {
                    labels: labels,
                    datasets: [
                      {
                        label: 'Sales',
                        data: deliveredgraphdata,
                        backgroundColor: 'rgba(75,192,192,0.6)',
                      },
                    ],
                  };
                  const accepteddata = {
                    labels: labels,
                    datasets: [
                      {
                        label: 'Sales',
                        data: acceptedgraphdata,
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
                        <div style={chartStyles.title}>{acceptedtitle}</div>
                        <Bar data={accepteddata} options={options} />
                        <div style={chartStyles.title}>{deliveredtitle}</div>
                        <Bar data={delivereddata} options={options} />
                        </div>
                        </div>
                    </>
                )
            }
            function ProductsTable(){
                return(
                    <>
                        <div className="infoP-container">
                            <p style={{backgroundColor:"rgba(172, 203, 185, 0.966)",width:"280px"}}>all information about delivered products in table</p>
                        </div>
                        <div className="productstable-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>Time</th>
                                    <th>DeliveryId</th>
                                    <th>ProductId</th>
                                    <th>ProductName</th>
                                    <th>AcceptedProductQuantity</th>
                                    <th>DeliveredProductQuantity</th>
                                    <th>VicalPlateNo</th>
                                    <th>BakeryId</th>
                                    <th>AcceptedTime</th>
                                    <th>DeliverdId</th>
                                    <th>DeliverdTime</th>

                                </tr>
                            </thead>
                            <tbody>
                                {filteredProductData.map((data,index) => (
                                <tr key={index}>
                                    <td>{data.time}</td>
                                    <td>{data.deliveryid}</td>
                                    <td>{data.productid}</td>
                                    <td>{data.productname}</td>
                                    <td>{data.totalproductaccepted}</td>
                                    <td>{data.totalproductdeliverd}</td>
                                    <td>{data.viclapaleteno}</td>
                                    <td>{data.acceptedfrom}</td>
                                    <td>{data.timeofacceptance}</td>
                                    <td>{data.deliverdto}</td>
                                    <td>{data.timeofdelivery}</td>
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
                    <div className="deliveredproducts-container">
                        <div className="searche-container">
                            <input type="text" placeholder="searche" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
                        </div>
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
                    refresh={props.refresh}
                />
                <AddDeliverComponente
                    active = {props.activeadd}
                    refresh={props.refresh}
                />
                <FullDeliverInfoComponente
                    active = {props.activedeliverinfo}
                    refresh={props.refresh}
                />
                <DeliveredProducts
                    active = {props.activedeliveredpro}
                    refresh={props.refresh}
                />
            </div>
        </>
    )
}
function Delivery(props){
    const [main, setmain] = useState(false)
    const [add, setadd] = useState(false)
    const [deliverinfo, setdeliverinfo] = useState(true)
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
                    deliverydata = {props.deliverydata}
                    deliveryproductdata={props.deliveryproductdata}
                    deliverydaydata={props.deliverydaydata}
                    deliverymonthdata={props.deliverymonthdata}
                    deliveryyeardata={props.deliveryyeardata}
                    productdata={props.productdata}

                    refresh={props.refresh}
                    token={props.token}
                />
            </div>
        </>
    ):""
}

export default Delivery;