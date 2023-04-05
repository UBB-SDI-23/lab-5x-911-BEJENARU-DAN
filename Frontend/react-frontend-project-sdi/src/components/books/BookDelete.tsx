import { Container, Card, CardContent, IconButton, CardActions, Button } from "@mui/material";
import { Link, useNavigate, useParams } from "react-router-dom";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import { BACKEND_API_URL } from "../../constants";


export const BookDelete = () => {
    const { bookID } = useParams();
    const navigate = useNavigate();
    
    const handleDelete = async( event: {preventDefault : () => void }) => {
        event?.preventDefault();
        await axios.delete(`${BACKEND_API_URL}/Book/${bookID}/`);
        navigate("/Book/");
    };
    
    const handleCancel = (event: {preventDefault: () => void}) => {
        event.preventDefault();
        navigate("/Book/");
    }

    return(
        <Container>
            <Card>
                <CardContent>
                    <IconButton 
                        component={Link}
                        sx={{mr:3}}
                        to={`/Book/`}>
                            <ArrowBackIcon/>
                        </IconButton>
                        Are you sure you want to delete this book?
                </CardContent>
                <CardActions>
                    <Button onClick={handleDelete}>Delete</Button>
                    <Button onClick={handleCancel}>Cancel</Button>
                </CardActions>
            </Card>
        </Container>
    )
}
