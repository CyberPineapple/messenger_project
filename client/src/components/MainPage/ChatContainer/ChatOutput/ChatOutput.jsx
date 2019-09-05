import React, { Component } from "react";
import styles from "./ChatOutput.module.css";
import sendMessage from "../../../../websockets/websocket";
import Message from "./Message/Message";

export default class ChatOutput extends Component {
  render() {
    const { messagesList, reply, replyMessage } = this.props;
    let messages = [];
    if (messagesList.length !== 0) {
      messages = messagesList.map((value, id) => (
        <Message
          text={value.text}
          image={value.image}
          user={value.user}
          date={value.date}
          id={value.id}
          key={id}
          reply={reply}
          replyMessage={value.reply}
          isChecked={replyMessage === value.id}
        />
      ));
    } else {
      messages = (
        <div className={styles.loading}>
          <div className={styles.line1} />
          <div className={styles.line2} />
          <div className={styles.line3} />
        </div>
      );
    }
    return (
      <div className={styles.block}>
        <div className={styles.chatName}>{this.props.activeChat}</div>
        <div className={styles.messagesList} onScroll={this.scrollChat}>
          {messages}
        </div>
      </div>
    );
  }

  componentDidUpdate() {
    let el = document.querySelector("." + styles.messagesList);
    el.scrollTop = el.scrollHeight;
  }

  componentDidMount() {
    let el = document.querySelector("." + styles.messagesList);
    el.scrollTop = el.scrollHeight;
  }

  scrollChat = value => {
    if (value.target.scrollTop === 0) {
      let data = {
        Type: "chat",
        Command: "earlier"
      };
      sendMessage(JSON.stringify(data));
      value.target.scrollTop = 10;
    }
  };
}
