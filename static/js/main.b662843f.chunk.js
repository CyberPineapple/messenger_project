(window.webpackJsonp=window.webpackJsonp||[]).push([[0],[,,,,,,function(e,t,a){e.exports={block:"MainMenu_block__znKXj",menu:"MainMenu_menu__3HzX7",blockView:"MainMenu_blockView__2TtZU MainMenu_block__znKXj",blockHide:"MainMenu_blockHide__1iAwk MainMenu_block__znKXj",button:"MainMenu_button__13Dhf",burger:"MainMenu_burger__1mICN",line:"MainMenu_line__2btEy",line1:"MainMenu_line1__128rK MainMenu_line__2btEy",line2:"MainMenu_line2__3Kv9e MainMenu_line__2btEy",line3:"MainMenu_line3__2rLb3 MainMenu_line__2btEy",line1Active:"MainMenu_line1Active__12n3R MainMenu_line__2btEy",line2Active:"MainMenu_line2Active__TSKxu MainMenu_line__2btEy",line3Active:"MainMenu_line3Active__n7ptN MainMenu_line__2btEy",menu_image:"MainMenu_menu_image__3TAsp",menu_login:"MainMenu_menu_login__2r9_S",menu_chat:"MainMenu_menu_chat__1K3x8",menu_chat_list:"MainMenu_menu_chat_list__30Ogi",input:"MainMenu_input__2F7pE"}},,,function(e,t,a){e.exports={block:"ChatMenu_block__1ApSi",menu:"ChatMenu_menu__3abvv",blockView:"ChatMenu_blockView__1eYR1 ChatMenu_block__1ApSi",blockHide:"ChatMenu_blockHide__2bq5n ChatMenu_block__1ApSi",button:"ChatMenu_button__l8ioH",burger:"ChatMenu_burger__16Hm9",line:"ChatMenu_line__2gtxU",line1:"ChatMenu_line1__2qYgm ChatMenu_line__2gtxU",line2:"ChatMenu_line2__WvR3e ChatMenu_line__2gtxU",line3:"ChatMenu_line3__23xtC ChatMenu_line__2gtxU",line1Active:"ChatMenu_line1Active__1g0l2 ChatMenu_line__2gtxU",line2Active:"ChatMenu_line2Active__1yw1n ChatMenu_line__2gtxU",line3Active:"ChatMenu_line3Active__g828U ChatMenu_line__2gtxU",buttonMenu:"ChatMenu_buttonMenu__1gdAJ",usersList:"ChatMenu_usersList__3Kyk5",title:"ChatMenu_title__2vTTy",user:"ChatMenu_user__ypJxY"}},function(e,t,a){e.exports={block:"ChatOutput_block__1zW8F",chatName:"ChatOutput_chatName___5jSq",messagesList:"ChatOutput_messagesList__12vfV",loading:"ChatOutput_loading__1c9cW",line1:"ChatOutput_line1__2qFNf",spin:"ChatOutput_spin__27p64",line2:"ChatOutput_line2__24QBd",line3:"ChatOutput_line3__2Kqr6"}},function(e,t,a){e.exports={message:"Message_message__2ahwu",newMessage:"Message_newMessage__1ycW-",checked:"Message_checked__3suVw Message_message__2ahwu",message_user:"Message_message_user__2vjCC",message_text:"Message_message_text__2eY4V",message_time:"Message_message_time__mHr8V",message_image:"Message_message_image__2P9xB",replyBlock:"Message_replyBlock__2A_xW",replyUser:"Message_replyUser__1QTcs",replyText:"Message_replyText__2XQ4p"}},,,function(e,t,a){e.exports={page:"AuthentificationPage_page__3py-N",layout:"AuthentificationPage_layout__2fDmh",button:"AuthentificationPage_button__1jip2",input:"AuthentificationPage_input__2xKRO",title:"AuthentificationPage_title__3sOMz"}},,function(e,t,a){e.exports={block:"ChatInput_block__Pr7kD",inputText:"ChatInput_inputText__34Cv9",button:"ChatInput_button__1XZ32",inputFile:"ChatInput_inputFile__BuedB",imagesBlock:"ChatInput_imagesBlock__2R13a",image:"ChatInput_image__3H3Xa"}},function(e,t,a){e.exports={block:"LoadingPage_block__3sfph",text:"LoadingPage_text__1tk9S",line1:"LoadingPage_line1__1rhxD",spin:"LoadingPage_spin__1aUPu",line2:"LoadingPage_line2__3enc5",line3:"LoadingPage_line3__2slWX"}},,,,,,function(e,t,a){e.exports={menu_chat_list_item:"ChatItem_menu_chat_list_item__2oULd"}},function(e,t,a){e.exports={clockBLock:"Clock_clockBLock__45FGV",clock:"Clock_clock__2ufjn"}},,,,,,function(e,t,a){e.exports=a.p+"static/media/new_message.8b29b843.mp3"},function(e,t,a){e.exports={layout:"MainPage_layout__19sGD"}},function(e,t,a){e.exports={block:"ChatContainer_block__1BRnS"}},,function(e,t,a){e.exports=a(45)},,,,,function(e,t,a){},,,,,,function(e,t,a){"use strict";a.r(t);var n=a(0),s=a.n(n),i=a(19),r=a.n(i),c=(a(39),a(1)),l=a(2),o=a(4),u=a(3),m=a(5),_=a(8),p=a(14),h=a.n(p),d=a(12),g=a(18),b=a(7),v={user:{login:"",password:""},usersOnline:[],page:"loading",message:"",messagesList:[],chatList:[],chatName:"",chatPassword:"",activeChat:"",renderChatOutput:!0,image:"",replyMessage:""};var C=a(29),E=Object(d.createStore)(function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:v,t=arguments.length>1?arguments[1]:void 0,a=t.type,n=t.payload;switch(a){case"SET_PAGE":return Object(b.a)({},e,{page:n});case"SET_LOGIN":return Object(b.a)({},e,{user:{login:n,password:e.user.password}});case"SET_PASSWORD":return Object(b.a)({},e,{user:{login:e.user.login,password:n}});case"SET_ONLINE_USERS":return Object(b.a)({},e,{usersOnline:n});case"SET_MESSAGE":return Object(b.a)({},e,{message:n});case"SET_MESSAGES_LIST":return Object(b.a)({},e,{messagesList:e.messagesList.concat(n)});case"REMOVE_MESSAGE":return Object(b.a)({},e,{message:""});case"SET_CHAT_LIST":return Object(b.a)({},e,{chatList:n});case"ADD_CHAT_NAME":return Object(b.a)({},e,{chatName:n});case"REMOVE_CHAT_NAME":return Object(b.a)({},e,{chatName:""});case"ADD_CHAT_PASSWORD":return Object(b.a)({},e,{chatPassword:n});case"REMOVE_CHAT_PASSWORD":return Object(b.a)({},e,{chatPassword:""});case"ACTIVE_CHAT":return Object(b.a)({},e,{activeChat:n});case"REMOVE_MESSAGES_LIST":return Object(b.a)({},e,{messagesList:[]});case"RENDER_CHAT_OUTPUT":return Object(b.a)({},e,{renderChatOutput:n});case"EARLIER_MESSAGES":return Object(b.a)({},e,{messagesList:[].concat(Object(g.a)(n),Object(g.a)(e.messagesList))});case"SET_IMAGE":return Object(b.a)({},e,{image:n});case"REPLY_MESSAGE":return Object(b.a)({},e,{replyMessage:n});default:return e}},Object(C.composeWithDevTools)()),f=function(e){return{type:"SET_PAGE",payload:e}},y=function(e){return{type:"SET_MESSAGES_LIST",payload:e}},O=function(){return{type:"REMOVE_MESSAGES_LIST"}},M=function(e){return{type:"ADD_CHAT_NAME",payload:e}},k=function(){return{type:"REMOVE_CHAT_NAME"}},j=function(e){return{type:"ADD_CHAT_PASSWORD",payload:e}},N=function(){return{type:"REMOVE_CHAT_PASSWORD"}},S=function(e){return{type:"ACTIVE_CHAT",payload:e}},w=function(e){return{type:"RENDER_CHAT_OUTPUT",payload:e}},A=function(e){return{type:"REPLY_MESSAGE",payload:e}},P=a(30),T=a.n(P),L=new WebSocket("wss://host-94-103-84-32.hosted-by-vdsina.ru:443/");L.onopen=function(){E.dispatch(f("authentification"))},L.onclose=function(){console.log("disconnect"),E.dispatch(f("loading"))},L.onmessage=function(e){var t=JSON.parse(e.data);if(console.log(t),null!==t)switch(t.Type){case"account":if("success"===t.Status){E.dispatch(f("main"));var a={Type:"chat",Command:"choice",Chat:"general"};a=JSON.stringify(a),x(a),a={Type:"chat",Command:"connected"},a=JSON.stringify(a),x(a),E.dispatch(w(!1))}else"error"===t.Status&&console.log("\u041e\u0448\u0438\u0431\u043a\u0430 \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438");break;case"registration":console.log("\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f");break;case"chat":if("list"===t.Command&&E.dispatch({type:"SET_CHAT_LIST",payload:t.Chats}),"choice"===t.Command&&(E.dispatch(S(t.Chat)),E.dispatch(y(t.Messages)),E.dispatch(w(!0))),"message"===t.Command){if(t.Message.user!==E.getState().user.login){var n=new Audio;n.src=T.a,n.play()}E.dispatch(y(t.Message))}"earlier"===t.Command&&0!==t.Messages.length&&E.dispatch(function(e){return{type:"EARLIER_MESSAGES",payload:e}}(t.Messages)),"connected"===t.Command&&E.dispatch(function(e){return{type:"SET_ONLINE_USERS",payload:e}}(t.Online));break;default:console.log(t)}},L.onerror=function(e){console.log("error: ",e)};var x=function(e){console.log(e),L.send(e)},I=x,R=function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,s=new Array(n),i=0;i<n;i++)s[i]=arguments[i];return(a=Object(o.a)(this,(e=Object(u.a)(t)).call.apply(e,[this].concat(s)))).handleChangeLoginField=function(e){a.props.setLogin(e.target.value)},a.handleClickLoginField=function(){a.props.setLogin("")},a.handleCLickPasswordField=function(){a.props.setPassword("")},a.handleChangePasswordField=function(e){a.props.setPassword(e.target.value)},a.authorization=function(){var e=a.props,t=e.login,n=e.password;if(""!==t&&""!==n){var s={Type:"account",Command:"login",Login:t,Password:n};s=JSON.stringify(s),I(s)}},a.registration=function(){var e=a.props,t=e.login,n=e.password;if(""!==t&&""!==n){var s={Type:"account",Command:"registration",Login:t,Password:n};s=JSON.stringify(s),I(s)}},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this.props,t=e.login,a=e.password;return s.a.createElement("div",{className:h.a.page},s.a.createElement("div",{className:h.a.layout},s.a.createElement("p",{className:h.a.title},"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c"),s.a.createElement("p",null,"\u041b\u043e\u0433\u0438\u043d"),s.a.createElement("input",{type:"text",name:"login",autoComplete:"on",className:h.a.input,onChange:this.handleChangeLoginField,onClick:this.handleClickLoginField,value:t,maxLength:20,placeholder:"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d"}),s.a.createElement("p",null,"\u041f\u0430\u0440\u043e\u043b\u044c"),s.a.createElement("input",{placeholder:"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c",type:"password",name:"password",autoComplete:"on",className:h.a.input,onChange:this.handleChangePasswordField,value:a,onClick:this.handleCLickPasswordField,maxLength:30}),s.a.createElement("button",{className:h.a.button,onClick:this.authorization},"\u0412\u043e\u0439\u0442\u0438"),s.a.createElement("button",{className:h.a.button,onClick:this.registration},"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f")))}}]),t}(n.PureComponent),H=function(e){function t(){return Object(c.a)(this,t),Object(o.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this.props,t=e.login,a=e.password,n=e.setLogin,i=e.setPassword;return s.a.createElement(R,{login:t,password:a,setLogin:n,setPassword:i})}}]),t}(n.Component),V={setLogin:function(e){return{type:"SET_LOGIN",payload:e}},setPassword:function(e){return{type:"SET_PASSWORD",payload:e}}},D=Object(_.b)(function(e){return{login:e.user.login,password:e.user.password}},V)(H),F=a(31),U=a.n(F),B=a(32),G=a.n(B),J=a(10),W=a.n(J),K=a(11),q=a.n(K),z=function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,s=new Array(n),i=0;i<n;i++)s[i]=arguments[i];return(a=Object(o.a)(this,(e=Object(u.a)(t)).call.apply(e,[this].concat(s)))).handleClick=function(){var e=a.props;(0,e.reply)(e.id)},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this.props,t=e.text,a=e.date,n=e.image,i=e.user,r=e.isChecked,c=e.replyMessage;return s.a.createElement("div",{className:r?q.a.checked:q.a.message,onClick:this.handleClick},s.a.createElement("div",{className:q.a.message_user},i),t&&s.a.createElement("div",{className:q.a.message_text},t),s.a.createElement("div",{className:q.a.message_time},a),n&&s.a.createElement("img",{src:"https://host-94-103-84-32.hosted-by-vdsina.ru"+n,className:q.a.message_image,alt:"images"}),c&&s.a.createElement("div",{className:q.a.replyBlock},s.a.createElement("div",{className:q.a.replyUser},c.user),s.a.createElement("div",{className:q.a.replyText},c.text)))}}]),t}(n.PureComponent),X=function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,s=new Array(n),i=0;i<n;i++)s[i]=arguments[i];return(a=Object(o.a)(this,(e=Object(u.a)(t)).call.apply(e,[this].concat(s)))).scrollChat=function(e){if(0===e.target.scrollTop){I(JSON.stringify({Type:"chat",Command:"earlier"})),e.target.scrollTop=10}},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this.props,t=e.messagesList,a=e.reply,n=e.replyMessage,i=[];return i=0!==t.length?t.map(function(e,t){return s.a.createElement(z,{text:e.text,image:e.image,user:e.user,date:e.date,id:e.id,key:t,reply:a,replyMessage:e.reply,isChecked:n===e.id})}):s.a.createElement("div",{className:W.a.loading},s.a.createElement("div",{className:W.a.line1}),s.a.createElement("div",{className:W.a.line2}),s.a.createElement("div",{className:W.a.line3})),s.a.createElement("div",{className:W.a.block},s.a.createElement("div",{className:W.a.chatName},this.props.activeChat),s.a.createElement("div",{className:W.a.messagesList,onScroll:this.scrollChat},i))}},{key:"componentDidUpdate",value:function(){var e=document.querySelector("."+W.a.messagesList);e.scrollTop=e.scrollHeight}},{key:"componentDidMount",value:function(){var e=document.querySelector("."+W.a.messagesList);e.scrollTop=e.scrollHeight}}]),t}(n.Component),Y=function(e){function t(){return Object(c.a)(this,t),Object(o.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this.props,t=e.messagesList,a=e.activeChat,n=e.reply,i=e.replyMessage;return s.a.createElement(X,{messagesList:t,activeChat:a,reply:n,replyMessage:i})}}]),t}(n.Component),Q={reply:A},Z=Object(_.b)(function(e){return{messagesList:e.messagesList,activeChat:e.activeChat,replyMessage:e.replyMessage}},Q)(Y),$=a(16),ee=a.n($),te=a(33),ae=a.n(te),ne=function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,s=new Array(n),i=0;i<n;i++)s[i]=arguments[i];return(a=Object(o.a)(this,(e=Object(u.a)(t)).call.apply(e,[this].concat(s)))).state={text:""},a.loadImage=function(e){var t=a.props.setImage,n=Object(g.a)(e.target.files),s=new ae.a;if(!n.length)return null;s.compress(n,{quality:.75,maxWidth:1920,maxHeight:1920}).then(function(e){t(e[0].prefix+e[0].data)})},a.pressEnter=function(e){"Enter"===e.key&&a.send()},a.changeTextInput=function(e){var t=e.target.value;t=t.replace("  "," "),a.setState({text:t})},a.send=function(){var e=a.state.text,t=a.props,n=t.image,s=t.setImage,i=t.replyMessage,r=t.reply;if(""!==e&&" "!==e[e.length-1]||""!==n){var c={Type:"chat",Command:"message"};e&&(c.Text=e),n&&(c.Image=n),i&&(c.Reply={id:i}),I(JSON.stringify(c)),s(""),r(""),a.setState({text:""})}},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this.state.text,t=this.props.image;return s.a.createElement("div",{className:ee.a.block},s.a.createElement("div",{className:ee.a.imagesBlock},s.a.createElement("img",{className:ee.a.image,src:t,alt:""}),s.a.createElement("label",{htmlFor:"file",className:ee.a.inputFile},s.a.createElement("input",{type:"file",accept:"image/jpeg,image/png",style:{display:"none"},id:"file",onChange:this.loadImage}))),s.a.createElement("input",{className:ee.a.inputText,type:"text",onChange:this.changeTextInput,value:e,onKeyPress:this.pressEnter}),s.a.createElement("button",{className:ee.a.button,onClick:this.send},"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c"))}}]),t}(n.PureComponent),se=function(e){function t(){return Object(c.a)(this,t),Object(o.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this.props,t=e.setImage,a=e.image,n=e.replyMessage,i=e.reply;return s.a.createElement(ne,{setImage:t,image:a,replyMessage:n,reply:i})}}]),t}(n.Component),ie=Object(_.b)(function(e){return{image:e.image,replyMessage:e.replyMessage}},{reply:A,setImage:function(e){return{type:"SET_IMAGE",payload:e}}})(se),re=function(e){function t(){return Object(c.a)(this,t),Object(o.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){return s.a.createElement("div",{className:G.a.block},s.a.createElement(Z,null),s.a.createElement(ie,null))}}]),t}(s.a.Component),ce=a(6),le=a.n(ce),oe=a(23),ue=a.n(oe),me=function(e){function t(){var e;return Object(c.a)(this,t),(e=Object(o.a)(this,Object(u.a)(t).call(this))).choiceChat=function(){var t={Type:"chat",Command:"choice",Chat:e.props.value.Chat};t=JSON.stringify(t),e.props.renderChatOutput(!1),e.props.removeMessagesList(),I(t),t={Type:"chat",Command:"connected"},t=JSON.stringify(t),I(t)},e.onPressEnter=function(t){"Enter"===t.key&&e.choiceSecretChat(e.props.value.Chat)},e.choiceSecretChat=function(t){var a={Type:"chat",Command:"choice",Chat:t,Password:e.state.chatPassword};a=JSON.stringify(a),I(a),e.props.renderChatOutput(!1),e.props.removeMessagesList(),e.setState({viewPasswordField:!1,chatPassword:""})},e.onChangePassword=function(t){e.setState({chatPassword:t})},e.state={viewPasswordField:!1,chatPassword:""},e}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e,t=this,a=this.props.value;if(!1===a.Closed)e=s.a.createElement("div",{onClick:this.choiceChat,className:ue.a.menu_chat_list_item},s.a.createElement("p",null,a.Chat));else if(!0===a.Closed){var n="";!0===this.state.viewPasswordField&&(n=s.a.createElement("input",{type:"text",value:this.props.chatPassword,onChange:function(e){return t.onChangePassword(e.target.value)},onKeyPress:function(e){return t.onPressEnter(e)},maxLength:30,autoFocus:!0})),e=s.a.createElement("div",{className:ue.a.menu_chat_list_item,onClick:function(){return t.setState({viewPasswordField:!0})},onMouseLeave:function(){return t.setState({viewPasswordField:!1})}},s.a.createElement("p",null,a.Chat),n)}return s.a.createElement(s.a.Fragment,null,e)}}]),t}(s.a.Component),_e=Object(_.b)(null,function(e){return Object(d.bindActionCreators)({removeMessagesList:O,renderChatOutput:w},e)})(me),pe=a(24),he=a.n(pe),de=a(25),ge=a.n(de),be=function(e){function t(){var e;return Object(c.a)(this,t),(e=Object(o.a)(this,Object(u.a)(t).call(this))).updateClock=function(){setInterval(e.tick,5e3)},e.tick=function(){e.setState({time:ge()().format("lll")})},e.state={time:ge()().format("lll")},e}return Object(m.a)(t,e),Object(l.a)(t,[{key:"componentDidMount",value:function(){this.updateClock()}},{key:"render",value:function(){var e=this.state.time;return s.a.createElement("div",{className:he.a.clockBlock},s.a.createElement("div",{className:he.a.clock},e))}}]),t}(s.a.PureComponent),ve=function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,s=new Array(n),i=0;i<n;i++)s[i]=arguments[i];return(a=Object(o.a)(this,(e=Object(u.a)(t)).call.apply(e,[this].concat(s)))).state={isView:!1,viewChatInput:!1},a.clickButton=function(){var e=a.state.isView;a.setState({isView:!e})},a.sendChat=function(e){if(""!==a.props.chatName&&"Enter"===e.key){var t={Type:"chat",Command:"create",Chat:a.props.chatName};""!==a.props.chatPassword&&(t.Password=a.props.chatPassword),t=JSON.stringify(t),L.send(t),a.props.removeChatName(),a.props.removeChatPassword()}},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this,t=this.state.isView,a=this.props.chatList;a=a.map(function(e,t){return s.a.createElement(_e,{value:e,key:t})});var i="";return!1===this.state.viewChatInput?i=s.a.createElement("p",{className:le.a.menu_chat,onClick:function(){return e.setState({viewChatInput:!e.state.viewChatInput})}},"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0447\u0430\u0442"):!0===this.state.viewChatInput&&(i=s.a.createElement(n.Fragment,null,s.a.createElement("p",{className:le.a.menu_chat,onClick:function(){return e.setState({viewChatInput:!e.state.viewChatInput})}},"\u0417\u0430\u043a\u0440\u044b\u0442\u044c"),s.a.createElement("p",{className:le.a.menu_chat},"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0447\u0430\u0442\u0430"),s.a.createElement("input",{type:"text",className:le.a.input,onChange:function(t){return e.props.addChatName(t.target.value)},onKeyPress:function(t){return e.sendChat(t)},value:this.props.chatName,onClick:function(){return e.props.removeChatName()},maxLength:12}),s.a.createElement("p",{className:le.a.menu_chat},"\u041f\u0430\u0440\u043e\u043b\u044c (\u043d\u0435 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e)"),s.a.createElement("input",{type:"text",className:le.a.input,onChange:function(t){return e.props.addChatPassword(t.target.value)},onKeyPress:function(t){return e.sendChat(t)},value:this.props.chatPassword,onClick:function(){return e.props.removeChatPassword()},maxLength:30}))),s.a.createElement(n.Fragment,null,s.a.createElement("div",{className:t?le.a.blockView:le.a.blockHide},s.a.createElement("button",{className:le.a.button,onClick:this.clickButton},s.a.createElement("div",{className:le.a.burger},s.a.createElement("div",{className:t?le.a.line1Active:le.a.line1}),s.a.createElement("div",{className:t?le.a.line2Active:le.a.line2}),s.a.createElement("div",{className:t?le.a.line3Active:le.a.line3}))),s.a.createElement("div",{className:le.a.menu},s.a.createElement("div",{className:le.a.menu_image}),s.a.createElement("p",{className:le.a.menu_login},this.props.login),i,s.a.createElement("p",{className:le.a.menu_chat},"\u0421\u043f\u0438\u0441\u043e\u043a \u0447\u0430\u0442\u043e\u0432:"),s.a.createElement("div",{className:le.a.menu_chat_list},a),s.a.createElement(be,null))))}}]),t}(n.PureComponent),Ce=Object(_.b)(function(e){return{login:e.user.login,chatList:e.chatList,chatName:e.chatName,chatPassword:e.chatPassword}},function(e){return Object(d.bindActionCreators)({addChatName:M,removeChatName:k,activeChat:S,removeMessagesList:O,removeChatPassword:N,addChatPassword:j},e)})(ve),Ee=a(9),fe=a.n(Ee),ye=function(e){function t(){var e,a;Object(c.a)(this,t);for(var n=arguments.length,s=new Array(n),i=0;i<n;i++)s[i]=arguments[i];return(a=Object(o.a)(this,(e=Object(u.a)(t)).call.apply(e,[this].concat(s)))).state={isView:!1},a.clickButton=function(){var e=a.state.isView;a.setState({isView:!e})},a.clearChat=function(){I(JSON.stringify({Type:"chat",Command:"purge"}))},a}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this.state.isView,t=this.props.usersOnline;return s.a.createElement("div",{className:e?fe.a.blockView:fe.a.blockHide},s.a.createElement("button",{className:fe.a.button,onClick:this.clickButton},s.a.createElement("div",{className:fe.a.burger},s.a.createElement("div",{className:e?fe.a.line1Active:fe.a.line1}),s.a.createElement("div",{className:e?fe.a.line2Active:fe.a.line2}),s.a.createElement("div",{className:e?fe.a.line3Active:fe.a.line3}))),s.a.createElement("div",{className:fe.a.menu},s.a.createElement("p",{className:fe.a.title},"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438 \u0432 \u0447\u0430\u0442\u0435"),s.a.createElement("ul",{className:fe.a.usersList},t.map(function(e){return s.a.createElement("li",{className:fe.a.user,key:e},e)})),s.a.createElement("button",{className:fe.a.buttonMenu,onClick:this.clearChat},"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0447\u0430\u0442")))}}]),t}(n.PureComponent),Oe=function(e){function t(){return Object(c.a)(this,t),Object(o.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this.props.usersOnline;return s.a.createElement(ye,{usersOnline:e})}}]),t}(n.Component),Me=Object(_.b)(function(e){return{usersOnline:e.usersOnline}},{})(Oe),ke=function(e){function t(){return Object(c.a)(this,t),Object(o.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){return s.a.createElement("div",{className:U.a.layout},s.a.createElement(Ce,null),s.a.createElement(re,null),s.a.createElement(Me,null))}}]),t}(s.a.Component),je=a(17),Ne=a.n(je),Se=function(){return s.a.createElement("div",{className:Ne.a.block},s.a.createElement("p",{className:Ne.a.text},"Connecting to server"),s.a.createElement("div",{className:Ne.a.line1}),s.a.createElement("div",{className:Ne.a.line2}),s.a.createElement("div",{className:Ne.a.line3}))},we=function(e){function t(){return Object(c.a)(this,t),Object(o.a)(this,Object(u.a)(t).apply(this,arguments))}return Object(m.a)(t,e),Object(l.a)(t,[{key:"render",value:function(){var e=this.props.page;return s.a.createElement("div",{className:"App"},"loading"===e&&s.a.createElement(Se,null),"authentification"===e&&s.a.createElement(D,null),"main"===e&&s.a.createElement(ke,null))}}]),t}(n.Component),Ae=Object(_.b)(function(e){return{page:e.page}})(we);r.a.render(s.a.createElement(_.a,{store:E},s.a.createElement(Ae,null)),document.getElementById("root"))}],[[34,1,2]]]);
//# sourceMappingURL=main.b662843f.chunk.js.map