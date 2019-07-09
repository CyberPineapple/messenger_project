import React from "react";
import style from "./Clock.module.css";

export default class Clock extends React.Component {
  constructor() {
    super();
    this.state = {
      hour: '',
      minute: '',
      flash: '\u205F'
    };
  }

  componentDidMount() {
    this.updateClock();
  }

  render() {
    const { hour, minute, flash } = this.state;

    return (
      <div className={style.clockBlock}>
        <div className={style.clock}>
          {hour}
          {flash}
          {minute}
        </div>
      </div>
    );
  }

  updateClock = () => {
    setInterval(this.tick, 1000);
  };

  tick = () => {
    let date = new Date();
    let flash;
    let minuts = date.getMinutes();
    if (minuts < 10){
      minuts = "0" + minuts;
    }
    if (this.state.flash === ":") {
      flash = "\u205F";
    } else if (this.state.flash === "\u205F") {
      flash = ":";
    }
    this.setState({
      hour: date.getHours(),
      minute: minuts,
      flash: flash
    });
  };
}
