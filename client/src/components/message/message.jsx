import React from 'react';
import style from './message.module.css';

export default class Message extends React.Component{

  render(){
    const { data } = this.props;
    let image;
    if (data.image){
      image = <img src={data.image} className={style.message_image} alt='images'></img>
    }

  return (
    <div className={style.message}>
      <div className={style.message_user}>{data.user}</div>
      <div className={style.message_text}>{data.text}</div>
      <div className={style.message_time}>{data.date}</div>
      {image}
    </div>
  )
  }
}