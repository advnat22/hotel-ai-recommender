import { useEffect,useState } from "react";

import "../styles/Results.css";

function HotelResults(){

    const [hotels,setHotels]=useState([]);

    useEffect(()=>{

        fetch(

            "http://127.0.0.1:8000/search"

        )

        .then(

            res=>res.json()

        )

        .then(

            data=>setHotels(data)

        );

    },[]);

    return(

        <div className="resultsContainer">

            <h1 className="resultsTitle">

                Recommended Hotels

            </h1>

            <div className="hotelGrid">

                {

                    hotels.map(

                        (hotel,index)=>

                        <div

                            className="hotelCard"

                            key={hotel.name}

                        >

                            <div className="rankBadge">

                                #{index+1}

                            </div>

                            <h2 className="hotelName">

                                {hotel.name}

                            </h2>

                            <p className="hotelInfo">

                                ⭐ Rating: {hotel.rating}

                            </p>

                            <p className="hotelInfo">

                                📍 {hotel.address}

                            </p>

                            <div className="score">

                                AI Score: {hotel.score}

                            </div>

                            <div className="summaryBox">

                                <h4>

                                    AI Review Summary

                                </h4>

                                <p className="summary">

                                    {

                                        hotel.summary ||

                                        "Summary unavailable"

                                    }

                                </p>

                            </div>

                        </div>

                    )

                }

            </div>

        </div>

    );

}

export default HotelResults;