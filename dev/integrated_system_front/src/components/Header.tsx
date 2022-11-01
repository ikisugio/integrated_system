import { AppBar, Toolbar, Typography } from '@mui/material'
import { styled } from '@mui/material/styles';
import React from 'react'
import AccountCircleIcon from '@mui/icons-material/AccountCircle';


const Header = () => {
return (
    <AppBar position="static">
    <CustomeToolbar>
        <FlexedTypography>
        介護労働安定センター
        </FlexedTypography>
        <AccountCircleIcon />
    </CustomeToolbar>
    </AppBar>
    );
};


const FlexedTypography = styled(Typography)({
    flex: 1
});
const CustomeToolbar = styled(Toolbar)({
    backgroundColor: "rgba(255,255,255,0.9)",
});

export default Header;
