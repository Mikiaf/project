import React from "react";
import { useState } from "react";
import './childcomponent-style/bodybusiness.css'




function BusinessMainbar(props){
    return(
        <>
            <div className="businessmainbar-container">
                <button onClick={props.functrans}>Transaction</button><br></br>
                <button onClick={props.funcsell}>Sale Status</button><br></br>
                <button onClick={props.funcsalary}>salary status</button>
                <button onClick={props.funcprolose}>profit and lose</button>
                <button onClick={props.funcorder}>order</button>
                <button onClick={props.funccost}>cost</button>
                <button onClick={props.funcconnection}>connection</button>
            </div>
        </>
    )
}
function BusinessSidebar(props){
    function Transaction(props){
        function TransactionGraph(){
            return (
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",width:'240px'}}>all information about transaction in graph</p>
                    </div>
                    <div className="transactiongraph-container">
                        <p>test</p>
                    </div>
                </>
            )
        }
        function TransactionInfoTable(){
            return (
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)"}}>all information transactionn in table</p>
                    </div>
                    <div className="transactioninfoTable-container">
                        <table>
                                <thead>
                                    <tr>
                                        <th>TransID</th>
                                        <th>TransTime</th>
                                        <th>TransType</th>
                                        <th>Transproduct</th>
                                        <th>TransFrom</th>
                                        <th>Transdeliver</th>
                                        <th>TransTo</th>
                                        <th>TransQuantity</th>
                                        <th>TransGoal</th>
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
                <div className="transaction-conatainer">
                    <TransactionGraph/>
                    <TransactionInfoTable/>
                </div>
            </>
        ) :""
    }
    function SellStatus(props){
            function SellStatusInGraph(){
                return(
                    <>
                        <div className="branchsellinfoP-container">
                            <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                            width: "370px",
                                            }}>all information about Branch selles and bakery send outes in graph</p>
                        </div>
                        <div className="sellstatusgraph-conatainer">
                            
                        </div>
                    </>
                )
            }
            function BranchSell(props){
                return(
                    <>
                        <div className="branchsellinfoP-container">
                            <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",
                                            width: "200px",
                                            }}>all information Branch selles in table</p>
                        </div>
                        <div className="branchsellinfoTable-container">
                        <table>
                                            <thead>
                                                <tr>
                                                    <th>BranchId</th>
                                                    <th>ControlersId</th>
                                                    <th>AcceptedProductIn$</th>
                                                    <th>DayBranchSellIn$</th>
                                                    <th>DaySellGoalIn$</th>
                                                    <th>M.BranchSellIn$</th>
                                                    <th>M.SellGoalIn$</th>
                                                    <th>YearBranchSellIn$</th>
                                                    <th>YearSellGoalIn$</th>
                                                    <th>TotalBranchSellIn$</th>
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
            function BakerySendOut(props){
                return(
                    <>
                        <div className="baksersendoutinfoP-container">
                            <p style={{backgroundColor:"rgba(180, 224, 159, 0.966)",
                                            width: "220px"}}>all information Bakery send out in table </p>
                        </div>
                        <div className="bakerysendoutTable-container">
                        <table>
                                            <thead>
                                                <tr>
                                                    <th>BakeryId</th>
                                                    <th>ManagersId</th>
                                                    <th>SendOutProductIn$</th>
                                                    <th>DayBakerySendOut</th>
                                                    <th>DaySendOutGoal</th>
                                                    <th>M.BakerySendOut</th>
                                                    <th>M.BakerySendGoalGoal</th>
                                                    <th>yearBakerySendOut</th>
                                                    <th>yearBakerySendOutGoal</th>
                                                    <th>TotalBranchSell</th>
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
                <div className="sellstatus-container">
                        <SellStatusInGraph/>
                        <BranchSell/>
                        <BakerySendOut/>
                </div>
            </>
        ):""
    }
    function SalaryStatus(props){
        function SalaryStatusGraph(props){
            return(
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",width:"250px"}}>All information about salarystatus in graph</p>
                    </div>
                    <div className="statusgraph-container">
                                test
                    </div>
                </>
            )
        }
        function SalaryStatusTable(props){
            return(
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",width:"250px"}
                    }>All information about salarystatus in table</p>
                    </div>
                    <div className="salarystatustable-container">
                    <table>
                                <thead>
                                    <tr>
                                        <th>BakeryEmployeSalary</th>
                                        <th>DeliveryEmployeSalary</th>
                                        <th>BranchEmployeSalary</th>
                                        <th>HighestPaidDepartment</th>
                                        <th>LowestPaidDepartment</th>
                                        <th>TotalSalaryPaidIn.M</th>
                                        <th>TotalSalaryPaidIn.y</th>
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
                <div className="salarystatus-container">
                    <SalaryStatusGraph/>
                    <SalaryStatusTable/>
                </div>
            </>
        ) : ""
    }
    function ProfitAndLose(props){
        function ProfitAndLoseGraph(props){
            return(
                <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgba(172, 203, 185, 0.966)",width:"300px"}}>all information about business profit and lose in graph</p>
                    </div>
                    <div className="prolosegraph-container">

                    </div>
                </>
            )
        }
        function ProfitAndLoseTable(props){
            return(
                <>
                    <div className="infoP-container">
                        <p style={{backgroundColor:"rgba(172, 203, 185, 0.966)",width:"300px"}}>all information about business profit and lose in table</p>
                    </div>
                    <div className="prolosetable-container">
                    <table>
                                <thead>
                                    <tr>
                                        <th>CompYearProfit</th>
                                        <th>CompMonthProfit</th>
                                        <th>CompDayProfit</th>
                                        <th>BranchWithMostSell</th>
                                        <th>BranchWithMostSellIN$</th>
                                        <th>BranchWithLeastSell</th>
                                        <th>BranchWithLeastSellIN$</th>
                                        <th>BakeryWithMostSendOutes</th>
                                        <th>BakeryWithMostSendOutesIN$</th>
                                        <th>BakeryWithLestSendOutes</th>
                                        <th>BakeryWithLestSendOutesIN$</th>
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
                <div className="profitandlose-container">
                        <ProfitAndLoseGraph/>
                        <ProfitAndLoseTable/>
                </div>
            </>
        ):""
    }
    function Order(props){
        function OrderGraph(){
            return (
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",width:'240px'}}>all information about transaction in graph</p>
                    </div>
                    <div className="ordergraph-container">
                        <p>test</p>
                    </div>
                </>
            )
        }
        function OrderInfoTable(){
            return (
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)"}}>all information transactionn in table</p>
                    </div>
                    <div className="orderinfoTable-container">
                        <table>
                                <thead>
                                    <tr>
                                        <th>TransID</th>
                                        <th>TransTime</th>
                                        <th>TransType</th>
                                        <th>Transproduct</th>
                                        <th>TransFrom</th>
                                        <th>Transdeliver</th>
                                        <th>TransTo</th>
                                        <th>TransQuantity</th>
                                        <th>TransGoal</th>
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
                <div className="order-conatainer">
                    <OrderGraph/>
                    <OrderInfoTable/>
                </div>
            </>
        ) :""
    }
    function Cost(props){
        function CostGraph(){
            return (
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",width:'240px'}}>all information about transaction in graph</p>
                    </div>
                    <div className="costgraph-container">
                        <p>test</p>
                    </div>
                </>
            )
        }
        function CostInfoTable(){
            return (
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)"}}>all information transactionn in table</p>
                    </div>
                    <div className="costinfoTable-container">
                        <table>
                                <thead>
                                    <tr>
                                        <th>TransID</th>
                                        <th>TransTime</th>
                                        <th>TransType</th>
                                        <th>Transproduct</th>
                                        <th>TransFrom</th>
                                        <th>Transdeliver</th>
                                        <th>TransTo</th>
                                        <th>TransQuantity</th>
                                        <th>TransGoal</th>
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
                <div className="cost-conatainer">
                    <CostGraph/>
                    <CostInfoTable/>
                </div>
            </>
        ) :""
    }
    function Connection(props){
        function ConnectionGraph(){
            return (
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)",width:'240px'}}>all information about transaction in graph</p>
                    </div>
                    <div className="connectiongraph-container">
                        <p>test</p>
                    </div>
                </>
            )
        }
        function ConnectionInfoTable(){
            return (
                <>
                    <div className="generalinfoP-container">
                        <p style={{backgroundColor:"rgba(152, 214, 193, 0.767)"}}>all information transactionn in table</p>
                    </div>
                    <div className="connectioninfoTable-container">
                        <table>
                                <thead>
                                    <tr>
                                        <th>TransID</th>
                                        <th>TransTime</th>
                                        <th>TransType</th>
                                        <th>Transproduct</th>
                                        <th>TransFrom</th>
                                        <th>Transdeliver</th>
                                        <th>TransTo</th>
                                        <th>TransQuantity</th>
                                        <th>TransGoal</th>
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
                <div className="connection-conatainer">
                    <ConnectionGraph/>
                    <ConnectionInfoTable/>
                </div>
            </>
        ) :""
    }
    return(
        <>
            <div className="businesssidebar-container">
                <Transaction
                    active = {props.activetrans}
                />
                <SellStatus
                    active = {props.activesell}
                />
                <SalaryStatus
                    active = {props.activesalary}
                />
                <ProfitAndLose
                    active={props.activeprolose}
                />
                <Order
                    active={props.activeorder}
                />
                <Cost
                    active={props.activecost}
                />
                <Connection
                    active={props.activeconnection}
                />
            </div>
        </>
    )
}



function Business(props){
        const [trans, settrans] = useState(true)
        const [sell, setsell] = useState(false)
        const [salary, setsalary] = useState(false)
        const [pro_lose, setprolose] = useState(false)
        const [order, setorder] = useState(false)
        const [cost, setcost] = useState(false)
        const [connection, setconnection] = useState(false)

        function activetrans(){
            setsell(false)
            setsalary(false)
            setprolose(false)
            return settrans(true)
        }
        function activesell(){
            setsalary(false)
            setprolose(false)
            settrans(false)
            return setsell(true)
        }
        function activesalary(){
           
            setprolose(false)
            settrans(false)
            setsell(false)
            return  setsalary(true)
        }
        function activeprolose(){
            settrans(false)
            setsell(false)
            setsalary(false) 
            return setprolose(true)
        }
        function activeorder(){
            setsell(false)
            setsalary(false)
            setprolose(false)
            settrans(false)
            return setorder(true)
        }
        function activecost(){
            setsell(false)
            setsalary(false)
            setprolose(false)
            settrans(false)
            setorder(false)
            return setcost(true)
        }
        function activeconnection(){
            setsell(false)
            setsalary(false)
            setprolose(false)
            settrans(false)
            setorder(false)
            setcost(true)
            return setconnection(true)
        }
    return props.active ?(
        <>
            <div className="business-container">
                <BusinessMainbar
                    functrans = {activetrans}
                    funcsell = {activesell}
                    funcsalary = {activesalary}
                    funcprolose = {activeprolose}
                    funcorder = {activeorder}
                    funccost = {activecost}
                    funcconnection = {activeconnection}
                />
                <BusinessSidebar
                    activetrans = {trans}
                    activesell = {sell}
                    activesalary = {salary}
                    activeprolose = {pro_lose}
                    activeorder = {order}
                    activecost = {cost}
                    activeconnection = {connection}
                />
            </div>
        </>
    ): ""
}

export default Business;