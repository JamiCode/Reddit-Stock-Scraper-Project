import React, {useEffect, useState} from 'react';
import { render } from "react-dom";
import WallStreetBetsGraph from "./WallStreetBetsGraph";


const App = (props) => {


  return (
    <div>
     	<WallStreetBetsGraph/>
    </div>
  )
}

export default App; 
const container = document.getElementById("react");
render(<App />, container);
