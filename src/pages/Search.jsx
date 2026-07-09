import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Search.css";

function Search(){

    const [location,setLocation]=useState("");

    const navigate=useNavigate();

    function handleSearch(){

        navigate(

            `/results?location=${location}`

        );
    }

    return(

        <div className="searchContainer">

            <div className="searchCard">

                <h1>

                    Find Your Hotel

                </h1>

                <p>

                    Personalized recommendations (Currently only works for Sentosa)

                </p>

                <input

                    placeholder="Sentosa"

                    value={location}

                    onChange={(e)=>

                        setLocation(

                            e.target.value

                        )

                    }

                />

                <button

                    onClick={handleSearch}

                >

                    Search Hotels

                </button>

            </div>

        </div>
    )
}

export default Search;
