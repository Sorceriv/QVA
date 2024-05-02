import './ChatBox.scss';
import ChatDialogue from './../ChatDialogue/ChatDialogue';

interface Props {
    opened: boolean,
}

function ChatBox({opened}: Props) {
    //CORS logic happens here I guess
    var conversation = [
        {
            role: "user",
            message: "Hi",
        },
        {
            role: "bot",
            message: "Hello, I am bot.",
        },
        {
            role: "user",
            message: "I need help in fixing vulnerabilities regarding Linux systems failing to start whenever I reboot it.",
        },
        {
            role: "bot",
            message: "Sure! Let me help you with that. To do that we need to dawjidjasijdoawkdaw;kdawdwa",
        },
        {
            role: "user",
            message: "Thanks.",
        },
    ]
    return (
        <>
            <div className="main-chatbox-container" style={opened ? {width: "500px", height: "500px"} : {width: "0px", height: "0px"}}>
                <div className="top-area-container">

                </div>
                <div className="chat-area">
                    {/* <ChatDialogue /> */}
                    {conversation.map((item, key) => (
                        <ChatDialogue role={item.role} message={item.message}/>
                    ))}
                </div>
                <div className="input-area">

                </div>
            </div>
        </>
    )
}

export default ChatBox;