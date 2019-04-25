import React from 'react'
import connect from 'react-redux'
import style from './chatbox.module.css'


export default class Chatbox extends React.Component{

    render(){

        return(
            <div className={style.block}>
                <div className={style.output}>
                </div>
                <div className={style.input}>
                <textarea></textarea>
                <div className={style.button}>Отправить</div>
                </div>
          </div>
        )
    }
}
