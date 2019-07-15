import React from "react";
import style from "./Clock.module.css";
import moment from 'moment'

export default class Clock extends React.PureComponent {
  constructor() {
    super();
    this.state = {
      time: moment().format('lll')
    };
  }

  componentDidMount() {
    this.updateClock();
  }

  render() {
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
      time: moment().format('lll')
    });
  };
}
