import React, { PureComponent } from "react";
import styles from "./ChatInput.module.css";
import Compress from "compress.js";
import sendMessage from "../../../../websockets/websocket";

export default class ChatInput extends PureComponent {
  state = {
    text: ""
  };

  loadImage = e => {
    const { setImage } = this.props;
    let file = [...e.target.files];
    const compress = new Compress();
    if (!file.length) {
      return null;
    }
    compress
      .compress(file, {
        quality: 0.75,
        maxWidth: 1920,
        maxHeight: 1920
      })
      .then(data => {
        setImage(data[0].prefix + data[0].data);
      });
  };

  pressEnter = e => {
    if (e.key === "Enter") {
      this.send();
    }
  };

  changeTextInput = e => {
    let value = e.target.value;
    value = value.replace("  ", " ");
    this.setState({
      text: value
    });
  };

  send = () => {
    const { text } = this.state;
    const { image, setImage, replyMessage, reply } = this.props;
    if ((text !== "" && text[text.length - 1] !== " ") || image !== "") {
      let data = {
        Type: "chat",
        Command: "message"
      };
      if (text) {
        data.Text = text;
      }
      if (image) {
        data.Image = image;
      }
      if (replyMessage) {
        data.Reply = { user: replyMessage.user, text: replyMessage.text };
      }
      sendMessage(JSON.stringify(data));
      setImage("");
      reply('');
      this.setState({
        text: ""
      });
    }
  };

  render() {
    const { text } = this.state;
    const { image } = this.props;

    return (
      <div className={styles.block}>
        <div className={styles.imagesBlock}>
          <img className={styles.image} src={image} alt="" />
          <label htmlFor="file" className={styles.inputFile}>
            <input
              type="file"
              accept="image/jpeg,image/png"
              style={{ display: "none" }}
              id="file"
              onChange={this.loadImage}
            />
          </label>
        </div>
        <input
          className={styles.inputText}
          type="text"
          onChange={this.changeTextInput}
          value={text}
          onKeyPress={this.pressEnter}
        />
        <button className={styles.button} onClick={this.send}>
          Отправить
        </button>
      </div>
    );
  }
}
