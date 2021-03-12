import React from 'react';
import { render } from "react-dom";

export default class App extends React.Component {

	constructor(props) {
		super(props);
		this.state = {
			stock_ticker:null,
			stock_mentions:null
		};
		//BIND ZONE
		this.handlegetRedditDatabase = this.handlegetRedditDatabase.bind(this)
	}

	handlegetRedditDatabase(){
		fetch("reddit/api/stocks-overall-view-wallstreetbets")
		.then((respone)=> {
			if (respone.status > 400) {
				console.log("Something Went wrong")
			} else {
				console.log("Api call works perfectly")
			}
			return respone.json()
		})
		.then((data)=>{
			console.log(data)
		})
	}

	render() {
		return (
			<div>
				<h1> Click the button below to get </h1>
				<button className="btn btn-success" onClick={this.handlegetRedditDatabase}> LOL </button>
			</div>
		);
	}
}
const container = document.getElementById("react-app");
render(<App />, container);