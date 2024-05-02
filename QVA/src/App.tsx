import ChatButton from './components/ChatButton/ChatButton';
import ChatBox from './components/ChatBox/ChatBox';
import './App.scss';
import { useState } from 'react';

function App() {
  const [chatOpen, setChatOpen] = useState(false);
  const onButtonClick = (text: string) => {
    console.log(text);
    setChatOpen(!chatOpen);
  }
  return (
    <>
      <ChatButton onClick={onButtonClick}/>
      <ChatBox opened={chatOpen}/>
    </>
  )
}

export default App
