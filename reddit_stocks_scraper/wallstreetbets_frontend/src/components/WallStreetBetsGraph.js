import { Bar, Pie } from 'react-chartjs-2';
import React, {useEffect, useState} from 'react';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import CardActionArea from '@material-ui/core/CardActionArea';
import Container from '@material-ui/core/Container';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from "@material-ui/core/InputLabel"
import Input from "@material-ui/core/Input"
import FormHelperText from "@material-ui/core/FormHelperText"
import Select from "@material-ui/core/Select"
import MenuItem from "@material-ui/core/MenuItem"





const formStyle = {
  "position":'relative',
  "left":"20%",
  "top":5
}

const settingsSize = {
  "width":(0.34 * window.innerWidth),
  "height":(0.40 * window.innerHeight)
}



// PieChart Component
class PieChart extends React.Component{
  constructor(props) {
    super(props);
    this.stockState = {}
    this.state = {
      data :{
        labels: ['Loading'],
        datasets: [
        {
          label: '# of Votes',
          data: null,
          backgroundColor: null,
          borderColor: null,
          borderWidth: 1,
        },
        ],
      },
      stocksInfo:{},
    }
    // CALL METHOD ZONE
    this.handleFetchOverallStockData()
    // BIND ZONE
    this.test = this.test.bind(this)
  }
  arrayIncludes(arrayOne, arrayTwo){
    let indicator = false;

    let count = 0;
    for( let i = 0; i < arrayOne.length; i++){
      if(arrayOne[i] === arrayTwo[i]){
        if (count === 2){
          indicator = true;
          return indicator
        }
        else {
           count = count + 1;
          continue;
        }         
      }
      else{
        return indicator;
      }
    }
  }

  arrayIsPresentInObject(obj, array){
    // loop over the values(arra)
    let objValues = Object.values(obj)
    for(let i = 0; i < objValues.length; i++){
      if(this.arrayIncludes(array,objValues[i])){
        return true;
      }
    } 

    return false;

  }

  handleRandomColorPicker(labelArray){
    let objectLabelRGB = {}
    function rgbColorPicker(){
      let rValue = Math.floor(Math.random() * 255);
      let gValue = Math.floor(Math.random() * 255);
      let bValye = Math.floor(Math.random() * 255);
      let rgbArray = [rValue, gValue ,bValye]
      return rgbArray;
    }
    for(let i = 0; i < labelArray.length; i++){
      let rgbArray= rgbColorPicker();
      while (true) {
        if(!this.arrayIsPresentInObject(objectLabelRGB, rgbArray)){
          // if rgb array value is not already present in ObjectLabelRGB, then break out of the loop
          break;
        }
        else{
          rgbArray= rgbColorPicker();
          continue;
        }
      }
      objectLabelRGB[labelArray[i]] = rgbArray
    }
    return objectLabelRGB;
  }

  handeRGBParsing(labelRgbObject){
    let values = Object.values(labelRgbObject)
    let finalArray = []
    for(let i = 0; i < values.length; i++ ){
      finalArray.push(`rgba(${values[i][0]}, ${values[i][1]}, ${values[i][2]}, 1)`)
    }
    return finalArray;
  }
  handeRGBParsingBorder(labelRgbObject){
    let values = Object.values(labelRgbObject)
    let finalArray = []
    for(let i = 0; i < values.length; i++ ){
      finalArray.push(`rgba(${values[i][0]}, ${values[i][1]}, ${values[i][2]}, 1`)
    }
  }

  handleFetchOverallStockData(){
    fetch("/reddit/api/stocks-overall-view-wallstreetbets")
    .then((response) => {return response.json()})
    .then((data) =>{
      console.log(data.length)
      for(let i = 0; i < data.length; i++){
        // if a stock_ticker is present in the state already, then just update the stock mentions if not do nothing
        this.state.stocksInfo[`${data[i].stock_ticker}`] = data[i].stock_mentions
      }
      this.stockState['stockTickerData'] = Object.keys(this.state.stocksInfo); // type array
      this.stockState['stockMentionsData'] = Object.values(this.state.stocksInfo);// type array
      // console.log(this.stockState.stockMentionsData)
      this.setState({
        data :{
        labels: this.stockState.stockTickerData,
        datasets: [
        {
          label: '# of Votes',
          data: this.stockState.stockMentionsData,
          backgroundColor: this.handeRGBParsing(this.handleRandomColorPicker(this.stockState.stockTickerData)),
          borderColor: this.handeRGBParsingBorder(this.handleRandomColorPicker(this.stockState.stockTickerData)),
          borderWidth: 1,
        },
        ],
      },
      })
    });
  }

  test(e){
    console.log(this.state.width60thPercentile)
  }

  widthResponsiveness(){
    if(window.innerWidth <= 1146 ){
        return(
            0.32 * window.innerWidth
        )
    }
    else{
      return (
        0.57 * window.innerWidth
      )
    }
  }

  
  render() {
    return (
      <div className="piegraph" style={{
        left:(this.widthResponsiveness()) 
      }}>
        <div>
          <Pie data={this.state.data} width={this.props.width} height={this.props.height}/>
        </div>
        <button onClick={this.test} > Test </button>
      </div>
    );
  }

}

class Settings extends React.Component{
  constructor(props){
    super(props)
    this.state = {
      "data_representation" : "piechart"
    }
  }

  render(){
    return(
      <React.Fragment>
        <div className="settings" style={{"width":settingsSize.width, 'height':settingsSize.height}}>
          <div style={formStyle}>
            <FormControl style={{"width":"50%"}}
            variant="filled"
            >
              <InputLabel id="data-selector"> Data Representation</InputLabel>
              <Select 
              labelId="data-selector"
              value={this.state.data_representation}
              onChange={
                (e) => {
                  this.setState({
                    "data_representation":e.target.value
                  })
                }
              }
              >
                <MenuItem value={"piechart"}> Pie Chart </MenuItem>
                <MenuItem value={"bargraph"}> Bar Graph </MenuItem>
                <MenuItem value={"tabular"}> Tabular Form </MenuItem>
                <MenuItem value={3}> Java </MenuItem>
                <MenuItem value={5}> Node </MenuItem>
              </Select>
            </FormControl>
            </div>
        </div>
      </React.Fragment>
    )
  }
}

export default class WallStreetBetsGraph extends React.Component {
    constructor(props){
      super(props)
    }

    render(){
      return(
        <React.Fragment>
          <PieChart width={500} height={500}/>
          <Settings/>
        </React.Fragment>
      )
    }
}




    
