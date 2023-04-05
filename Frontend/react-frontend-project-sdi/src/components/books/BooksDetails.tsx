import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom"
import { Book } from "../../models/book";
import { Card, CardActions, CardContent, Container, IconButton } from "@mui/material";
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import { BACKEND_API_URL } from "../../constants";
import axios from "axios";
import { Publisher } from "../../models/publisher";

export const BookDetails = () => {
    const {bookID} = useParams();
    const [loading, setLoading] = useState(false);
    const [book, setBook] = useState<Book>();

    useEffect( () => {
        const fetchBook = async () => {   
            setLoading(true);  
            const response = await axios.get<Book>(`${BACKEND_API_URL}/Book/${bookID}/`);
            const book = response.data;
            setBook(book);
            setLoading(false);
    };
    fetchBook();
}, [bookID]);
    
   
    return(
        <Container>
            <Card>
                <CardContent>
                    <IconButton component={Link} sx={{mr: 3}} to={`/Book/`}>
                        <ArrowBackIcon />
                    </IconButton>{" "}
                    <h1>Book Details</h1>
                    <p>Name: {book?.name}</p>
                    <p>Number pages: {book?.nrOfPages}</p>
                    <p>Publisher: <>{(book?.publisherID as Publisher)?.name} {(book?.publisherID as Publisher)?.id}</></p>
                    <p>Release Year: {book?.releaseYear}</p>
                    <p>Genre: {book?.genre}</p>
                </CardContent>
                <CardActions>
                    <IconButton component={Link} sx={{ mr: 3 }} to={`/Book/${bookID}/edit/`}>
                        <EditIcon/>
                    </IconButton>

                    <IconButton component={Link} sx={{ mr: 3 }} to={`/Book/${bookID}/delete/`}>
						<DeleteForeverIcon sx={{ color: "red" }} />
					</IconButton>
                </CardActions>
            </Card>
        </Container>
    )
}

