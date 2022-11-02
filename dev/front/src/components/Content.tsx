import React, {useState, useEffect} from 'react';
import axios from 'axios';
import Table from './Table'
import { styled } from '@mui/material/styles';


const StyledTable = styled(Table)({
    padding: "10px",
  });

function Content() {
    return (
        <StyledTable />
    )
}

export default Content