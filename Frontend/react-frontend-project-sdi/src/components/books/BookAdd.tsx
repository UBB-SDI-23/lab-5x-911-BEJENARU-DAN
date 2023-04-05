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


export const BookAdd = () => {
    const navigate = useNavigate();
    const [publishers, setPublishers] = useState<Publisher[]>([])
    const [book, setBook] = useState<Omit<Book, "id">>({
        name: '',
        nrOfPages: 0,
        publisherID: undefined,
        releaseYear: 0,
        genre: '',
      });
    
    // Fetch the list of publishers from the server on component mount
    useEffect(() => {
        const getPublishers = async () => {
          const response = await axios.get<Publisher[]>(`${BACKEND_API_URL}/Publisher/`);
          setPublishers(response.data);
        };
        getPublishers();
      }, []);

    const addBook = async(event: {preventDefault: () => void}) => {
        event.preventDefault();
        try{
            await axios.post(`${BACKEND_API_URL}/Book/`, book);
            navigate("/Book/");
        }
        catch(error){
            console.log(error);
        }
    };

    return (
        <Container>
            <Card>
                <CardContent>
                    <IconButton
                        component = {Link} sx={{mr:3}} to={`/Book/`}>
                            <ArrowBackIcon/>
                    </IconButton>{" "}
                    <form onSubmit={addBook}>
                        <TextField
                            id="name"
                            label="Name"
                            variant="outlined"
                            fullWidth
                            sx={{mb:2}}
                            onChange={(event) => setBook({...book, name: event.target.value})}
                        />
                        <TextField
                            id="nrOfPages"
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
                            label="Release year"
                            variant="outlined"
                            fullWidth
                            sx={{mb:2}}
                            onChange={(event) => setBook({...book, releaseYear: parseInt(event.target.value)})}
                        />
                        <TextField
                            id="genre"
                            label="Genre"
                            variant="outlined"
                            fullWidth
                            sx={{mb:2}}
                            onChange={(event) => setBook({...book, genre: event.target.value})}
                        />
                        <Button type="submit">Add book</Button>
                    </form>
                </CardContent>
                <CardActions></CardActions>
            </Card>
        </Container>
    )
}


