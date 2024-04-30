import './ChatBox.scss';
import ChatDialogue from './../ChatDialogue/ChatDialogue';

function ChatBox() {
    return (
        <>
            <div className="main-chatbox-container">
                <div className="top-area-container">

                </div>
                <div className="chat-area">
                    {/* <ChatDialogue /> */}
                    <ChatDialogue role={"user"} text="HAHAHAHA"/>
                </div>
                <div className="input-area">

                </div>
            </div>
        </>
    )
}

export default ChatBox;