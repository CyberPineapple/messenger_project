import React, { PureComponent } from "react";
import style from "./Message.module.css";

export default class Message extends PureComponent {
  handleClick = () => {
    const { reply, id, user, text } = this.props;
    reply({
      id: id,
      user: user,
      text: text
    });
  };

  render() {
    const { text, date, image, user, isChecked, replyMessage } = this.props;

    return (
      <div
        className={isChecked ? style.checked : style.message}
        onClick={this.handleClick}
      >
        <div className={style.message_user}>{user}</div>
        {text && <div className={style.message_text}>{text}</div>}
        <div className={style.message_time}>{date}</div>
        {image && (
          <img
            src={"https://host-94-103-84-32.hosted-by-vdsina.ru" + image}
            className={style.message_image}
            alt="images"
          />
        )}
        {replyMessage && (
          <div className={style.replyBlock}>
            <div className={style.replyUser}>{replyMessage.user}</div>
            <div className={style.replyText}>{replyMessage.text}</div>
          </div>
        )}
      </div>
    );
  }
}
