import React from "react";
import style from "./Clock.module.css";
import moment from 'moment'

export default class Clock extends React.PureComponent {
  constructor() {
    super();
    this.state = {
      time: moment().locale('ru').format('LLL')
    };
  }

  componentDidMount() {
    this.updateClock();
  }

  render() {
    console.log(moment().format('LT'));
    const { time } = this.state;

    return (
      <div className={style.clockBlock}>
        <div className={style.clock}>
          {time}
        </div>
      </div>
    );
  }

  updateClock = () => {
    setInterval(this.tick, 5000);
  };

  tick = () => {
    this.setState({
      time: moment().locale('ru').format('LLL')
    });
  };
}
