import React from 'react';
import {makeStyles} from "@material-ui/core/styles";
import Loader from "./images/loader.svg";
import { 
	Grid, 
	Box, 
	Button, 
	Typography,
	Paper,
	Divider,
	IconButton
} from '@material-ui/core';

//style zone

const paperStyle = {
	padding:8,
	backgroundColor:'powderblue',
	marginTop:4,
}
const DemoStyle = {
	backgroundColor:'#23272a',
}

const authorStyles = {
	fontFamily:'Kalam',
	color:'red'
}

const upvotesStyles = {
	color:"blue"
}

const submissionStyles = {
	fontSize:18,
}

const commentStyles = {
	color:"green",
}

const dateStyle = {
	color:"purple"
}

const LoaderStyle = {
	color:'#0d6aff'
}

const refreshStyle = {
	color:'black'
}


//EACH SUBMISSION COMPONENT----------------------------------
export class Submission extends React.Component {
	constructor(props) {
		super(props);
		this.state = {}
		//bind zone
		this.handlerRefreshClickEvent = this.handlerRefreshClickEvent.bind(this)
	}

	
	handlerRefreshClickEvent(event){
		const index = this.props.index
		this.props.onAuthorChange(index)
		this.props.onTextChange(index)
		this.props.onURLChange(index)
		this.props.onCommentsChange(index)
		this.props.onDateChange(index)
		this.props.onTimeChange(index)

	}

	handleTextRendering(){
		if (typeof(this.props.text) === 'string') {
			return(
				<Typography >
					<a className="submission-link" target="_blank" href={this.props.url}>  
						{this.props.text}
					</a>
				</Typography>
			)
		}

		if (typeof(this.props.text !== 'string')) {
			return(
				<p style={LoaderStyle}>
					<img alt="loader" src={Loader} height="40"/> <i> Connecting To API, wait for few seconds </i>
				</p>
			)
		}

	}


	handleAuthorRendering(){
		if (typeof(this.props.author) === 'string'){
			return(
				<p style={authorStyles}>
					By: {this.props.author}
				</p>
			)
		}

		if (typeof(this.props.author) !== 'string'){
			return(
				<p>
					&nbsp;
				</p>
			)
		}

	}

	handleRestRendering(){	
		if (typeof(this.props.text) === 'string') {
			return(
				<p style={upvotesStyles}> <i className="fas fa-thumbs-up"></i> {this.props.upvotes} upvotes    - <span style={commentStyles}> <i className="far fa-comments"></i> {this.props.comments} comments </span> <span style={dateStyle}> Date: {this.props.date} {this.props.time}</span>
					<br/>
					<span style={refreshStyle}> 
						 <button className="icon-button" onClick={this.handlerRefreshClickEvent}> 
						 	<i className="fas fa-redo"></i>
						 </button> 
					 </span>
				</p> 

			)
		}

		if (typeof(this.props.text) !== 'string') {
			<p> &nbsp; </p>
		} 
	}

	render() {
		return (
			<Grid item xs={12}>
				<Paper style={paperStyle} variant="outlined"> 
					{this.handleTextRendering()}
					{this.handleAuthorRendering()}
					{this.handleRestRendering()}
				</Paper>
				<hr/>
			</Grid>

		);
	}
}

//EACH SUBMISSION COMPONENT----------------------------------

// DEMO BOX MAIN COMPONENT
export default class DemoBoxTop extends React.Component {
	//Variables zone 
	constructor(props) {
		super(props);
		//constructs}
		//state
		this.state = {}
		this.mapTenSubmissionToTitle()
		//bind zone
		this.onAuthorChange 	= this.onAuthorChange.bind(this)
		this.onTitleChange 		= this.onTitleChange.bind(this)
		this.onURLChange 		= this.onURLChange.bind(this)
		this.onUpvotesChange 	= this.onUpvotesChange.bind(this)		
	}


	fetchDataTitle(index){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response) =>{ return response.json()})
		.then((data)=>{
			if (index === 0) {
				this.setState({
				title0:data[index].title
				})
			}
			if (index === 1) {
				this.setState({
				title1:data[index].title
				})
			}
			if (index === 2) {
				this.setState({
				title2:data[index].title
				})
			}
			if (index === 3) {
				this.setState({
				title3:data[index].title
				})
			}
			if (index === 4) {
				this.setState({
				title4:data[index].title
				})
			}
			if (index === 5) {
				this.setState({
				title5:data[index].title
				})
			}	 
			
		})
	}


	fetchDataUrl(index){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response) =>{ return response.json()})
		.then((data)=>{
			if (index === 0) {
				this.setState({
					url0:data[index].url
				})
			}
			if (index === 1) {
				this.setState({
				url1:data[index].url
				})
			}
			if (index === 2) {
				this.setState({
					url2:data[index].url
				})
			}
			if (index === 3) {
				this.setState({
					url3:data[index].url
				})
			}
			if (index === 4) {
				this.setState({
					url4:data[index].url
				})
			}
			if (index === 5) {
				this.setState({
					url5:data[index].url
				})
			}	 
			
		})
	}


	fetchDataUpvotes(index){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response) =>{ return response.json()})
		.then((data)=>{
			if (index === 0) {
				this.setState({
					upvotes0:data[index].upvotes
				})
			}
			if (index === 1) {
				this.setState({
				upvotes1:data[index].upvotes
				})
			}
			if (index === 2) {
				this.setState({
					upvotes2:data[index].upvotes
				})
			}
			if (index === 3) {
				this.setState({
					upvotes3:data[index].upvotes
				})
			}
			if (index === 4) {
				this.setState({
					upvotes4:data[index].upvotes
				})
			}
			if (index === 5) {
				this.setState({
					upvotes5:data[index].upvotes
				})
			}	 
			
		})
	}

	fetchDataAuthor(index){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response) =>{ return response.json()})
		.then((data)=>{
			if (index === 0) {
				this.setState({
					author0:data[index].author
				})
			}
			if (index === 1) {
				this.setState({
				author1:data[index].author
				})
			}
			if (index === 2) {
				this.setState({
					author2:data[index].author
				})
			}
			if (index === 3) {
				this.setState({
					author3:data[index].author
				})
			}
			if (index === 4) {
				this.setState({
					author4:data[index].author
				})
			}
			if (index === 5) {
				this.setState({
					author5:data[index].author
				})
			}	 
			
		})
	}

	fetchDataComments(index){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response) =>{ return response.json()})
		.then((data)=>{
			if (index === 0) {
				this.setState({
					comments0:data[index].comments
				})
			}
			if (index === 1) {
				this.setState({
				comments1:data[index].comments
				})
			}
			if (index === 2) {
				this.setState({
					comment2:data[index].comments
				})
			}
			if (index === 3) {
				this.setState({
					comments3:data[index].comments
				})
			}
			if (index === 4) {
				this.setState({
					comments4:data[index].comments
				})
			}
			if (index === 5) {
				this.setState({
					comments5:data[index].comments
				})
			}	 
			
		})
	}

	fetchDataDateCreated(index){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response) =>{ return response.json()})
		.then((data)=>{
			if (index === 0) {
				this.setState({
					date0:data[index].date_created
				})
			}
			if (index === 1) {
				this.setState({
				date1:data[index].date_created
				})
			}
			if (index === 2) {
				this.setState({
					date2:data[index].date_created
				})
			}
			if (index === 3) {
				this.setState({
					date3:data[index].date_created
				})
			}
			if (index === 4) {
				this.setState({
					date4:data[index].date_created
				})
			}
			if (index === 5) {
				this.setState({
					date5:data[index].date_created
				})
			}	 
			
		})
	}

	fetchDataTimeCreated(index){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response) =>{ return response.json()})
		.then((data)=>{
			if (index === 0) {
				this.setState({
					time0:data[index].time_created
				})
			}
			if (index === 1) {
				this.setState({
				time1:data[index].time_created
				})
			}
			if (index === 2) {
				this.setState({
					time2:data[index].time_created
				})
			}
			if (index === 3) {
				this.setState({
					time3:data[index].time_created
				})
			}
			if (index === 4) {
				this.setState({
					time4:data[index].time_created
				})
			}
			if (index === 5) {
				this.setState({
					time5:data[index].time_created
				})
			}	 
			
		})
	}
	
	onAuthorChange(index){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response)=>{return response.json()})
		.then((data)=>{
			if (index === 0 ) {
				this.setState({
					author0:data[index].author,
				})
			}
			if (index === 1 ) {
				this.setState({
					author1:data[index].author,
				})
			}
			if (index === 2 ) {
				this.setState({
					author2:data[index].author,
				})
			}
			if (index === 3 ) {
				this.setState({
					author3:data[index].author,
				})
			}
			if (index === 4 ) {
				this.setState({
					author4:data[index].author,
				})
			}
			if (index === 5 ) {
				this.setState({
					author5:data[index].author,
				})
			}
		})
	}
	onTitleChange(index){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response)=>{return response.json()})
		.then((data)=>{
			if (index === 0 ) {
				this.setState({
					title0:data[index].title
				})
			}
			if (index === 1 ) {
				this.setState({
					title1:data[index].title
				})
			}
			if (index === 2 ) {
				this.setState({
					title2:data[index].title
				})
			}
			if (index === 3 ) {
				this.setState({
					title3:data[index].title
				})
			}
			if (index === 4 ) {
				this.setState({
					title4:data[index].title
				})
			}
			if (index === 5 ) {
				this.setState({
					title5:data[index].title
				})
			}
		})
	}

	onURLChange(index){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response)=>{return response.json()})
		.then((data)=>{
			if (index === 0 ) {
				this.setState({
					url0:data[index].url
				})
			}
			if (index === 1 ) {
				this.setState({
					url1:data[index].url
				})
			}
			if (index === 2 ) {
				this.setState({
					url2:data[index].url
				})
			}
			if (index === 3 ) {
				this.setState({
					url3:data[index].url
				})
			}
			if (index === 4 ) {
				this.setState({
					url4:data[index].url
				})
			}
			if (index === 5 ) {
				this.setState({
					url5:data[index].url
				})
			}
		})
	}
	onUpvotesChange(){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response)=>{return response.json()})
		.then((data)=>{
			if (index === 0 ) {
				this.setState({
					upvotes0:data[index].upvotes
				})
			}
			if (index === 1 ) {
				this.setState({
					upvotes1:data[index].upvotes
				})
			}
			if (index === 2 ) {
				this.setState({
					upvotes2:data[index].upvotes
				})
			}
			if (index === 3 ) {
				this.setState({
					upvotes3:data[index].upvotes
				})
			}
			if (index === 4 ) {
				this.setState({
					upvotes4:data[index].upvotes
				})
			}
			if (index === 5 ) {
				this.setState({
					upvotes5:data[index].upvotes
				})
			}
		})
	}

	onCommentsChange(){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response)=>{return response.json()})
		.then((data)=>{
			if (index === 0 ) {
				this.setState({
					comments0:data[index].comments
				})
			}
			if (index === 1 ) {
				this.setState({
					comments1:data[index].comments
				})
			}
			if (index === 2 ) {
				this.setState({
					comments2:data[index].comments
				})
			}
			if (index === 3 ) {
				this.setState({
					comments3:data[index].comments
				})
			}
			if (index === 4 ) {
				this.setState({
					comments4:data[index].comments
				})
			}
			if (index === 5 ) {
				this.setState({
					comments5:data[index].comments
				})
			}
		})
	}

	onDateChange(){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response)=>{return response.json()})
		.then((data)=>{
			if (index === 0 ) {
				this.setState({
					date0:data[index].date_created
				})
			}
			if (index === 1 ) {
				this.setState({
					date1:data[index].date_created
				})
			}
			if (index === 2 ) {
				this.setState({
					date2:data[index].date_created
				})
			}
			if (index === 3 ) {
				this.setState({
					date3:data[index].date_created
				})
			}
			if (index === 4 ) {
				this.setState({
					date4:data[index].date_created
				})
			}
			if (index === 5 ) {
				this.setState({
					date5:data[index].date_created
				})
			}
		})
	}

	onTimeChange(){
		fetch("/reddit/api/stocks-top-wallstreetbets?format=json")
		.then((response)=>{return response.json()})
		.then((data)=>{
			if (index === 0 ) {
				this.setState({
					time0:data[index].time_created
				})
			}
			if (index === 1 ) {
				this.setState({
					time1:data[index].time_created
				})
			}
			if (index === 2 ) {
				this.setState({
					time2:data[index].time_created
				})
			}
			if (index === 3 ) {
				this.setState({
					time3:data[index].time_created
				})
			}
			if (index === 4 ) {
				this.setState({
					time4:data[index].time_created
				})
			}
			if (index === 5 ) {
				this.setState({
					time5:data[index].time_created
				})
			}
		})
	}

	mapTenSubmissionToTitle(){
		const array = [0,1,2,3,4,5,6,7,8,9]

		function callback(x, index){
			this.fetchDataTitle(index)
			this.fetchDataUrl(index)
			this.fetchDataUpvotes(index)
			this.fetchDataAuthor(index)
			this.fetchDataComments(index)
			this.fetchDataDateCreated(index)
			this.fetchDataTimeCreated(index)
		}
		array.map(callback ,this)
	}


	handleSubmissionRendering(){
		return(
			<React.Fragment>
				<Submission 
					text={this.state.title0} 
					url={this.state.url0} 
					author={this.state.author0}
					upvotes={this.state.upvotes0}
					comments={this.state.comments0}
					date={this.state.date0}
					time={this.state.time0}
					index={0}
					onTextChange={this.onTitleChange}
					onURLChange={this.onURLChange}
					onAuthorChange={this.onAuthorChange}
					onUpvotesChange={this.onUpvotesChange}
					onCommentsChange={this.onCommentsChange}
					onDateChange={this.onDateChange}
					onTimeChange={this.onTimeChange}
				/>
				<Submission 
					text={this.state.title1} 
					url={this.state.url1} 
					author={this.state.author0}
					upvotes={this.state.upvotes1}
					comments={this.state.comments1}
					date={this.state.date1}
					time={this.state.time1}
					index={1}
					onTextChange={this.onTitleChange}
					onURLChange={this.onURLChange}
					onAuthorChange={this.onAuthorChange}
					onUpvotesChange={this.onUpvotesChange}
					onCommentsChange={this.onCommentsChange}
					onDateChange={this.onDateChange}
					onTimeChange={this.onTimeChange}
				/>
				<Submission 
					text={this.state.title2} 
					url={this.state.url2} 
					author={this.state.author2}
					upvotes={this.state.upvotes2}
					comments={this.state.comments2}
					date={this.state.date2}
					time={this.state.time2}
					index={2}
					onTextChange={this.onTitleChange}
					onURLChange={this.onURLChange}
					onAuthorChange={this.onAuthorChange}
					onUpvotesChange={this.onUpvotesChange}
					onCommentsChange={this.onCommentsChange}
					onDateChange={this.onDateChange}
					onTimeChange={this.onTimeChange}
				/>
				<Submission 
					text={this.state.title3} 
					url={this.state.url3} 
					author={this.state.author3}
					upvotes={this.state.upvotes3}
					comments={this.state.comments3}
					date={this.state.date3}
					time={this.state.time3}
					index={3}
					onTextChange={this.onTitleChange}
					onURLChange={this.onURLChange}
					onAuthorChange={this.onAuthorChange}
					onUpvotesChange={this.onUpvotesChange}
					onCommentsChange={this.onCommentsChange}
					onDateChange={this.onDateChange}
					onTimeChange={this.onTimeChange}
				/>
				<Submission 
					text={this.state.title4} 
					url={this.state.url4} 
					author={this.state.author4}
					upvotes={this.state.upvotes4}
					comments={this.state.comments4}
					date={this.state.date4}
					time={this.state.time4}
					index={4}
					onTextChange={this.onTitleChange}
					onURLChange={this.onURLChange}
					onAuthorChange={this.onAuthorChange}
					onUpvotesChange={this.onUpvotesChange}
					onCommentsChange={this.onCommentsChange}
					onDateChange={this.onDateChange}
					onTimeChange={this.onTimeChange}
				/>
				<Submission 
					text={this.state.title5} 
					url={this.state.url5} 
					author={this.state.author5}
					upvotes={this.state.upvotes5}
					comments={this.state.comments5}
					date={this.state.date5}
					time={this.state.time5}
					index={5}
					onTextChange={this.onTitleChange}
					onURLChange={this.onURLChange}
					onAuthorChange={this.onAuthorChange}
					onUpvotesChange={this.onUpvotesChange}
					onCommentsChange={this.onCommentsChange}
					onDateChange={this.onDateChange}
					onTimeChange={this.onTimeChange}
				/>
			</React.Fragment>
			

		)
	}
	

	render() {
		const props = this.state
		return (
			<div className="demo">
				<Grid 
				container 
				spacing={3}
				>
					{this.handleSubmissionRendering()}		
				</Grid>
			</div>
		);
	}
}

