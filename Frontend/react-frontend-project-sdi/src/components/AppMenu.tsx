
import { AppBar, Box, Button, IconButton, Toolbar, Typography } from "@mui/material";
import {Link, useLocation } from "react-router-dom"

export const AppMenu = () => {
    const location = useLocation();
    const path = location.pathname;

    return (
            <Box sx={{flexGrow: 1}}>
                <AppBar>
                    <Toolbar>
                        <IconButton
                            component={Link}
                            to="/"
                            size="large"
                            edge="start"
                            aria-label="school"
                            sx={{ mr: 2 }}
                        >
                        </IconButton>
                        <Typography variant="h6" component="div" sx={{ mr: 5 }}>
                            Books management
                        </Typography>
                        <Button 
                            variant={path.startsWith("/Book/") ? "outlined" : "text"}
                            to="/Book/"
                            component={Link}
                            color="inherit"
                            sx={{mr:5}}
                        >
                            Books
                        </Button>
                        <Button 
                            variant={path.startsWith("/Publisher/PublisherCountbyBooks/") ? "outlined" : "text"}
                            to="/Publisher/PublisherCountbyBooks/"
                            component={Link}
                            color="inherit"
                            sx={{mr:5}}
                        >
                            Statistics
                        </Button>
                    </Toolbar>
                </AppBar>
            </Box>
    )
}