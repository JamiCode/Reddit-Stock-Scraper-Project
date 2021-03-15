import React from 'react';
import {makeStyles} from "@material-ui/core/styles";
import { 
	Grid, 
	Box, 
	Button, 
	Typography,
	Paper,
	Divider
} from '@material-ui/core';

//style

const paperStyle = {
	padding:14,
	backgroundColor:'powderblue',
}
const DemoStyle = {
	backgroundColor:'#343a40',
}


export class Submission extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			text:this.props.text
		}
	}


	render() {
		return (
			<Grid item xs={12}>
				<Paper style={paperStyle} variant="outlined">  
					<Typography> {this.state.text} </Typography> 
				</Paper>
				<hr/>
			</Grid>

		);
	}
}


export default class DemoBox extends React.Component {
	//Variables zone 
	constructor(props) {
		super(props);
		this.state = {
			//Nothing for now in out state
		}
	}

	render() {
		return (
			<div className="demo">
				<Grid 
				container 
				spacing={3}
				>	
					<Submission text="Loading Making Api Call"/>
				</Grid>
			</div>
		);
	}
}

