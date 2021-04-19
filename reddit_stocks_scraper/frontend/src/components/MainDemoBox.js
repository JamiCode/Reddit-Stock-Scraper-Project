import React from 'react';
import { render } from "react-dom";
import DemoBoxHot from "./DemoBoxHot";
import DemoBoxTop from "./DemoBoxTop";
import DemoBoxNew from "./DemoBoxNew";
import Alert from "@material-ui/lab/Alert";

import { 
	Grid, 
	Box, 
	Button, 
	Typography,
	Paper,
	Divider,
} from '@material-ui/core';


// styles section
const alertStyle = {
	width:"50%",
	margin:0,
	marginLeft:78
}

const HeaderButtonStyle = {
	width:525,
	marginTop:100,
	fontSize:14,
}


export default class MainDemoBox extends React.Component {

	constructor(props) {
		super(props);
		this.state = {
			onShow:'hot'
		}
		this.buttonStyleActive = {
			borderBottom:'solid 3px red'
		}
		//bind zone
		this.handleHotButtonClick = this.handleHotButtonClick.bind(this);
		this.handleTopButtonClick = this.handleTopButtonClick.bind(this); 
		this.handleNewButtonClick = this.handleNewButtonClick.bind(this);
	}

	
	handleDemoRendering(){
		if (this.state.onShow === "hot") {
			return(
				<DemoBoxHot/>
			)
		}
		if (this.state.onShow === "top") {
			return(
				<DemoBoxTop/>
			)
		}
		if (this.state.onShow === "new") {
			return(
				<DemoBoxNew/>
			)
		}
	}

	handleHotButtonClick(event){
		this.setState({
			onShow:'hot',
		})
		this.buttonStyle['borderBottom'] = "solid 1px red";
	}

	handleTopButtonClick(event){
		this.setState({
			onShow:'top',
		})
	}

	handleNewButtonClick(event){
		this.setState({
			onShow:'new',
		})
	}

	handleHotStyle(){
		if (this.state.onShow === 'hot') {
			return(
				this.buttonStyleActive
			)
		}
		else{
			return(
				{}
			)
		}
	}

	handleTopStyle(){
		if (this.state.onShow === 'top') {
			return(
				this.buttonStyleActive
			)
		}
		else{
			return(
				{}
			)
		}
	}

	handleNewStyle(){
		if (this.state.onShow === 'new') {
			return(
				this.buttonStyleActive
			)
		}
		else{
			return(
				{}
			)
		}
	}

	render() {
		return (
			<div> 
				<div className="tabs__container">
					{/*<center> 
						<i>
							<p className="demoText" style={HeaderButtonStyle}> 
								<i className="fas fa-bolt"></i> Subreddit Demo Live Feed <i class="fas fa-bolt"></i> 
							</p>
						</i>
					</center>*/}
					<button
					style={this.handleHotStyle()} 
					className="tabs_button tab-hot-hover" 
					onClick={this.handleHotButtonClick}
					> <i className="fab fa-hotjar"></i> &nbsp; Hot &nbsp; <i className="fab fa-reddit-alien"></i> 
					</button>
					<button 
					style={this.handleTopStyle()}
					className="tabs_button tab-top-hover" 
					onClick={this.handleTopButtonClick}
					> 
						<i className="fas fa-arrow-up"></i> &nbsp; Top &nbsp;<i className="fab fa-reddit-alien"></i>
					</button>
					<button 
					style={this.handleNewStyle()}
					className="tabs_button tab-new-hover" 
					onClick={this.handleNewButtonClick}
					>
						<i className="far fa-newspaper"></i> &nbsp; New &nbsp;<i className="fab fa-reddit-alien"></i> 
					</button> 
					
				</div>
				{this.handleDemoRendering()}
			</div>
		);
	}
}


