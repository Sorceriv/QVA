import './ChatButton.scss'

interface Props {
    onClick: (text: string) => void,
}

function ChatDialogue({onClick}: Props) {
    return (
        <>
            <button className="chat-button" onClick={() => {onClick("Test")}}></button>
        </>
    )
}

export default ChatDialogue;