import {
	TableContainer,
	Paper,
	Table,
	TableHead,
	TableRow,
	TableCell,
	TableBody,
	CircularProgress,
	Container,
	IconButton,
	Tooltip,
} from "@mui/material";
import React from "react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Book } from "../../models/book";
import { Publisher } from "../../models/publisher";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';
import ArrowDownwardIcon from '@mui/icons-material/ArrowDownward';
import UnfoldMoreIcon from '@mui/icons-material/UnfoldMore';
import { BACKEND_API_URL } from "../../constants";

export const BooksShowAll = () => {
    const [loading, setLoading] = useState(false);
    const [books, setBooks] = useState<Book[]>([]);
    const [sortOrder, setSortOrder] = useState<"asc" | "desc" | "">("");
    useEffect( () => {
            setLoading(true);
            fetch(`${BACKEND_API_URL}/Book/`)
            .then((response) => response.json())
            .then((data) => {
                setBooks(data);
                setLoading(false);
            });
    }, []);

    const handleSortByYear = () => {
        if (sortOrder === "asc") {
          setSortOrder("desc");
          setBooks((prevBooks) =>
            [...prevBooks].sort((a, b) => b.releaseYear - a.releaseYear)
          );
        } else if (sortOrder === "desc") {
          setSortOrder("");
          setBooks((prevBooks) =>
            [...prevBooks].sort((a, b) => a.id - b.id)
          );
        } else {
          setSortOrder("asc");
          setBooks((prevBooks) =>
            [...prevBooks].sort((a, b) => a.releaseYear - b.releaseYear)
          );
        }
      };

    return (
        <Container>
            <h1>All books</h1>
            {loading && <CircularProgress/>}
            {!loading && books.length === 0 && <p>No books found.</p>}
            {!loading && (
                <IconButton component={Link} sx={{mr:3}} to={`/Book/add/`}>
                    <Tooltip title="Add a new book" arrow>
                        <AddIcon color="primary" />
                    </Tooltip>
                </IconButton>
            )}
            {!loading && books.length > 0 && (
                <TableContainer component={Paper}>
                    <Table sx={{minWidth: 650}} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell align="center">#</TableCell>
                                <TableCell align="center">Name</TableCell>
                                <TableCell align="center">Pages</TableCell>
                                <TableCell align="center">Publisher ID</TableCell>
                                <TableCell align="center">
                                <Tooltip title="Sort by Release Year" arrow>
                                    <IconButton onClick={handleSortByYear}>
                                        {sortOrder === "asc" ? (
                                            <ArrowUpwardIcon color="primary" />
                                        ) : sortOrder === "desc" ? (
                                            <ArrowDownwardIcon color="primary" />
                                        ) : (
                                            <UnfoldMoreIcon color="primary" />
                                        )}
                                    </IconButton>
                                    </Tooltip>
                                    Release Year
                                    </TableCell>
                                <TableCell align="center">Genre</TableCell>
                                <TableCell align="center">Operations</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {books.map((book: Book, index) => (
                                <TableRow key={book.id}>
                                    <TableCell align="center" component = "th" scope="row">{index + 1}</TableCell>
                                    <TableCell align="center" component = "th" scope="row">
                                        <Link to = {`/Book/${book.id}/details/`} title = "View book details">
                                            {book.name}
                                        </Link>
                                    </TableCell>
                                    <TableCell align="center">{book.nrOfPages}</TableCell>
                                    <TableCell align="center">
                                        <>{book?.publisherID}</>
                                    </TableCell>
                                    <TableCell align="center">{book.releaseYear}</TableCell>
                                    <TableCell align="center">{book.genre}</TableCell>
                                    <TableCell align="center">
                                        <IconButton
                                            component={Link}
                                            sx={{mr:3}}
                                            to={`/Book/${book.id}/details/`}>
                                            <Tooltip title = "View book details" arrow>
                                                <ReadMoreIcon color="primary"/>
                                            </Tooltip>
                                        </IconButton>
                                        <IconButton 
                                            component={Link}
                                            sx={{mr:3}}
                                            to={`/Book/${book.id}/edit/`}>
                                                <EditIcon/>
                                        </IconButton>
                                        <IconButton
                                            component = {Link}
                                            sx={{mr:3}}
                                            to={`/Book/${book.id}/delete/`}>
                                                <DeleteForeverIcon sx={{color:"red"}}/>
                                        </IconButton>
                                    </TableCell>
                                    
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            )}
        </Container>
        
            
    )
  }