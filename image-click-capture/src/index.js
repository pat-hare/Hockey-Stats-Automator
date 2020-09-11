import React from 'react';
import ReactDOM from 'react-dom';
import { CSVLink } from "react-csv";
import HockeyCircle from './HockeyCircle.png'

class Application extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      clicks: []
    }
    this.onMouseClick = this.onMouseClick.bind(this);
  }

  onMouseClick(e) {
    const newArr = this.state.clicks.concat({ x: e.nativeEvent.offsetX, y: e.nativeEvent.offsetY })
    this.setState({
      clicks: newArr
    })
  }
  
  render() {
    return (
      <div className="container">
        <div>
          <img
            onClick={this.onMouseClick}
            width="1373"
            height="774"
            src={HockeyCircle} />
        </div>
        <ul>
          {this.state.clicks.map((item, index) => {
            return <li key={index}>x: {item.x}, y: {item.y}, shot taker: , type of shot: </li>
          })}
        </ul>
        <CSVLink filename='shot-map.csv' data={this.state.clicks}>Download me</CSVLink>
      </div>
    );
  }
}

ReactDOM.render(<Application />, document.getElementById('app'));
