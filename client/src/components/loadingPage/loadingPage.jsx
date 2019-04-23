import React from 'react'
import style from './loadingPage.module.css'

const LoadingPage = () => {
    return (
        <div className={style.block}>
            <p className={style.text}>Connect to server</p>
            <div className={style.line1}></div>
            <div className={style.line2}></div>
            <div className={style.line3}></div>
        </div>
    )
}

export default LoadingPage;