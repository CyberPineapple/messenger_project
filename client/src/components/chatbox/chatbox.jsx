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
                <textarea onChange={(event)=> this.props.setMessage(event.target.value)} value={this.props.message}></textarea>
                <div className={style.button} onClick={()=>this.sendMessage()}>Отправить</div>
                </div>
          </div>
        )
    }

    sendMessage = () =>{
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
