import ChatButton from './components/ChatButton/ChatButton';
import ChatBox from './components/ChatBox/ChatBox';
import './App.scss';

function App() {
  const onButtonClick = (text: string) => {
    console.log(text);
  }
  return (
    <>
      <ChatButton onClick={onButtonClick}/>
      <ChatBox/>
    </>
  )
}

export default App
