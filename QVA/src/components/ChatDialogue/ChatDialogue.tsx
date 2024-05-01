import './ChatDialogue.scss'

interface Props {
    role: String,
    message: String,

}

function ChatDialogue({role, message}: Props) {
    return (
        <>

        <div className={"dialogue-container " + (role == "bot" ? "left" : "right")}>
            {message}
        </div>

        </>
    )
}

export default ChatDialogue;