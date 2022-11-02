import './App.css';
import { Grid } from '@mui/material';
import Header from './components/Header';
import Content from './components/Content';
import { styled } from '@mui/material/styles';

const StyledHeader = styled(Header)({
  backgroundColor: "black",
});

function App() {
  return (
    <>
      <StyledHeader/>
      <Content />
    </>
  );
}


export default App;
