import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Preferences from "./pages/Preferences";
import Search from "./pages/Search";
import HotelResults from "./pages/HotelResults";

function App(){

  return(

    <BrowserRouter>

      <Routes>

        <Route

          path="/"

          element={<Login/>}

        />

        <Route

          path="/preferences"

          element={<Preferences/>}

        />

        <Route

          path="/search"

          element={<Search/>}

        />

        <Route

          path="/results"

          element={<HotelResults/>}

        />

      </Routes>

    </BrowserRouter>

  )

}

export default App;