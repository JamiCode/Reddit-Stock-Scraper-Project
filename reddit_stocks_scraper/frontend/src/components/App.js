import React from 'react';
import DemoBox from "./DemoBox"
import { render } from "react-dom";

class App extends React.Component {

	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div>
				<div className="DemoBox">
				<DemoBox/>
				</div>
			</div>
		);
	}
}

export default App;
const container = document.getElementById("react-app");
render(<App />, container);