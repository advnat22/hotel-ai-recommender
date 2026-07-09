import { useState } from "react";

import { useNavigate } from "react-router-dom";

import "../styles/Preferences.css";

function Preferences() {

    const navigate = useNavigate();

    const [budget,setBudget] = useState("");

    const [tripType,setTripType] = useState("");

    const [food,setFood] = useState("Medium");

    const [transport,setTransport] = useState("Medium");

    const [luxury,setLuxury] = useState("Medium");

    const [cleanliness,setCleanliness] = useState("Medium");


    async function savePreferences(){

        const user_id = localStorage.getItem(

            "user_id"

        );

        const data={

            user_id,

            budget,

            trip_type:tripType,

            food,

            transport,

            luxury,

            cleanliness

        };

        try{

            const response = await fetch(

                "https://hotel-ai-recommender.onrender.com/preferences",

                {

                    method:"POST",

                    headers:{

                        "Content-Type":

                        "application/json"

                    },

                    body:JSON.stringify(

                        data

                    )

                }

            );

            const result =

            await response.json();

            console.log(

                result

            );

            alert(

                "Preferences Saved"

            );

            navigate(

                "/search"

            );

        }

        catch(err){

            alert(

                "Save failed"

            );

        }

    }


    function createButtons(

        value,

        setter,

        options,

        activeClass

    ){

        return(

            <div className="segment">

                {

                    options.map(

                        (option)=>

                        <button

                            key={option}

                            type="button"

                            className={

                                value===option

                                ?

                                `segmentBtn active ${activeClass}`

                                :

                                "segmentBtn"

                            }

                            onClick={()=>

                                setter(

                                    option

                                )

                            }

                        >

                            {option}

                        </button>

                    )

                }

            </div>

        );

    }


    return(

        <div className="prefContainer">

            <div className="leftSide">

                <h1>

                    Build Your

                    <span>

                        Travel DNA

                    </span>

                </h1>

                <p>

                    Tell us what matters most.

                    We personalize hotel reviews,

                    rankings and recommendations

                    around your travel style.

                </p>

                <div className="floatingCards">

                    <div className="miniCard">

                        🏨 Smart Ranking

                    </div>

                    <div className="miniCard">

                        ✨ AI Insights

                    </div>

                    <div className="miniCard">

                        📍 Personalized Hotels

                    </div>

                    <div className="miniCard">

                        🧠 Review Intelligence

                    </div>

                </div>

            </div>


            <div className="prefCard">

                <h2>

                    Preferences

                </h2>

                <p>

                    Configure your travel profile

                </p>


                <div className="prefSection">

                    <label>

                        Budget Preference

                    </label>

                    {

                        createButtons(

                            budget,

                            setBudget,

                            [

                                "Budget",

                                "Mid",

                                "Luxury"

                            ],

                            "medium"

                        )

                    }

                </div>


                <div className="prefSection">

                    <label>

                        Trip Type

                    </label>

                    {

                        createButtons(

                            tripType,

                            setTripType,

                            [

                                "Solo",

                                "Couple",

                                "Family",

                                "Business"

                            ],

                            "high"

                        )

                    }

                </div>


                {

                    [

                        [

                            "Food Importance",

                            food,

                            setFood

                        ],

                        [

                            "Transport Importance",

                            transport,

                            setTransport

                        ],

                        [

                            "Luxury Importance",

                            luxury,

                            setLuxury

                        ],

                        [

                            "Cleanliness Importance",

                            cleanliness,

                            setCleanliness

                        ]

                    ].map(

                        ([title,val,setter])=>

                        <div

                            className="prefSection"

                            key={title}

                        >

                            <label>

                                {title}

                            </label>

                            {

                                createButtons(

                                    val,

                                    setter,

                                    [

                                        "Low",

                                        "Medium",

                                        "High"

                                    ],

                                    val.toLowerCase()

                                )

                            }

                        </div>

                    )

                }

                <button

                    className="saveBtn"

                    onClick={savePreferences}

                >

                    Save Preferences

                </button>

            </div>

        </div>

    );

}

export default Preferences;
