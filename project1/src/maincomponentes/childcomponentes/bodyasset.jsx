import React from "react";
import { useState } from "react";
import Modal from "./grandchildcomponetes/modal1";
import "./childcomponent-style/bodyasset.css"

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
            return(
                <>
                    <div className="generalinfoP-container">
                        <p>submit information about asset</p>
                    </div>
                    <div className="forminfo-container">
                        <form className="forminput-container">
                                <input type="text" placeholder="Enter branch name"/><br/>
                                <input type="text" placeholder="Enter branch location"/><br/>
                                <input type="text" placeholder="Enter branch controler"/><br/>
                                <input type="number" placeholder="Enter delivery id"/><br/>
                                <input type="text" placeholder="Enter Branch type"/><br/>
                                <input type="text" placeholder="Enter Branch sell goal"/><br/>
                                <button>submit</button>
                        </form>
                    </div>
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
                        <Modal active={active} func ={nextbtn} close = {()=> setactive(false)}>
                            <p>test</p>
                        </Modal>
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