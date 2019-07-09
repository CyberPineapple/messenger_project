import React from "react";
import { connect } from "react-redux";
import style from "./Chatbox.module.css";
import { bindActionCreators } from "redux";
import {
  setMessage,
  removeMessage,
  clearImages,
  addImage
} from "../../actions/actions.js";
import sendMessage from "../../websockets/websocket";
import ChatOutput from "../ChatOutput/ChatOutput";
import Compress from "compress.js";

class Chatbox extends React.Component {
  render() {
    let chat = null;
    let pictures = (
      <div
        className={style.image}
        style={{ backgroundImage: `url(${this.props.images})` }}
      />
    );
    if (this.props.renderChatOutput) {
      chat = <ChatOutput />;
    }

    return (
      <div className={style.block}>
        <div className={style.chat}>{chat}</div>
        <div className={style.input}>
          <div className={style.imagesBlock}>
            <label htmlFor="file" className={style.button_file}>
              <input
                type="file"
                accept="image/jpeg,image/png"
                style={{ display: "none" }}
                id="file"
                onChange={e => this.loadImage(e)}
              />
            </label>
            <div className={style.pictures}>{pictures}</div>
          </div>
          <textarea
            onChange={event => this.onChangeMessage(event.target.value)}
            value={this.props.message}
            onKeyPress={e => this.pressEnter(e)}
          />
          <div className={style.button} onClick={() => this.sendMessage()}>
            Отправить
          </div>
        </div>
      </div>
    );
  }

  sendMessage = () => {
    if (
      this.props.activeChat !== "" &&
      (this.props.message !== "" || this.props.images !== "")
    ) {
      let data = {
        Type: "chat",
        Command: "message"
      };
      if (this.props.message !== "") {
        data.Text = this.props.message;
      }
      if (this.props.images !== "") {
        data.Image = this.props.images;
      }
      data = JSON.stringify(data);
      console.log(data);
      sendMessage(data);
      this.props.removeMessage();
      this.props.clearImages();
    }
  };

  pressEnter = e => {
    if (e.key === "Enter") {
      this.sendMessage();
    }
  };

  onChangeMessage = value => {
    if (value !== "\n") this.props.setMessage(value);
  };

  loadImage = e => {
    let file = [...e.target.files];
    console.log(file[0].size);
    const compress = new Compress();

    compress.compress(file, {
      quality: 0.75,
      maxWidth: 1920,
      maxHeight: 1920
    }).then((data) => {
      console.log(data[0]);
      this.props.addImage(data[0].prefix + data[0].data);
    });
  };
}

const mapStateToProps = store => {
  return {
    message: store.message,
    login: store.login,
    activeChat: store.activeChat,
    renderChatOutput: store.renderChatOutput,
    images: store.images
  };
};

const mapDispatchToProps = dispatch => {
  return bindActionCreators(
    {
      setMessage: setMessage,
      removeMessage: removeMessage,
      clearImages: clearImages,
      addImage: addImage
    },
    dispatch
  );
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Chatbox);
