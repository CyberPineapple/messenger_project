import React from "react";
import style from "./authentificationPage.module.css";
import { Animated } from "react-animated-css";
import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import { setPage, setLogin, setPassword, removeLogin, removePassword } from "../../actions/actions.js";

class AuthentificationPage extends React.Component {
  render() {
    return (
      <Animated
        animationIn="flipInX"
        animationInDuration={1000}
        isVisible={true}
      >
        <div className={style.page}>
          <div className={style.layout}>
            <p className={style.title}>Добро пожаловать</p>
            <p>Логин</p>
            <input
              type="text"
              className={style.input}
              onChange={(event) => this.props.setLogin(event.target.value)}
              onClick={()=>this.props.removeLogin()}
              value={this.props.login}
            />
            <p>Пароль</p>
            <input
              type="password"
              className={style.input}
              onChange={(event) => this.props.setPassword(event.target.value)}
              value={this.props.password}
              onClick={()=>this.props.removePassword()}
            />
            <div
              className={style.button}
              onClick={() => this.goToPage()}
            >
              Войти
            </div>
            <div
              className={style.button}
              onClick={() => console.log('Хочу зарегаться')}
            >
              Регистрация
            </div>
          </div>
        </div>
      </Animated>
    );
  }

  goToPage = () =>{
    if (this.props.login !== '' && this.props.password !== ''){
      this.props.setPage("main")
    }

  }
}


const mapStateToProps = store =>{
  return {
    login: store.login,
    password: store.password
  }
}

const mapDispatchToProps = dispatch => {
  return bindActionCreators({ setPage: setPage, setLogin: setLogin, setPassword: setPassword, removeLogin: removeLogin, removePassword: removePassword }, dispatch);
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(AuthentificationPage);