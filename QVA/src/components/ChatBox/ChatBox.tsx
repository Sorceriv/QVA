import './ChatBox.scss';
import ChatDialogue from './../ChatDialogue/ChatDialogue';

import axios from "axios";
import { useEffect, useState } from 'react';

interface Props {
    opened: boolean,
}

function ChatBox({opened}: Props) {
    //CORS logic happens here I guess
    // var conversation = [
    //     {
    //         role: "user",
    //         message: "Hi",
    //     },
    //     {
    //         role: "bot",
    //         message: "Hello, I am bot.",
    //     },
    //     {
    //         role: "user",
    //         message: "I need help in fixing vulnerabilities regarding Linux systems failing to start whenever I reboot it.",
    //     },
    //     {
    //         role: "bot",
    //         message: "Sure! Let me help you with that. To do that we need to dawjidjasijdoawkdaw;kdawdwa",
    //     },
    //     {
    //         role: "user",
    //         message: "Thanks.",
    //     },
    // ];

    const [conversation, setConversation] = useState([] as any);
    const [message, setMessage] = useState({role: "bot", message:"Hi, tell me your problems on your machine."})
    // useEffect(() => {
    //     fetch("http://localhost:5000")
    //       .then((res) => res.json())
    //       .then((data) => {
    //         console.log(data);
    //         //setData(data.message);
    //       });
    // }, []);

    const handleSubmit = async(event: any) => {
        event.preventDefault();

        const formData = new FormData();
        console.log(event.target["user-text"].value);

        formData.append("text", event.target["user-text"].value);

        //Add user chat to conversaion use useeffect for interval and typing effect
        setConversation([...conversation, {role: "user", message: event.target["user-text"].value}])
        try {
            axios.post("http://localhost:5000/upload", formData).then((res: any) => {
                console.log("MESSAGE: " + res.data.message);
                //Add bot response to conversation useeffect for interval and typing effect
                setMessage({role:"bot", message: res.data.message});
            });
        } catch (error) {
            console.log("ERROR: " + error);
        }
    }
    //add automatic scrolldown on new chat
    //fix empty message starter/fix errors when emptying fixed using as any but find a more readable and optimized solution
    //Empty textbox when typing
    
    useEffect(() => {
        setConversation([...conversation, message]);
    }, [message]);

    return (
        <>
            <div className="main-chatbox-container" style={opened ? {width: "500px", height: "500px"} : {width: "0px", height: "0px"}}>
                <div className="top-area-container">

                </div>
                <div className="chat-area">
                    {/* <ChatDialogue /> */}
                    {conversation.map((item, key) => (
                        <ChatDialogue key={key} role={item.role} message={item.message}/>
                    ))}
                </div>
                <div className="input-area">
                    <form onSubmit={handleSubmit}>
                        <input name="user-text" type="text"></input>
                        <input type="submit" value="→"></input> {/**ajax submission, find reference used in cgi*/}
                    </form>
                </div>
            </div>
        </>
    )
}

export default ChatBox;