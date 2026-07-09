import { useState } from "react";

import { useNavigate } from "react-router-dom";

import "../styles/login.css";

function Login() {

    const navigate = useNavigate();

    const [isLogin, setIsLogin] = useState(true);

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const [name, setName] = useState("");

    const [message, setMessage] = useState("");

    const [loading, setLoading] = useState(false);


    async function handleSubmit() {

        if (

            email.trim() === "" ||

            password.trim() === ""

        ) {

            setMessage(

                "Please fill all required fields"

            );

            return;
        }

        if (

            !isLogin &&

            name.trim() === ""

        ) {

            setMessage(

                "Please enter your full name"

            );

            return;
        }

        setLoading(

            true

        );

        setMessage("");

        const endpoint = isLogin

            ?

            "http://127.0.0.1:8000/login"

            :

            "http://127.0.0.1:8000/signup";

        try {

            const response = await fetch(

                endpoint,

                {

                    method: "POST",

                    headers: {

                        "Content-Type":

                            "application/json"

                    },

                    body: JSON.stringify({

                        email,

                        password,

                        name

                    })

                }

            );

            const data =

                await response.json();

            if (

                response.ok

            ) {

                setMessage(

                    data.message ||

                    "Success"

                );

                if (

                    isLogin &&

                    data.message === "success"

                ) {

                    localStorage.setItem(

                        "user_id",

                        data.user_id

                    );

                    navigate(

                        "/preferences"

                    );

                }

                if (

                    !isLogin &&

                    data.user_id

                ) {

                    setMessage(

                        "Account created successfully"

                    );

                    setIsLogin(

                        true

                    );

                }

            }

            else {

                setMessage(

                    data.detail ||

                    "Something went wrong"

                );

            }

        }

        catch (

            err

        ) {

            setMessage(

                "Backend connection failed"

            );

        }

        setLoading(

            false

        );

    }

    return (

        <div className="container">

            <div className="card">

                <h1 className="logo">

                    Stay<span>Wise</span>

                </h1>

                <p className="subtitle">

                    AI Hotel Review Intelligence

                </p>

                <h2 className="heading">

                    {

                        isLogin

                        ?

                        "Welcome Back"

                        :

                        "Create Account"

                    }

                </h2>

                {

                    !isLogin &&

                    <input

                        type="text"

                        placeholder="Full Name"

                        value={name}

                        onChange={(e)=>

                            setName(

                                e.target.value

                            )

                        }

                    />

                }

                <input

                    type="email"

                    placeholder="Email"

                    value={email}

                    onChange={(e)=>

                        setEmail(

                            e.target.value

                        )

                    }

                />

                <input

                    type="password"

                    placeholder="Password"

                    value={password}

                    onChange={(e)=>

                        setPassword(

                            e.target.value

                        )

                    }

                />

                {

                    message &&

                    <p className="message">

                        {message}

                    </p>

                }

                <button

                    onClick={handleSubmit}

                >

                    {

                        loading

                        ?

                        "Please wait..."

                        :

                        (

                            isLogin

                            ?

                            "Login"

                            :

                            "Create Account"

                        )

                    }

                </button>

                <p

                    className="toggle"

                    onClick={() => {

                        setIsLogin(

                            !isLogin

                        );

                        setMessage("");

                    }}

                >

                    {

                        isLogin

                        ?

                        "Don't have an account? Create one"

                        :

                        "Already have an account?"

                    }

                </p>

            </div>

        </div>

    );

}

export default Login;
