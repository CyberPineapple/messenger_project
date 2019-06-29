import React from "react";
import { connect } from "react-redux";
import style from "./chatbox.module.css";
import { bindActionCreators } from "redux";
import { setMessage, removeMessage, clearImages, addImage } from "../../actions/actions.js";
import { socket } from "../../websockets/websocket";
import ChatOutput from "../chatOutput/chatOutput";

class Chatbox extends React.Component {
  render() {
    let chat = null;
    let pictures = <div className={style.image} style={{backgroundImage: `url(${this.props.images})`}}></div>;
    if (this.props.renderChatOutput) {
      chat = <ChatOutput />;
    } else {
      chat = null;
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
                style={{display: 'none'}}
                id='file'
                onChange={(e) => this.loadImage(e)}
              />
            </label>
            <div className={style.pictures}>
              {pictures}
            </div>
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
    if (this.props.activeChat !== "" && (this.props.message !== '' || this.props.images !== '')) {

      let data = {
        Type: "chat",
        Command: "message",
      };
      if (this.props.message !== ''){
        data.Text = this.props.message;
      }
      if (this.props.images !== ''){
        data.Image = this.props.images
      }
      data = JSON.stringify(data);
      console.log(data);
      socket.send(data);
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

  loadImage = (e) =>{
    let reader = new FileReader();
    let file = e.target.files[0];
    reader.onload = () =>{
      this.props.addImage(reader.result);
    }
    reader.readAsDataURL(file);
  }
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
    { setMessage: setMessage, removeMessage: removeMessage, clearImages: clearImages, addImage: addImage },
    dispatch
  );
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Chatbox);
