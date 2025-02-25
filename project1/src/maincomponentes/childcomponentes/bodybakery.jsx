import React from "react"
import { useState,useEffect,useMemo } from "react"
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS } from 'chart.js/auto';
import './childcomponent-style/bodybakery.css'
import Updatedata from "./grandchildcomponetes/updatedatapopup"
import Deletedata from "./grandchildcomponetes/deletedatapopup"
import InsertData from "./grandchildcomponetes/insertdatapopup"

function BakeryMainbar(props){
    return(
        <>
            <div className="bekerymainbar-container">
                <button onClick={props.funcbekeryinfo}>FullBakery Info</button>
                <button onClick={props.funcmain}>Main</button><br></br>
                <button onClick={props.funcadd}>Add bekery</button><br></br>
                <button onClick={props.funcbakedproducts}>Baked Products</button>
            </div>
        </>
    )
}
function BakerySidebar(props){
    const [id,setid] = useState()
    const [item,setitem] = useState({})
    const bakerydata = props.bakerydata
    const bakeryproductdata = props.bakeryproductdata
    const bakerydaydata = props.bakerydaydata
    const bakerymonthdata = props.bakerymonthdata
    const bakeryyeardata = props.bakeryyeardata
    const productdata = props.productdata

    const bakerytoken = props.token
    function Sidebarmaincomponentes(props){
        const [searchTerm, setSearchTerm] = useState("");
        const combinedMonthYearData = bakerydata.map(bakeryData => {
            const yearData = bakeryyeardata.find(y => y.bakeryid === bakeryData.bakeryid);
            const monthData = bakerymonthdata.find(w => w.bakeryid === bakeryData.bakeryid);
            return { ...bakeryData, ...yearData, ...monthData };
        });
        console.log("test bakery")
        console.log(combinedMonthYearData)
        const combinedDayData = bakerydata.map(bakeryData => {
            const dayData = bakerydaydata.find(y => y.bakeryid === bakeryData.bakeryid);
            return { ...bakeryData, ...dayData};
        });
        const filteredMonthYearData = useMemo(() => combinedMonthYearData.filter(
            (item) => 
              (item.bakeryname && item.bakeryname.toLowerCase().includes(searchTerm.toLowerCase()))
          ), [combinedMonthYearData, searchTerm]);
        const filteredDayData = useMemo(() => combinedDayData.filter(
            (item) => 
              (item.bakeryname && item.bakeryname.toLowerCase().includes(searchTerm.toLowerCase()))
          ), [combinedDayData, searchTerm]);
        function GeneralInfoTable(){
            return(
                <>
                    <div className="generalinfoP-container">
                                <p>Mothly and yearly status about bakery</p>
                    </div>
                    <div className="generalinfotable-container">
                    <table>
                            <thead>
                                <tr>
                                    <th>Date</th>
                                    <th>BakeryName</th>
                                    <th>StartedDate</th>
                                    <th>M.SendOutProductes</th>
                                    <th>M.BakedProductes</th>
                                    <th>M.BakedProductValue</th>
                                    <th>M.SendoutProductValue</th>
                                    <th>M.BakeryGoal</th>
                                    <th>M.SendOutGoal</th>
                                    <th>Y.SendoutProductes</th>
                                    <th>Y.BakedProductes</th>
                                    <th>Y.SendoutProductValue</th>
                                    <th>Y.BakedProductValue</th>
                                    <th>Y.BakeryGoal</th>
                                    <th>Y.SendOutGoal</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredMonthYearData.map((data,index) => (
                                    <tr key={index}>
                                        <td>{data.data}</td>
                                        <td>{data.bakeryname}</td>
                                        <td>{data.bakerystartingdate}</td>
                                        <td>{data.monthtotalsendoutproducts}</td>
                                        <td>{data.monthtotalbakedproducts}</td>
                                        <td>{data.monthtotalbakedproductvalue}</td>
                                        <td>{data.monthtotalsendoutproductvalue}</td>
                                        <td>{data.monthbakerygoal}</td>
                                        <td>{data.monthsendoutgoal}</td>
                                        <td>{data.yeartotalsendoutproducts}</td>
                                        <td>{data.yeartotalbakedproducts}</td>
                                        <td>{data.yeartotalsendoutproductvalue}</td>
                                        <td>{data.yeartotalbakedproductvalue}</td>
                                        <td>{data.yearbakerygoal}</td>
                                        <td>{data.yearsendoutgoal}</td>
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
                            <p>Today status about bakery</p>
                    </div>
                     <div className="todayinfotable-container">
                    <table>
                            <thead>
                                <tr>
                                    <th>Date</th>
                                    <th>BakeryName</th>
                                    <th>ManagerId</th>
                                    <th>DayBakedProducts</th>
                                    <th>DaySendouts</th>
                                    <th>DayBakedProductValue</th>
                                    <th>DaySendoutsProductValue</th>
                                    <th>DayBakeryGoal</th>
                                    <th>Dayworkinghour</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredDayData.map((data,index)=>(
                                    <tr key={index}>
                                        <td>{data.data}</td>
                                        <td>{data.bakeryname}</td>
                                        <td>{data.managerid}</td>
                                        <td>{data.totalbakedproducts}</td>
                                        <td>{data.totalsendoutproducts}</td>
                                        <td>{data.totalbakedproductvalue}</td>
                                        <td>{data.totalsendoutproductvalue}</td>
                                        <td>{data.daybakerygoal}</td>
                                        <td>{data.daysendoutgoal}</td>
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
              <div className="mainbekeryinfo-container">
                    <div className="searche-container">
                        <input type="text" placeholder="searche" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
                    </div>
                    <GeneralInfoTable/>
                    <TodayInfoTable/>  
              </div>  
            </>
        ) : ""
    }
    function Addbakerycomponentes(props){
        function Forminfo(){
            
            const [bakeryname, setbakeryname] = useState('');
            const [bakerytype, setbakerytype] = useState('');
            const [manager_id, setmanager_id] = useState();
            const [location, setlocation] = useState('');
            const [totaldaytobakeproductsgoal, settotaldaytobakeproductsgoal] = useState();
            const [totalmonthtobakeproductsgoal, settotalmonthtobakeproductsgoal] = useState();
            const [totalyeartobakeproductsgoal, settotalyeartobakeproductsgoal] = useState();
            const [totaldaytosendoutproductsgoal, settotaldaytosendoutproductsgoal] = useState();
            const [totalmonthtosendoutproductsgoal, settotalmonthsendoutproductsgoal] = useState();
            const [totalyeartosendoutproductsgoal, settotalyeartosendoutproductsgoal] = useState();
            const [totalworker, settotalworker] = useState();
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
                        <p>submit information about bekery</p>
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
                                    placeholder="Enter bakery name"
                                    value={bakeryname}
                                    onChange={(e) => setbakeryname(e.target.value)}
                                    /><br/>
                                <input 
                                    type="text" 
                                    placeholder="Enter bakery type"
                                    value={bakerytype}
                                    onChange={(e) => setbakerytype(e.target.value)}
                                    /><br/>
                                <input 
                                    type="text" 
                                    placeholder="Enter bakery location"
                                    value={location}
                                    onChange={(e) => setlocation(e.target.value)}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter bekery manager id"
                                    value={manager_id}
                                    onChange={(e) => setmanager_id(e.target.value)}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter total workers"
                                    value={totalworker}
                                    onChange={(e) => settotalworker(e.target.value)}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter total day to bake products goal"
                                    value={totaldaytobakeproductsgoal}
                                    onChange={(e) => settotaldaytobakeproductsgoal(e.target.value)}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter total month to bake products goal"
                                    value={totalmonthtobakeproductsgoal}
                                    onChange={(e) => settotalmonthtobakeproductsgoal(e.target.value)}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter total year to bake products goal"
                                    value={totalyeartobakeproductsgoal}
                                    onChange={(e) => settotalyeartobakeproductsgoal(e.target.value)}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter total day to send out products goal"
                                    value={totaldaytosendoutproductsgoal}
                                    onChange={(e) => settotaldaytosendoutproductsgoal(e.target.value)}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter total month to send out products goal"
                                    value={totalmonthtosendoutproductsgoal}
                                    onChange={(e) => settotalmonthsendoutproductsgoal(e.target.value)}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter total year to send out products goal"
                                    value={totalyeartosendoutproductsgoal}
                                    onChange={(e) => settotalyeartosendoutproductsgoal(e.target.value)}
                                    /><br/>
                                <button onClick={handleSubmit}>submit</button>
                        </form>
                    </div>
                    {activeinsertdata && (
                            <InsertData
                              refresh={props.refresh}
                              token={bakerytoken}
                              activeinsertdata={activeinsertdata}
                              db='bakery'
                              data={{
                                bakeryname,
                                bakerytype,
                                manager_id,
                                location,
                                totalworker,
                                totaldaytobakeproductsgoal,
                                totalmonthtobakeproductsgoal,
                                totalyeartobakeproductsgoal,
                                totaldaytosendoutproductsgoal,
                                totalmonthtosendoutproductsgoal,
                                totalyeartosendoutproductsgoal,
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
                <div className="addbekery-container">
                    <Forminfo/>
                </div>
            </>
        ) : ""
    }
    function Fullbakeryinfocomponentes(props){
        function Bekery(){
            const [searchTerm, setSearchTerm] = useState("");
            const handleRowClick = (item) => {
                // Perform any action with the clicked row bakerydata
                setid(item.bakeryid)
                setitem(item)
                console.log("Row clicked:", item);
                //alert(`You clicked on ${item.name} from ${item.city}`);
              };
              const filteredData = useMemo(() =>bakerydata.filter(
                (item) =>
                  (item.bakeryname && item.bakeryname.toLowerCase().includes(searchTerm.toLowerCase())) ||
                  (item.bakerytype && item.bakerytype.toLowerCase().includes(searchTerm.toLowerCase())) ||
                  (item.bakeryid && item.bakeryid.toString().includes(searchTerm)) ||
                  (item.managerid && item.managerid.toString().includes(searchTerm)) ||
                  (item.location && item.location.toLowerCase().includes(searchTerm.toLowerCase()))
              ),
              [bakerydata,searchTerm]
              )
            return(
            <>
                <div className="generalinfoP-container">
                    <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                    width: "300px"
                    }}>All information about bekery and there send out status</p>
                </div>
                <div className="sbranches-container">
                    <div className="searche-container">
                        <input type="text" placeholder="searche" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
                    </div>
                    <div className="table-container">
                        <table>
                            <thead>
                                <tr>
                                    <th>BakeryId</th>
                                    <th>BakeryName</th>
                                    <th>BakeryType</th>
                                    <th>ManagerId</th>
                                    <th>BakeryStartedDate</th>
                                    <th>TotalWorkingHours</th>
                                    <th>Location</th>
                                    <th>TotalWorkers</th>
                                    <th>TotalBakedProducts</th>
                                    <th>TotalSendOutProducts</th>
                                    <th>TotalDayToBakeProductsGoal</th>
                                    <th>TotalMonthToBakeProductsGoal</th>
                                    <th>TotalYearToBakeProductsGoal</th>
                                    <th>TotalDayToSendOutProductsGoal</th>
                                    <th>TotalMonthToSendOutProductsGoal</th>
                                    <th>TotalYearToSendOutProductsGoal</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredData.map((item,index) =>(
                                    <tr key={index} onClick={() => handleRowClick(item)}>
                                                <td>{item.bakeryid}</td>
                                                <td>{item.bakeryname}</td>
                                                <td>{item.bakerytype}</td>
                                                <td>{item.managerid}</td>
                                                <td>{item.bakerystarteddate}</td>
                                                <td>{item.totalworkinghours}</td>
                                                <td>{item.location}</td>
                                                <td>{item.totalworkers}</td>
                                                <td>{item.totalbakedproducts}</td>
                                                <td>{item.totalsendoutproducts}</td>
                                                <td>{item.totaldaytobakeproductsgoal}</td>
                                                <td>{item.totalmonthtobakeproductsgoal}</td>
                                                <td>{item.totalyeartobakeproductsgoal}</td>
                                                <td>{item.totaldaytosendoutproductsgoal}</td>
                                                <td>{item.totalmonthtosendoutproductsgoal}</td>
                                                <td>{item.totalyeartosendoutproductsgoal}</td>
                                      </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </>
            )
        }
        function BekeryMainInfo(){
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
                let inputaccept;
                switch (value) {
                    case 'BakeryName':
                    case 'BakeryType':
                    case 'Location':
                        inputType = 'text';
                        break;
                    case 'BakeryImage':
                        inputType = 'file';
                        inputaccept="image/*";
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
                <div className="generalinfoP-container">
                    <p>information about bekery</p>
                </div>
                <div className="maininfo-container">
                <div className="bakeryinfo-conatiner">
                     <div className="bakerycharinfo-conatiner">
                            <input disabled={true} placeholder={`Bakery id=${item.bakeryid}`}/><br/>
                            <input disabled={true} placeholder={`Bakery name=${item.bakeryname}`}/><br/>
                            <input disabled={true} placeholder={`Bakery type=${item.bakerytype}`}/><br/>
                            <input disabled={true} placeholder={`Manager Id=${item.managerid}`}/><br/>
                            <input disabled={true} placeholder={`Location=${item.location}`}/>
                        </div>
                        <div className="bakeryimage-container">
                            <p>
                                <strong>Bakery Image:</strong>
                                {item.bakeryimage ? (
                                <img src={`http://127.0.0.1:5000//static/image/employees/bakery${item.bakeryname.replace(/\s+/g, '')}.png`} alt="Employee" />
                                ) : (
                                <span> No Image Available</span>
                                )}
                            </p>
                        </div>
                </div>
                                <div className="managebakery-buttoncontainer">
                                    <button className="updatebakery-btn" onClick={() =>setactiveupdatedata(true)}>Update Bakery</button>
                                    <button className="deletebakery-btn" onClick={() =>setactivedeletedata(true)}>Delete Bakery</button>
                                </div>
                                <Deletedata
                                  refresh={props.refresh}
                                  token={bakerytoken}
                                    id={id}
                                    db='bakery'
                                    active={activedeletedata}
                                    handleclose={handleclosedeletedata}
                                ></Deletedata>
                                <Updatedata 
                                    refresh={props.refresh}
                                    token={bakerytoken}
                                    id={id}
                                    db="bakery"
                                    active={activeupdatedata} 
                                    handlclose = {handlecloseupdatedata}
                                    selectedcolumn={selectedcolumn}
                                    type={type}
                                    accept={accept}
                                    >
                                <div>
                                        <label>
                                            <p>Choose an option:</p>
                                            <select className="column-container" value={selectedcolumn} onChange={handleChange}>
                                                <option value="">Select...</option>
                                                <option value="BakeryName">bakeryname</option>
                                                <option value="BakeryType">bakerytype</option>
                                                <option value="ManagerId">managerid</option>
                                                <option value="Location">location</option>
                                                <option value="TotalWorkers">totalworkers</option>
                                                <option value="TotalDayToBakeProductsGoal">totaldaytobakeproductsgoal</option>
                                                <option value="TotalMonthtoBakeProductsGoal">totalmonthtobakeproductsgoal</option>
                                                <option value="TotalYearToBakeProductsGoal">totalyeartobakeproductsgoal</option>
                                                <option value="TotalDayToSendoutProductsGoal">totaldaytosendoutproductsgoal</option>
                                                <option value="TotalMonthToSendoutProductsGoal">totalmonthtosendoutproductsgoal</option>
                                                <option value="TotalYearToSendoutProductsGoal">totalyeartosendoutproductsgoal</option>
                                                <option value="BakeryImage">bakeryimage</option>
                                            </select>
                                        </label>
                                    </div>
                                </Updatedata>
                </div>
                </>
            )
       }
       function BekeryStatus(){
        const [daydata,setdaydata] = useState(false)
        const [monthdata,setmonthdata] = useState(true)
        const [yeardata,setyeardata] = useState(false)
        const [labels,setlabels] = useState()
        const [bakedgraphdata,setbakedgraphdata] = useState()
        const [sendoutgraphdata,setsendoutgraphdata] = useState()
        const [bakedtitle,setbakedtitle] = useState("Month baked data")
        const [sendouttitle,setsendouttitle] = useState("Month send out data")

        useEffect(() => {
              
            if (daydata){
                setbakedtitle("Day baked data")
                setsendouttitle("Day send out data")
                if (id){
                    const newLabels = [];
                    const newbakedGraphData = [];
                    const newsendoutGraphData = [];
                    for(let i=0; i< bakerydaydata.length;i++) {
                        if (item.deliveryid == bakerydaydata[i]['deliveryid']){
                            newLabels.push(bakerydaydata[i]["date"]);
                            newbakedGraphData.push(bakerydaydata[i]["totalbakedproducts"]);
                            newsendoutGraphData.push(bakerydaydata[i]["totalsendoutproducts"]);
                        }
                    }
                    setlabels(newLabels)
                    setbakedgraphdata(newbakedGraphData)
                    setsendoutgraphdata(newsendoutGraphData)
                }
             }
             if (monthdata){
                setbakedtitle("Month baked data")
                setsendouttitle("Month send out data")
                 if (id){
                    const newLabels = [];
                    const newbakedGraphData = [];
                    const newsendoutGraphData = [];
                    for(let i=0; i< bakerymonthdata.length;i++) {
                        if (item.deliveryid == bakerymonthdata[i]['deliveryid']){
                            newLabels.push(bakerymonthdata[i]["date"]);
                            newbakedGraphData.push(bakerymonthdata[i]["monthtotalbakedproducts"]);
                            newsendoutGraphData.push(bakerymonthdata[i]["monthtotalsendoutproducts"]);
                        }
                    }
                    setlabels(newLabels)
                    setbakedgraphdata(newbakedGraphData)
                    setsendoutgraphdata(newsendoutGraphData)
                }
             }
             if (yeardata){
                setbakedtitle("Year baked data")
                setsendouttitle("Year send out data")
                 if (id){
                    const newLabels = [];
                    const newbakedGraphData = [];
                    const newsendoutGraphData = [];
                    for(let i=0; i< bakeryyeardata.length;i++) {
                        if (item.branchid == bakeryyeardata[i]['branchid']){
                            newLabels.push(bakeryyeardata[i]["date"])
                            newbakedGraphData.push(bakeryyeardata[i]["yeartotalbakedproducts"])
                            newsendoutGraphData.push(bakeryyeardata[i]["yeartotalsendoutproducts"])
                        }
                    }
                    setlabels(newLabels)
                    setbakedgraphdata(newbakedGraphData)
                    setsendoutgraphdata(newsendoutGraphData)
                }
              }
          }, [daydata, monthdata, yeardata,id,bakerydaydata, bakerymonthdata, bakeryyeardata, item]);

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
        const bakeddata = {
            labels:labels,
            datasets: [
              {
                label: 'Sales',
                data: bakedgraphdata,
                backgroundColor: 'rgba(75,192,192,0.6)',
              },
            ],
          };
          const sendoutdata = {
            labels:labels,
            datasets: [
              {
                label: 'Sales',
                data: sendoutgraphdata,
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
                <div style={chartStyles.title}>{bakedtitle}</div>
                <Bar data={bakeddata} options={options} />
                <div style={chartStyles.title}>{sendouttitle}</div>
                <Bar data={sendoutdata} options={options} />
                </div>
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
        const [searchTerm, setSearchTerm] = useState("");
        const combinedProductData = bakerydata.map(bakeryData => {
            const productData = productdata.find(y => y.bakeryid === bakeryData.bakeryid);
            const bakeryproductData = bakeryproductdata.find(x => x.bakeryid === bakeryData.bakeryid);
            return { ...bakeryData, ...productData, ...bakeryproductData};
        });
        const filteredProductData = useMemo(() => combinedProductData.filter(
            (item) => 
              (item.bakeryname && item.bakeryname.toLowerCase().includes(searchTerm.toLowerCase()))
          ), [combinedProductData, searchTerm]);
        function ProductsGraph(){
            const [labels,setlabels] = useState([])
            const [bakedgraphdata,setbakedgraphdata] = useState()
            const [sendoutgraphdata,setsendoutgraphdata] = useState()
            const [bakedtitle,setbakedtitle] = useState("baked data")
            const [sendouttitle,setsendouttitle] = useState("send out data")
            
            useEffect(() => {
                if (id) {
                  const newLabels = [];
                  const newbakedGraphData = [];
                  const newsendoutGraphData = [];
                  for (let i = 0; i < productdata.length; i++) {
                    if (item.branchid === productdata[i]['branchid']) {
                      newLabels.push(productdata[i]["date"]);
                      newbakedGraphData.push(productdata[i]["numberofproductbaked"]);
                      newsendoutGraphData.push(productdata[i]["totalproductssendout"]);
                    }
                  }
                  setlabels(newLabels);
                  setbakedgraphdata(newbakedGraphData);
                  setsendoutgraphdata(newsendoutGraphData);
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
            const bakedddata = {
                labels: labels,
                datasets: [
                  {
                    label: 'Sales',
                    data:bakedgraphdata,
                    backgroundColor: 'rgba(75,192,192,0.6)',
                  },
                ],
              };
              const sendoutdata = {
                labels: labels,
                datasets: [
                  {
                    label: 'Sales',
                    data: sendoutgraphdata,
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
                    <div style={chartStyles.title}>{bakedtitle}</div>
                    <Bar data={bakedddata} options={options} />
                    <div style={chartStyles.title}>{sendouttitle}</div>
                    <Bar data={sendoutdata} options={options} />
                    </div>
                    </div>
                </>
            )
        }
        function ProductsTable(){
            return(
                <>
                    <div className="generalinfoP-container">
                            <p style={{width:"260px"}}>all information about bakery products in table</p>
                    </div>
                    <div className="productstable-container">
                    <table>
                            <thead>
                                <tr>
                                    <th>Time</th>
                                    <th>BakeryName</th>
                                    <th>ProductId</th>
                                    <th>ProductName</th>
                                    <th>TimeOfBakery</th>
                                    <th>TotalBakedProducts</th>
                                    <th>TotalProductsSendOut</th>
                                    <th>ProductsRemaining</th>
                                    <th>ProductsUsedForBakery</th>
                                    <th>MoneyUsedToBakeTheProduct</th>
                                    <th>TotalBakedProductValue</th>
                                    <th>TotalProductsSendOutValue</th>
                                    <th>OneProductValueInMoney</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filteredProductData.map((data,index) =>(
                                <tr key={index}>
                                    <td>{data.time}</td>
                                    <td>{data.bakeryname}</td>
                                    <td>{data.productid}</td>
                                    <td>{data.productname}</td>
                                    <td>{data.timeofbakery}</td>
                                    <td>{data.numberofproductbaked}</td>
                                    <td>{data.totalproductssendout}</td>
                                    <td>{data.numberofproductsremaining}</td>
                                    <td>{data.usedproductsforbakery}</td>
                                    <td>{data.moneyusedtobaketheproduct}</td>
                                    <td>{data.totalbakedproductvalue}</td>
                                    <td>{data.totalsendoutproductvalue}</td>
                                    <td>{data.oneproductvalue}</td>
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
                <div className="bakedproducts-container">
                    <div className="searche-container">
                        <input type="text" placeholder="searche" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)}/>
                    </div>
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
                    refresh={props.refresh}
                />
                <Addbakerycomponentes
                    active = {props.ativeadd}
                    refresh={props.refresh}
                />
                <Fullbakeryinfocomponentes
                    active = {props.activebekeryinfo}
                    refresh={props.refresh}
                />
                <BakedProducts
                    active = {props.activebakedproducts}
                    refresh={props.refresh}
                />
            </div>
        </>
    )
}
function Bakery(props){
    const [main, setmain] = useState(false)
    const [add, setadd] = useState(false)
    const [fullbekeryinfo, setfullbekeryinfo] = useState(true)
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
                bakerydata={props.bakerydata}
                bakeryproductdata={props.bakeryproductdata}
                bakerydaydata={props.bakerydaydata}
                bakerymonthdata={props.bakerymonthdata}
                bakeryyeardata={props.bakeryyeardata}
                productdata={props.productdata}


                refresh={props.refresh}
                token={props.token}
            />
        </div>
        </>
    ): ""
}

export default Bakery;