import React from 'react';
import { connect } from 'react-redux';
import style from './chatbox.module.css';
import { bindActionCreators } from "redux";
import { setMessage, removeMessage } from "../../actions/actions.js";
import { socket } from '../../websockets/websocket'


class Chatbox extends React.Component{

    render(){
        const { messagesList } = this.props;
        const messages = messagesList.map((value)=><li>{value}</li>)
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
        if (this.props.message !== ''){
            let data = {
                Type: 'message',
                Sender: this.props.login,
                Text: this.props.message
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
        messagesList: store.messagesList
    }
}

const mapDispatchToProps = dispatch =>{
    return bindActionCreators({setMessage: setMessage, removeMessage: removeMessage}, dispatch);
}



export default connect(mapStateToProps, mapDispatchToProps)(Chatbox);
