import React from 'react';
import DemoBoxHot from "./DemoBoxHot";
import { render } from "react-dom";
import MainDemoBox from "./MainDemoBox"


// Main App Component
class App extends React.Component {

	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div>
				<div className="DemoBox">
				<MainDemoBox/>
				</div>
			</div>
		);
	}
}

export default App;
const container = document.getElementById("react-app");
render(<App />, container);