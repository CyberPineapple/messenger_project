import React, { PureComponent } from "react";
import styles from "./ChatMenu.module.css";
import PropTypes from "prop-types";
import sendMessage from "../../../websockets/websocket";

export default class ChatMenu extends PureComponent {
  static propTypes = {
    usersOnline: PropTypes.array
  };
  state = {
    isView: false
  };

  clickButton = () => {
    const { isView } = this.state;
    this.setState({
      isView: !isView
    });
  };

  clearChat = () => {
    const data = {
      Type: "chat",
      Command: "purge"
    };
    sendMessage(JSON.stringify(data));
  };

  render() {
    const { isView } = this.state;
    const { usersOnline } = this.props;
    return (
      <div className={isView ? styles.blockView : styles.blockHide}>
        <button className={styles.button} onClick={this.clickButton}>
          <div className={styles.burger}>
            <div className={isView ? styles.line1Active : styles.line1} />
            <div className={isView ? styles.line2Active : styles.line2} />
            <div className={isView ? styles.line3Active : styles.line3} />
          </div>
        </button>
        <div className={styles.menu}>
          <p className={styles.title}>Пользователи в чате</p>
          <ul className={styles.usersList}>
            {usersOnline.map(v => (
              <li className={styles.user} key={v}>{v}</li>
            ))}
          </ul>
          <button className={styles.buttonMenu} onClick={this.clearChat}>Очистить чат</button>
          {/* <button className={styles.buttonMenu}>Удалить чат</button> */}
        </div>
      </div>
    );
  }
}
