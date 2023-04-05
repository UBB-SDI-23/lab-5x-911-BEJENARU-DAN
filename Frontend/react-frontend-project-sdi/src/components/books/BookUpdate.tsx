import { Button, Card, CardActions, CardContent, FormControl, IconButton, InputLabel, MenuItem, Select, SelectChangeEvent, TextField } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import axios from "axios";
import { Book } from "../../models/book";
import { Publisher } from "../../models/publisher";
import { Address } from "../../models/address";
import { BACKEND_API_URL } from "../../constants";



export const BookUpdate = () => {
    const { bookID } = useParams();
    const navigate = useNavigate();
    const [publishers, setPublishers] = useState<Publisher[]>([])
    const [loading, setLoading] = useState(false);
    const [book, setBook] = useState<Omit<Book, "id">>({
        name: '',
        nrOfPages: 0,
        publisherID: undefined,
        releaseYear: 0,
        genre: '',
      });

    useEffect(() => {
        const getPublishers = async () => {
            setLoading(true);
            const response = await axios.get<Publisher[]>(`${BACKEND_API_URL}/Publisher/`);
            setPublishers(response.data);
            setLoading(false);
        };
        getPublishers();
        const fetchBook = async () => {
            setLoading(true);
            const response = await axios.get<Book>(`${BACKEND_API_URL}/Book/${bookID}/`);
            const book = response.data
            setBook(book);
            setLoading(false);
        }
        fetchBook();
      }, [bookID]);

    const updateBook = async(event: {preventDefault: () => void}) => {
        event.preventDefault();
        try{
            await axios.put(`${BACKEND_API_URL}/Book/${bookID}/`, book);
            navigate("/Book/");
        }
        catch(error){
            console.log(error);
        }
    };

    const updateCancel = (event: {preventDefault: () => void}) => {
        event.preventDefault();
        navigate("/Book/");
    };

    return (
        <Container>
            <Card>
                <CardContent>
                <IconButton
                        component = {Link} sx={{mr:3}} to={`/Book/`}>
                            <ArrowBackIcon/>
                    </IconButton>{" "}
                    <form>
                        <TextField
                            id="name"
                            value={book.name}
                            label="Name"
                            variant="outlined"
                            fullWidth
                            sx={{mb:2}}
                            onChange={(event) => setBook({...book, name: event.target.value})}
                        />
                        <TextField
                            id="nrOfPages"
                            value={book.nrOfPages}
                            label="Number of pages"
                            variant="outlined"
                            fullWidth
                            sx={{mb:2}}
                            onChange={(event) => setBook({...book, nrOfPages: parseInt(event.target.value)})}
                        />
                        <Select
                            id="publisherID"
                            value={(book.publisherID as Publisher)?.id }
                            onChange={(event: SelectChangeEvent<number>) => {
                                const publisherId = event.target.value as number;
                                const publisher = publishers.find((publisher) => publisher.id === publisherId);
                                setBook({
                                  ...book,
                                  publisherID: publisher?.id,
                                });
                              }}

                            label="Publisher"
                            variant="outlined"
                            fullWidth
                            sx={{ mb: 2 }}
                            >
                            {publishers.map((publisher) => (
                            <MenuItem key={publisher.id} value={publisher.id}>
                                {publisher.id};{publisher.name};<>{publisher.address}</>;{publisher.email};{publisher.webAddress}
                            </MenuItem>
                            ))}
                        </Select>
                        <TextField
                            id="releaseYear"
                            value={book.releaseYear}
                            label="Release year"
                            variant="outlined"
                            fullWidth
                            sx={{mb:2}}
                            onChange={(event) => setBook({...book, releaseYear: parseInt(event.target.value)})}
                        />
                        <TextField
                            id="genre"
                            value={book.genre}
                            label="Genre"
                            variant="outlined"
                            fullWidth
                            sx={{mb:2}}
                            onChange={(event) => setBook({...book, genre: event.target.value})}
                        />
                    </form>
                </CardContent>
                <CardActions>
                    <Button onClick={updateBook}>Update</Button>
                    <Button onClick={updateCancel}>Cancel</Button>
                </CardActions>
            </Card>
        </Container>
        )
}