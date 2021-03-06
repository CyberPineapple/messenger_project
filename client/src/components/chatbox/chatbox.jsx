import React from 'react';
import { connect } from 'react-redux';
import style from './chatbox.module.css';
import { bindActionCreators } from "redux";
import { setMessage, removeMessage } from "../../actions/actions.js";
import { socket } from '../../websockets/websocket'


class Chatbox extends React.Component{

    render(){
        const { messagesList } = this.props;
        let messages = [];
        if (messagesList.length !== 0){
            messages = messagesList.map((value, id)=><div key={id} className={style.message}>
                <div className={style.message_user}>{value.user}</div>
                <div className={style.message_text}>{value.text}</div>
                <div className={style.message_time}>{value.date}</div>
            </div>)
        }
        return(
            <div className={style.block}>
                <div className={style.output}>
                    {messages}
                </div>
                <div className={style.input}>
                <textarea onChange={(event)=> this.onChangeMessage(event.target.value)} value={this.props.message}  onKeyPress={(e) => this.pressEnter(e)}></textarea>
                <div className={style.button} onClick={()=>this.sendMessage()}>Отправить</div>
                </div>
          </div>
        )
    }

    sendMessage = () =>{
        if (this.props.message !== '' && this.props.activeChat !== ''){
            let data = {
                Type: 'chat',
                Command: 'message',
                Text: this.props.message,
            }
            data = JSON.stringify(data);
            socket.send(data);
            this.props.removeMessage();
        }
    }

    pressEnter = (e) =>{
        if (e.key === 'Enter'){
            this.sendMessage();
        }
    }

    onChangeMessage = (value) =>{
        if (value !== '\n')
        this.props.setMessage(value);
    }
}

const mapStateToProps = store => {
    return {
        message: store.message,
        login: store.login,
        messagesList: store.messagesList,
        activeChat: store.activeChat
    }
}

const mapDispatchToProps = dispatch =>{
    return bindActionCreators({setMessage: setMessage, removeMessage: removeMessage}, dispatch);
}



export default connect(mapStateToProps, mapDispatchToProps)(Chatbox);