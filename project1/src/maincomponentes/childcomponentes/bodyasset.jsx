import React from "react";
import { useState } from "react";
import "./childcomponent-style/bodyasset.css"
import InsertData from "./grandchildcomponetes/insertdatapopup";
import Updatedata from "./grandchildcomponetes/updatedatapopup";
import Deletedata from "./grandchildcomponetes/deletedatapopup";

function AssetMainbar(props){
    return(
        <>
            <div className="assetMainbar-conatiner">
                <button onClick={props.funcbranchasset}>Branch Asset</button><br></br>
                <button onClick={props.funcdeliveryasset}>Delivery Asset</button><br></br>
                <button onClick={props.funcbakeryasset}>Bakery Asset</button><br></br>
                <button onClick={props.funcaddasset}>Add Asset</button><br></br>
                <button onClick={props.funcfullassetinfo}>FullAsset Info</button>
            </div>
        </>
    )
}
function AssetSidebar(props){
    function BranchAsset(props){
        function BranchAssetTable(props){
            return(
                <>
                    <div className="branchassettable-container">
                    <table>
                                <thead>
                                    <tr>
                                        <th>BranchId</th>
                                        <th>AssetId</th>
                                        <th>NumberOfAsset</th>
                                        <th>ValueOfAsset</th>
                                        <th>AssetOwnedDate</th>
                                        <th>TotalValueofAsset</th>
                                        <th>TotalStatusofAsset</th>
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
                <div className="branchasset-container">
                    <BranchAssetTable/>
                </div>
            </>
        ):""
    }
    function DeliveryAsset(props){
        function DeliveryAssetInTable(props){
            return(
                <>
                    <div className="deliveryassetintable-container">
                        <table>
                                        <thead>
                                            <tr>
                                                <th>DeliveryId</th>
                                                <th>AssetId</th>
                                                <th>NumberOfAsset</th>
                                                <th>ValueOfAsset</th>
                                                <th>AssetOwnedDate</th>
                                                <th>TotalValueofAsset</th>
                                                <th>TotalStatusofAsset</th>
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
                <div className="deliveryasset-container">
                    <DeliveryAssetInTable/>
                </div>
            </>
        ):""
    }
    function BakeryAsset(props){
        function BakeryAssetInTable(props){
            return(
                <>
                    <div className="bakeryassetintable-container">
                    <table>
                                    <thead>
                                        <tr>
                                            <th>DeliveryId</th>
                                            <th>AssetId</th>
                                            <th>NumberOfAsset</th>
                                            <th>ValueOfAsset</th>
                                            <th>AssetOwnedDate</th>
                                            <th>TotalValueofAsset</th>
                                            <th>TotalStatusofAsset</th>
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
                <div className="bakerasset-container">
                        <BakeryAssetInTable/>
                </div>
            </>
        ):""
    }
    function AddAsset(props){
        function Doneinfo(props){
            return(
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)"}}>user submited asset information</p>
                    </div>
                    <div className="doneinfo-contaner">
                        <div className="submitedinfo-container">
                            <p>test</p>
                        </div>
                    </div>
                </>
            )
        }
        function Forminfo(props){
            const [ownerdename, setownerdename] = useState('');
            const [ownerid, setownerid] = useState(null);
            const [assetname, setassetname] = useState('');
            const [numberofasset, setnumberofasset] = useState(null);
            const [assettype, setassettype] = useState('');
            const [assetvalue, setassetvalue] = useState(null);
            const [location, setlocation] = useState('');
            const [assetstatus, setassetstatus] = useState('');
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
                        <p>submit information about asset</p>
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
                                <label>
                                        <select value={ownerdename} onChange={(e)=>setownerdename(e.target.value)}>
                                            <option value="">Select owner department name</option>
                                            <option value="branch">branch</option>
                                            <option value="delivery">delivery</option>
                                            <option value="bakery">bakery</option>
                                        </select>
                                </label><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter owner id"
                                    value={ownerid}
                                    onChange={(e)=>setownerid(e.target.value)}
                                    /><br/>
                                <input 
                                    type="text" 
                                    placeholder="Enter asset name"
                                    value={assetname}
                                    onChange={(e)=>setassetname(e.target.value)}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter number of asset"
                                    value={numberofasset}
                                    onChange={(e)=>setnumberofasset(e.target.value)}
                                    /><br/>
                                <input 
                                    type="text" 
                                    placeholder="Enter asset type"
                                    value={assettype}
                                    onChange={(e)=>setassettype(e.target.value)}
                                    /><br/>
                                <input 
                                    type="number" 
                                    placeholder="Enter asset value"
                                    value={assetvalue}
                                    onChange={(e)=>setassetvalue(e.target.value)}
                                    /><br/>
                                <input 
                                    type="text" 
                                    placeholder="Enter asset location"
                                    value={location}
                                    onChange={(e)=>setlocation(e.target.value)}
                                    /><br/>
                                <input 
                                    type="text" 
                                    placeholder="Enter asset status"
                                    value={assetstatus}
                                    onChange={(e)=>setassetstatus(e.target.value)}
                                    /><br/>
                                <button type="submit"onClick={handleSubmit}>submit</button>
                        </form>
                    </div>
                    {activeinsertdata && (
                            <InsertData
                              activeinsertdata={activeinsertdata}
                              db='asset'
                              data={{
                                assetname,
                                ownerdename,
                                ownerid,
                                numberofasset,
                                assettype,
                                assetvalue,
                                location,
                                assetstatus,
                                selectedImage
                              }}
                              handleclose={handleclose}
                            />
                          )}
                </>
            )
        }

        return props.active ?(
            <>
                <div className="addasset-container">
                    <Doneinfo/>
                    <Forminfo/>
                </div>
            </>
        ):""
    }
    function FullAssetInfo(props){
        function AssetInTable(props){
            return(
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",width:'240px'}}>all information about transaction in graph</p>
                    </div>
                    <div className="searche-container">
                                <input type="text" placeholder="searche"/>
                    </div>
                    <div className="fullassetinfointable-container">
                        <table>
                                        <thead>
                                            <tr>
                                                <th>AssetId</th>
                                                <th>AssetName</th>
                                                <th>AssetType</th>
                                                <th>VicalPlateNumber</th>
                                                <th>NumberOfAsset</th>
                                                <th>AssetValueIn$</th>
                                                <th>AssetOwnedDate</th>
                                                <th>TotalValueofAssetIn$</th>
                                                <th>TotalStatusofAsset</th>
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
        function AssetStatus(props){
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
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",width:'240px'}}>all status information about asset</p>
                    </div>
                    <div className="assetstatus-container">
                        <div className="manageasset-buttoncontainer">
                            <button className="manageasset-button" onClick={() => setactive(true)}>Manage asset</button>
                        </div>
                    </div>
                </>
            )
        }
        return props.active ?(
            <>
                <div className="fullassetInfo-container">
                        <AssetInTable/>
                        <AssetStatus/>
                </div>
            </>
        ):""
    }
    return(
        <>
            <div className="assetsidebar-container">
                    <BranchAsset
                        active = {props.activebranchasset}
                    />
                    <DeliveryAsset
                        active = {props.activedeliveasset}
                    />
                    <BakeryAsset
                        active = {props.activebakeryasset}
                    />
                    <AddAsset
                        active = {props.activeaddasset}
                    />
                    <FullAssetInfo
                        active = {props.activefullassetinfo}
                    />
            </div>
        </>
    )
}
function Asset(props){
    const [branchasset, setbranchasset] = useState(true)
    const [deliveryasset, setdeliveryasset] = useState(false)
    const [bakeryasset, setbakeryasset] = useState(false)
    const [addasset, setaddasset] = useState(false)
    const [fullassetinfo, setfullassetinfo] = useState(false)


    function activebranchasset(){
        setdeliveryasset(false)
        setbakeryasset(false)
        setfullassetinfo(false)
        setaddasset(false)
        return setbranchasset(true)
    }

    function activedeliveryasset(){
        setbranchasset(false)
        setbakeryasset(false)
        setfullassetinfo(false)
        setaddasset(false)
        return setdeliveryasset(true)
    }
    function activebakeryasset(){
        setbranchasset(false)
        setdeliveryasset(false)
        setfullassetinfo(false)
        setaddasset(false)
        return setbakeryasset(true)
    }
    function activefullassetinfo(){
        setbranchasset(false)
        setdeliveryasset(false)
        setbakeryasset(false)
        setaddasset(false)
        return setfullassetinfo(true)
    }
    function activeaddasset(){
        setbranchasset(false)
        setdeliveryasset(false)
        setbakeryasset(false)
        setfullassetinfo(false)
        return setaddasset(true)
    }
    return props.active ?(
        <>
            <div className="asset-container">
                    <AssetMainbar
                        funcbranchasset = {activebranchasset}
                        funcdeliveryasset = {activedeliveryasset}
                        funcbakeryasset = {activebakeryasset}
                        funcfullassetinfo = {activefullassetinfo}
                        funcaddasset = {activeaddasset}
                    />
                    <AssetSidebar
                        activebranchasset = {branchasset} 
                        activedeliveasset = {deliveryasset}
                        activebakeryasset =  {bakeryasset}
                        activefullassetinfo = {fullassetinfo}
                        activeaddasset = {addasset}
                    />

            </div>
        </>
    ):""    
}

export default Asset;