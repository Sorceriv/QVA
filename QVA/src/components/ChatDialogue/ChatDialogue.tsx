import './ChatDialogue.scss'

interface Props {
    role: String,
    message: String,

}

function ChatDialogue({role, message}: Props) {
    return (
        <>
            <div style={{float: role=="bot" ? "left" : "right"}} className="dialogue-container">
                <span>{message}</span>
            </div>
        </>
    )
}

export default ChatDialogue;