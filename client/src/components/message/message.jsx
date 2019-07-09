import React from "react";
import style from "./Message.module.css";

export default class Message extends React.Component {
  render() {
    const { data } = this.props;
    let image;
    let text;
    if (data.image) {
      image = (
        <img
          src={"https://host-94-103-84-32.hosted-by-vdsina.ru" + data.image}
          className={style.message_image}
          alt="images"
        />
      );
    }
    if (data.text){
      text = (<div className={style.message_text}>{data.text}</div>);
    }

    return (
      <div className={style.message}>
        <div className={style.message_user}>{data.user}</div>
        {text}
        <div className={style.message_time}>{data.date}</div>
        {image}
      </div>
    );
  }
}
