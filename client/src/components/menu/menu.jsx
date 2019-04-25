import React from 'react';
import { connect } from 'react-redux';
import style from './menu.module.css';

class Menu extends React.Component{

    render(){
        return(
          <div className={style.menu}>
            <div className={style.menu_image}></div>
            <p>{this.props.login}</p>
          </div>
        )
    }
}

export default connect(null, null)(Menu);