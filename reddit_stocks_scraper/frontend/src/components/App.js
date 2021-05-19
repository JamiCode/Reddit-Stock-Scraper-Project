import React from "react";
import ReactDOM from "react-dom";
import DemoBoxHot from "./DemoBoxHot";
import { render } from "react-dom";
import MainDemoBox from "./MainDemoBox";

// Main App Component
class App extends React.Component {

	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div className="App">
				<MainDemoBox/>
			</div>
		);
	}
}





export default App;
const container = document.getElementById("react-app");
render(<App />, container);
